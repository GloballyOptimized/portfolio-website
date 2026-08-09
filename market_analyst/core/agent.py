import json
import os
import re
import uuid
import queue
import threading
import logging
from typing import Generator

import httpx
from dotenv import load_dotenv

from .context import build_query_gen_messages, build_synthesis_messages
from .searcher import search_query
from .database import save_session

load_dotenv()

logger = logging.getLogger(__name__)

_GEMINI_KEY  = os.getenv("GEMINI_API_KEY")
_MODEL       = os.getenv("DATASTORY_MODEL", "gemma-4-26b-a4b-it")
_GEMINI_BASE = "https://generativelanguage.googleapis.com/v1beta/models"

MAX_QUERIES = 20
SEARCH_DELAY = 1.5  # seconds between searches (DDG rate-limit buffer)


def _call_gemini(contents: list[dict], system: str = "") -> str:
    url = f"{_GEMINI_BASE}/{_MODEL}:generateContent?key={_GEMINI_KEY}"
    payload = {
        "contents": contents,
        "generationConfig": {"temperature": 0.2, "maxOutputTokens": 4096},
    }
    if system:
        payload["systemInstruction"] = {"parts": [{"text": system}]}
    with httpx.Client(timeout=120) as client:
        resp = client.post(url, json=payload)
        resp.raise_for_status()
    candidates = resp.json().get("candidates", [])
    if not candidates:
        raise ValueError("Gemini returned no candidates")
    parts = candidates[0]["content"]["parts"]
    # skip thought parts (Gemma thinking model)
    text = " ".join(p["text"] for p in parts if not p.get("thought") and p.get("text"))
    return text or parts[-1].get("text", "")


def _extract_json(text: str):
    """Extract JSON from model output — tries multiple strategies."""
    # code block first
    m = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if m:
        try:
            return json.loads(m.group(1).strip())
        except json.JSONDecodeError:
            pass
    # raw parse
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError:
        pass
    # line-by-line — model sometimes puts JSON on its own line
    for line in text.splitlines():
        line = line.strip()
        if line.startswith(('[', '{')):
            try:
                return json.loads(line)
            except json.JSONDecodeError:
                pass
    # last resort: find first [ or { block
    for pat in (r"(\[[\s\S]*?\])", r"(\{[\s\S]*?\})"):
        m = re.search(pat, text)
        if m:
            try:
                return json.loads(m.group(1))
            except json.JSONDecodeError:
                pass
    logger.warning("[market_analyst] _extract_json failed. raw (first 400): %s", text[:400])
    return None


def _evt(q: queue.Queue, event_type: str, data: dict) -> None:
    q.put({"event": event_type, "data": data})


def _run_research(question: str, q: queue.Queue) -> None:
    import time
    session_id = str(uuid.uuid4())
    try:
        # ── Phase 1: Generate search queries ──────────────────────
        _evt(q, "llm_call", {
            "fn": "generate_queries", "phase": "start",
            "model": _MODEL, "detail": question[:120],
        })

        messages = build_query_gen_messages(question, MAX_QUERIES)
        t0 = time.time()
        try:
            raw = _call_gemini(messages, system="Output ONLY a valid JSON array of strings. No markdown fences, no explanation, no preamble. Start your response with [ and end with ].")
        except Exception as e:
            _evt(q, "error", {"text": f"LLM error (query gen): {e}"})
            return

        queries = _extract_json(raw)
        if not isinstance(queries, list):
            _evt(q, "error", {"text": "Could not parse search queries from model."})
            return

        queries = [str(q_) for q_ in queries if q_][:MAX_QUERIES]
        elapsed = round(time.time() - t0, 1)
        _evt(q, "llm_call", {
            "fn": "generate_queries", "phase": "end",
            "detail": f"{len(queries)} queries generated", "elapsed": elapsed,
        })
        _evt(q, "queries", {"queries": queries, "count": len(queries)})

        # ── Phase 2: Execute searches ──────────────────────────────
        results_map: dict[str, list[dict]] = {}
        for i, query in enumerate(queries):
            _evt(q, "searching", {"query": query, "index": i + 1, "total": len(queries)})
            results = search_query(query)
            results_map[query] = results
            _evt(q, "search_done", {
                "query": query,
                "index": i + 1,
                "total": len(queries),
                "result_count": len(results),
                "results": results,
            })
            time.sleep(SEARCH_DELAY)

        total_results = sum(len(v) for v in results_map.values())

        # ── Phase 3: Synthesise ────────────────────────────────────
        _evt(q, "llm_call", {
            "fn": "synthesize", "phase": "start",
            "model": _MODEL,
            "detail": f"{total_results} snippets from {len(queries)} queries",
        })
        synth_messages = build_synthesis_messages(question, queries, results_map)
        t0 = time.time()
        try:
            raw_analysis = _call_gemini(synth_messages, system="Output ONLY valid JSON matching the exact structure requested. No markdown fences, no explanation. Start your response with { and end with }.")
        except Exception as e:
            _evt(q, "error", {"text": f"LLM error (synthesis): {e}"})
            return

        analysis = _extract_json(raw_analysis)
        if not analysis or not isinstance(analysis, dict):
            _evt(q, "error", {"text": "Could not parse analysis from model."})
            return

        elapsed = round(time.time() - t0, 1)
        _evt(q, "llm_call", {
            "fn": "synthesize", "phase": "end",
            "detail": "analysis complete", "elapsed": elapsed,
        })

        # ── Phase 4: Persist ───────────────────────────────────────
        try:
            analysis_text = json.dumps(analysis)
            save_session(session_id, question, queries, results_map,
                         analysis_text, analysis.get("confidence", "medium"))
        except Exception as e:
            logger.warning("[market_analyst] failed to persist session: %s", e)

        _evt(q, "analysis", {"session_id": session_id, "analysis": analysis})
        _evt(q, "done", {"session_id": session_id})

    except Exception as e:
        _evt(q, "error", {"text": f"Research error: {e}"})
    finally:
        q.put(None)


def stream_research(question: str) -> Generator[str, None, None]:
    q: queue.Queue = queue.Queue()
    t = threading.Thread(target=_run_research, args=(question, q), daemon=True)
    t.start()
    while True:
        item = q.get()
        if item is None:
            break
        yield f"data: {json.dumps(item, default=str)}\n\n"
