import json
import os
import re
import queue
import threading
from typing import Generator

import httpx
from dotenv import load_dotenv

from .context import build_messages, SYSTEM_PROMPT
from .database import query as run_query

load_dotenv()

_GEMINI_KEY  = os.getenv("GEMINI_API_KEY")
_MODEL       = os.getenv("DATASTORY_MODEL", "gemma-4-26b-a4b-it")
_GEMINI_BASE = "https://generativelanguage.googleapis.com/v1beta/models"

MAX_STEPS   = 6
MAX_RETRIES = 2


def _call_llm(contents: list[dict]) -> str:
    url = f"{_GEMINI_BASE}/{_MODEL}:generateContent?key={_GEMINI_KEY}"
    payload = {
        "systemInstruction": {"parts": [{"text": SYSTEM_PROMPT}]},
        "contents": contents,
        "generationConfig": {"temperature": 0.1, "maxOutputTokens": 2048},
    }
    with httpx.Client(timeout=90) as client:
        resp = client.post(url, json=payload)
        resp.raise_for_status()
    candidates = resp.json().get("candidates", [])
    if not candidates:
        raise ValueError("Gemini returned no candidates")
    parts = candidates[0]["content"]["parts"]
    text = " ".join(p["text"] for p in parts if not p.get("thought") and p.get("text"))
    return text or parts[-1].get("text", "")


def _parse_action(text: str) -> dict | None:
    m = re.search(r"```(?:json)?\s*(.*?)```", text, re.DOTALL)
    if m:
        try:
            return json.loads(m.group(1).strip())
        except json.JSONDecodeError:
            pass
    m = re.search(r'\{\s*"type"\s*:.*?\}', text, re.DOTALL)
    if m:
        try:
            return json.loads(m.group(0))
        except json.JSONDecodeError:
            pass
    return None


def _rows_to_vega(rows: list[dict], limit: int = 500) -> list[dict]:
    result = []
    for row in rows[:limit]:
        clean = {}
        for k, v in row.items():
            clean[k] = v.isoformat() if hasattr(v, "isoformat") else v
        result.append(clean)
    return result


def _evt(q: queue.Queue, event_type: str, data: dict) -> None:
    q.put({"event": event_type, "data": data})


def _run_agent(question: str, q: queue.Queue) -> None:
    try:
        sql_steps: list[dict] = []
        retries = 0

        _evt(q, "status", {"text": "thinking…"})

        for step in range(MAX_STEPS):
            messages = build_messages(question, sql_steps)
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
                _evt(q, "status", {"text": f"retrying… ({retries}/{MAX_RETRIES})"})
                continue

            retries = 0

            if action.get("type") == "sql":
                sql = action.get("query", "").strip()
                _evt(q, "sql", {"sql": sql, "reasoning": action.get("reasoning", ""), "step": step + 1})

                result = run_query(sql)

                if result["error"]:
                    _evt(q, "sql_error", {"error": result["error"], "sql": sql})
                    sql_steps.append({"sql": sql, "result_preview": "", "row_count": 0, "error": result["error"]})
                else:
                    _evt(q, "sql_result", {
                        "row_count": result["row_count"],
                        "columns": result["columns"],
                        "rows": result["rows"][:100],
                    })
                    sql_steps.append({
                        "sql": sql,
                        "result_preview": result["result_preview"],
                        "row_count": result["row_count"],
                        "error": None,
                    })

            elif action.get("type") == "answer":
                chart_spec = action.get("chart")
                if chart_spec and sql_steps:
                    # embed data from last successful SQL
                    last = next((s for s in reversed(sql_steps) if not s.get("error")), None)
                    if last and not chart_spec.get("data", {}).get("values"):
                        res = run_query(last["sql"])
                        if not res["error"]:
                            chart_spec.setdefault("data", {})["values"] = _rows_to_vega(res["rows"], 500)

                _evt(q, "answer", {"text": action.get("text", "").strip(), "chart": chart_spec})
                _evt(q, "done", {})
                return

            else:
                _evt(q, "error", {"text": f"Unknown action type: {action.get('type')}"})
                return

        _evt(q, "error", {"text": f"Reached max steps ({MAX_STEPS}) without a final answer."})

    except Exception as e:
        _evt(q, "error", {"text": f"Agent error: {e}"})
    finally:
        q.put(None)


def stream_agent(question: str) -> Generator[str, None, None]:
    q: queue.Queue = queue.Queue()
    t = threading.Thread(target=_run_agent, args=(question, q), daemon=True)
    t.start()
    while True:
        item = q.get()
        if item is None:
            break
        yield f"data: {json.dumps(item, default=str)}\n\n"
