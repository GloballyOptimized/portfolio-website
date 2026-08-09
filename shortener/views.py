import secrets
import string
import json
import threading
import logging

from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST, require_GET
from django.db.models import Sum

from .models import ShortURL
from .redis_client import cache_get, cache_set, redis_ok
from .rate_limit import check_rate_limit

logger = logging.getLogger(__name__)

ALPHABET = string.ascii_letters + string.digits
CODE_LEN = 7


def _gen_code() -> str:
    return "".join(secrets.choice(ALPHABET) for _ in range(CODE_LEN))


def _make_code() -> str:
    for _ in range(10):
        code = _gen_code()
        if not ShortURL.objects.filter(code=code).exists():
            return code
    raise RuntimeError("Could not generate a unique code")


def _base_url(request) -> str:
    return f"{request.scheme}://{request.get_host()}"


def index(request):
    agg = ShortURL.objects.aggregate(total=Sum("access_count"))
    stats = {
        "total_urls": ShortURL.objects.count(),
        "total_hits": agg["total"] or 0,
        "redis_ok": redis_ok(),
    }
    return render(request, "shortener/index.html", {
        "active": "shortener",
        "stats": stats,
        "base_url": _base_url(request),
    })


@require_POST
def shorten(request):
    try:
        body = json.loads(request.body)
        url = body.get("url", "").strip()
    except Exception:
        return JsonResponse({"error": "invalid request body"}, status=400)

    if not url:
        return JsonResponse({"error": "url is required"}, status=400)

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        URLValidator()(url)
    except ValidationError:
        return JsonResponse({"error": "invalid URL"}, status=400)

    existing = ShortURL.objects.filter(original_url=url).first()
    if existing:
        return JsonResponse({
            "code": existing.code,
            "short_url": f"{_base_url(request)}/anotherurlshortner/{existing.code}",
            "original_url": url,
            "access_count": existing.access_count,
            "existed": True,
        })

    code = _make_code()
    ShortURL.objects.create(code=code, original_url=url)
    cache_set(code, url)

    return JsonResponse({
        "code": code,
        "short_url": f"{_base_url(request)}/anotherurlshortner/{code}",
        "original_url": url,
        "access_count": 0,
        "existed": False,
    }, status=201)


def redirect_url(request, code):
    # ── Rate limit check (per URL, all four windows) ──────────────
    allowed, rl_meta = check_rate_limit(code)
    if not allowed:
        window      = rl_meta.get("window", "unknown")
        limit       = rl_meta.get("limit", "?")
        retry_after = rl_meta.get("retry_after", 1)
        resp = HttpResponse(
            f"429 Too Many Requests — limit: {limit} requests/{window}. "
            f"Retry after {retry_after}s.",
            status=429,
            content_type="text/plain",
        )
        resp["Retry-After"] = str(retry_after)
        for k, v in rl_meta.items():
            if k.startswith("X-RateLimit"):
                resp[k] = v
        return resp

    # ── Cache / DB lookup ─────────────────────────────────────────
    url = cache_get(code)
    if url is None:
        try:
            obj = ShortURL.objects.get(code=code)
        except ShortURL.DoesNotExist:
            raise Http404("Short URL not found")
        url = obj.original_url
        cache_set(code, url)
        obj.record_access()
    else:
        def _update():
            try:
                ShortURL.objects.get(code=code).record_access()
            except ShortURL.DoesNotExist:
                pass
        threading.Thread(target=_update, daemon=True).start()

    resp = HttpResponseRedirect(url)
    for k, v in rl_meta.items():
        if k.startswith("X-RateLimit"):
            resp[k] = v
    return resp


@require_GET
def stats_view(request, code):
    try:
        obj = ShortURL.objects.get(code=code)
    except ShortURL.DoesNotExist:
        return JsonResponse({"error": "not found"}, status=404)
    return JsonResponse({
        "code": obj.code,
        "original_url": obj.original_url,
        "access_count": obj.access_count,
        "created_at": obj.created_at.isoformat(),
        "last_accessed": obj.last_accessed.isoformat() if obj.last_accessed else None,
        "cached": cache_get(obj.code) is not None,
    })


@require_GET
def api_info(request):
    agg = ShortURL.objects.aggregate(total=Sum("access_count"))
    return JsonResponse({
        "total_urls": ShortURL.objects.count(),
        "total_hits": agg["total"] or 0,
        "redis_ok": redis_ok(),
    })
