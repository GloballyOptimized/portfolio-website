import json
from django.shortcuts import render
from django.http import JsonResponse, StreamingHttpResponse

from .core.agent import stream_research
from .core.database import get_recent_sessions, get_session


def dashboard(request):
    try:
        recent = get_recent_sessions(10)
    except Exception:
        recent = []
    return render(request, "market_analyst/dashboard.html", {
        "active": "market_analyst",
        "recent": recent,
    })


def research(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)
    try:
        body = json.loads(request.body)
        question = body.get("question", "").strip()
    except Exception:
        return JsonResponse({"error": "invalid request body"}, status=400)
    if not question:
        return JsonResponse({"error": "question is required"}, status=400)

    response = StreamingHttpResponse(
        stream_research(question),
        content_type="text/event-stream",
    )
    response["Cache-Control"] = "no-cache"
    response["X-Accel-Buffering"] = "no"
    return response


def session_detail(request, session_id):
    s = get_session(session_id)
    if not s:
        return JsonResponse({"error": "not found"}, status=404)
    return JsonResponse(s, default=str)
