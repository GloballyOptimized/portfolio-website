import json
import uuid
import pathlib
from datetime import datetime, timezone

SESSIONS_DIR = pathlib.Path(__file__).resolve().parents[2] / "datastory" / "data" / "sessions"
SESSIONS_DIR.mkdir(parents=True, exist_ok=True)

MAX_HISTORY_TURNS = 20  # keep last N user/assistant turns


def new_session_id() -> str:
    return str(uuid.uuid4())[:8]


def session_path(session_id: str) -> pathlib.Path:
    return SESSIONS_DIR / f"{session_id}.json"


def load_session(session_id: str) -> dict:
    path = session_path(session_id)
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {
        "session_id": session_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "history": [],  # list of {"role": "user"|"assistant", "content": str}
    }


def save_session(session_id: str, session: dict) -> None:
    session["updated_at"] = datetime.now(timezone.utc).isoformat()
    # trim to last MAX_HISTORY_TURNS turns (each turn = 1 user + 1 assistant)
    history = session.get("history", [])
    if len(history) > MAX_HISTORY_TURNS * 2:
        session["history"] = history[-(MAX_HISTORY_TURNS * 2):]
    session_path(session_id).write_text(
        json.dumps(session, ensure_ascii=False, default=str), encoding="utf-8"
    )


def append_turn(session: dict, user_msg: str, assistant_msg: str) -> None:
    session.setdefault("history", [])
    session["history"].append({"role": "user", "content": user_msg})
    session["history"].append({"role": "assistant", "content": assistant_msg})


def reset_session(session_id: str) -> None:
    path = session_path(session_id)
    if path.exists():
        path.unlink()
