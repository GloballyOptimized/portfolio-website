import os
import logging
import redis

logger = logging.getLogger(__name__)

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
TTL = 30 * 24 * 3600  # 30 days

_client = None


def get_redis():
    global _client
    if _client is None:
        try:
            _client = redis.from_url(REDIS_URL, decode_responses=True, socket_connect_timeout=2)
            _client.ping()
        except Exception as e:
            logger.warning(f"[shortener] Redis unavailable: {e}")
            _client = None
    return _client


def cache_get(code: str):
    r = get_redis()
    if not r:
        return None
    try:
        url = r.get(f"s:{code}")
        if url:
            r.expire(f"s:{code}", TTL)
        return url
    except Exception:
        return None


def cache_set(code: str, url: str):
    r = get_redis()
    if not r:
        return
    try:
        r.setex(f"s:{code}", TTL, url)
    except Exception:
        pass


def cache_delete(code: str):
    r = get_redis()
    if not r:
        return
    try:
        r.delete(f"s:{code}")
    except Exception:
        pass


def redis_ok() -> bool:
    r = get_redis()
    if not r:
        return False
    try:
        r.ping()
        return True
    except Exception:
        return False
