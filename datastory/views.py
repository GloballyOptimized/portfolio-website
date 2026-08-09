import json
from django.shortcuts import render
from django.http import JsonResponse, StreamingHttpResponse
from django.views.decorators.http import require_POST, require_GET

from .core.database import get_kpis, query
from .core.schema import DATASET_INFO, VIEWS, STARTER_QUESTIONS
from .core.agent import stream_agent
from .core.sessions import new_session_id, reset_session


def dashboard(request):
    kpis = get_kpis()
    return render(request, "datastory/dashboard.html", {
        "active": "datastory",
        "kpis": kpis,
        "dataset": DATASET_INFO,
        "starter_questions": STARTER_QUESTIONS,
    })


def chat(request):
    """SSE streaming endpoint: POST question + session_id → stream of events."""
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)

    try:
        body = json.loads(request.body)
        question = body.get("question", "").strip()
        session_id = body.get("session_id") or new_session_id()
    except Exception:
        return JsonResponse({"error": "Invalid JSON body"}, status=400)

    if not question:
        return JsonResponse({"error": "question is required"}, status=400)

    response = StreamingHttpResponse(
        stream_agent(question, session_id),
        content_type="text/event-stream",
    )
    response["Cache-Control"] = "no-cache"
    response["X-Accel-Buffering"] = "no"
    response["X-Session-Id"] = session_id
    return response


@require_POST
def reset(request):
    try:
        body = json.loads(request.body)
        session_id = body.get("session_id", "")
        if session_id:
            reset_session(session_id)
        return JsonResponse({"ok": True, "new_session_id": new_session_id()})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


@require_GET
def schema(request):
    return JsonResponse({
        "dataset": DATASET_INFO,
        "views": VIEWS,
        "starter_questions": STARTER_QUESTIONS,
    })


@require_POST
def run_query(request):
    """Raw SQL execution (advanced/debug use)."""
    try:
        body = json.loads(request.body)
        sql = body.get("sql", "").strip()
        if not sql:
            return JsonResponse({"error": "sql is required"}, status=400)
        rows = query(sql)
        return JsonResponse({"rows": rows, "count": len(rows)})
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)
    except Exception as e:
        return JsonResponse({"error": f"Query failed: {e}"}, status=500)
