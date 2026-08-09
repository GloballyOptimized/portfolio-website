import json
import os
import re
import queue
import threading
from typing import Generator

import httpx
from dotenv import load_dotenv

from .context import build_messages, SYSTEM_PROMPT
from .tools import execute_sql, rows_to_vega_values
from .sessions import load_session, save_session, append_turn

load_dotenv()

_GEMINI_KEY = os.getenv("GEMINI_API_KEY")
_MODEL = os.getenv("DATASTORY_MODEL", "gemini-2.0-flash")
_GEMINI_BASE = "https://generativelanguage.googleapis.com/v1beta/models"

MAX_STEPS = 8
MAX_RETRIES = 2


# ── LLM call ──────────────────────────────────────────────────────────────────

def _call_llm(contents: list[dict]) -> str:
    """Call Gemini generateContent, return model text."""
    url = f"{_GEMINI_BASE}/{_MODEL}:generateContent?key={_GEMINI_KEY}"
    payload = {
        "systemInstruction": {"parts": [{"text": SYSTEM_PROMPT}]},
        "contents": contents,
        "generationConfig": {
            "temperature": 0.1,
            "maxOutputTokens": 2048,
        },
    }
    with httpx.Client(timeout=60) as client:
        resp = client.post(url, json=payload)
        resp.raise_for_status()
    candidates = resp.json().get("candidates", [])
    if not candidates:
        raise ValueError("Gemini returned no candidates")
    # Gemma returns thinking parts (thought=True) + response parts; skip thought parts
    parts = candidates[0]["content"]["parts"]
    text = " ".join(p["text"] for p in parts if not p.get("thought") and p.get("text"))
    return text or parts[-1].get("text", "")


# ── Action parser ──────────────────────────────────────────────────────────────

def _parse_action(text: str) -> dict | None:
    """
    Extract action JSON from model output.
    Handles: ```json blocks, <action> tags, bare JSON objects.
    """
    # 1. ```json ... ``` block (primary format for Gemma)
    match = re.search(r"```(?:json)?\s*(.*?)```", text, re.DOTALL)
    if match:
        raw = match.group(1).strip()
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            pass

    # 2. <action>...</action> tag
    match = re.search(r"<action>(.*?)</action>", text, re.DOTALL)
    if match:
        raw = match.group(1).strip()
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            pass

    # 3. bare JSON object containing "type"
    match = re.search(r'\{\s*"type"\s*:.*?\}', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            pass

    return None


# ── SSE event helpers ──────────────────────────────────────────────────────────

def _evt(q: queue.Queue, event_type: str, data: dict) -> None:
    q.put({"event": event_type, "data": data})


# ── Agent loop (runs in thread) ────────────────────────────────────────────────

def _run_agent(question: str, session_id: str, q: queue.Queue) -> None:
    try:
        session = load_session(session_id)
        history = session.get("history", [])
        sql_steps: list[dict] = []
        retries = 0
        full_answer = ""

        _evt(q, "status", {"text": "thinking..."})

        for step in range(MAX_STEPS):
            messages = build_messages(question, history, sql_steps)

            try:
                raw = _call_llm(messages)
            except Exception as e:
                _evt(q, "error", {"text": f"LLM error: {e}"})
                return

            action = _parse_action(raw)

            if action is None:
                retries += 1
                if retries > MAX_RETRIES:
                    _evt(q, "error", {"text": "Could not parse a valid action from the model. Try rephrasing."})
                    return
                _evt(q, "status", {"text": f"retrying... ({retries}/{MAX_RETRIES})"})
                continue

            retries = 0  # reset on successful parse

            if action.get("type") == "sql":
                sql = action.get("query", "").strip()
                reasoning = action.get("reasoning", "")
                _evt(q, "sql", {"sql": sql, "reasoning": reasoning, "step": step + 1})

                result = execute_sql(sql)

                if result["error"]:
                    _evt(q, "sql_error", {"error": result["error"], "sql": sql})
                    sql_steps.append({"sql": sql, "result_preview": "", "row_count": 0, "error": result["error"]})
                else:
                    _evt(q, "sql_result", {
                        "row_count": result["row_count"],
                        "columns": result["columns"],
                        "rows": result["rows"][:100],  # send up to 100 rows to frontend
                    })
                    sql_steps.append({
                        "sql": sql,
                        "result_preview": result["result_preview"],
                        "row_count": result["row_count"],
                        "error": None,
                    })

            elif action.get("type") == "answer":
                full_answer = action.get("text", "").strip()
                chart_spec = action.get("chart")

                # if chart references data from sql results, embed the latest rows
                if chart_spec and sql_steps and not chart_spec.get("data", {}).get("values"):
                    last_step_idx = next(
                        (i for i in reversed(range(len(sql_steps))) if not sql_steps[i].get("error")),
                        None,
                    )
                    if last_step_idx is not None:
                        # re-run last SQL to get full rows for chart
                        last_sql = sql_steps[last_step_idx]["sql"]
                        chart_result = execute_sql(last_sql)
                        if not chart_result["error"]:
                            chart_spec.setdefault("data", {})["values"] = rows_to_vega_values(chart_result["rows"], 500)

                _evt(q, "answer", {"text": full_answer, "chart": chart_spec})

                # persist to session
                append_turn(session, question, full_answer)
                save_session(session_id, session)
                _evt(q, "done", {})
                return

            else:
                _evt(q, "error", {"text": f"Unknown action type: {action.get('type')}"})
                return

        # exceeded max steps
        _evt(q, "error", {"text": f"Reached max steps ({MAX_STEPS}) without a final answer."})

    except Exception as e:
        _evt(q, "error", {"text": f"Agent error: {e}"})
    finally:
        q.put(None)  # sentinel


# ── Public SSE generator ───────────────────────────────────────────────────────

def stream_agent(question: str, session_id: str) -> Generator[str, None, None]:
    """
    Generator that yields SSE-formatted strings.
    Each event: "data: <json>\\n\\n"
    """
    q: queue.Queue = queue.Queue()
    t = threading.Thread(target=_run_agent, args=(question, session_id, q), daemon=True)
    t.start()

    while True:
        item = q.get()
        if item is None:
            break
        yield f"data: {json.dumps(item, default=str)}\n\n"
