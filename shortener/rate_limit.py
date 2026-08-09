"""
Token bucket rate limiting per short URL code.

Windows:
  - 10  req / second  → true token bucket (Lua, atomic)
  - 100 req / minute  → fixed-window counter (Redis INCR)
  - 100 req / hour    → fixed-window counter
  - 1000 req / day    → fixed-window counter

If Redis is unavailable the check fails open (request is allowed).
"""

import time
import logging
from .redis_client import get_redis

logger = logging.getLogger(__name__)

# ── Limits ────────────────────────────────────────────────────────────
LIMIT_SECOND = 10
LIMIT_MINUTE = 50
LIMIT_HOUR   = 100
LIMIT_DAY    = 1_000

# ── Lua: atomic token bucket ──────────────────────────────────────────
# KEYS[1] = bucket key
# ARGV[1] = capacity (int)
# ARGV[2] = refill rate (tokens/second, float)
# ARGV[3] = current unix time (float, ms precision)
# Returns {0|1, remaining_floor}
_BUCKET_LUA = """
local key    = KEYS[1]
local cap    = tonumber(ARGV[1])
local rate   = tonumber(ARGV[2])
local now    = tonumber(ARGV[3])

local d      = redis.call('HMGET', key, 't', 'ts')
local tokens = tonumber(d[1]) or cap
local last   = tonumber(d[2]) or now

local elapsed = now - last
if elapsed < 0 then elapsed = 0 end
tokens = math.min(cap, tokens + elapsed * rate)

local ok = 0
if tokens >= 1.0 then
    tokens = tokens - 1.0
    ok     = 1
end

local ttl = math.ceil(cap / rate) + 2
redis.call('HMSET', key, 't', tostring(tokens), 'ts', tostring(now))
redis.call('EXPIRE', key, ttl)
return {ok, math.floor(tokens)}
"""


def check_rate_limit(code: str) -> tuple[bool, dict]:
    """
    Check all four rate-limit windows for *code*.

    Returns:
        (allowed, meta)
        meta always contains X-RateLimit-* headers.
        On denial meta also has: limit, window, retry_after.
    """
    r = get_redis()
    if not r:
        return True, {}

    now = time.time()

    try:
        # ── 1. Per-second token bucket (atomic Lua) ────────────────
        tb_res   = r.eval(_BUCKET_LUA, 1,
                          f"rl:tb:{code}",
                          LIMIT_SECOND,       # capacity
                          LIMIT_SECOND,       # rate = capacity (10 tokens/sec)
                          now)
        tb_ok    = int(tb_res[0]) == 1
        tb_rem   = int(tb_res[1])

        # ── 2. Per-minute / hour / day (fixed-window INCR) ─────────
        m_key = f"rl:m:{code}:{int(now // 60)}"
        h_key = f"rl:h:{code}:{int(now // 3600)}"
        d_key = f"rl:d:{code}:{int(now // 86400)}"

        pipe = r.pipeline(transaction=False)
        pipe.incr(m_key); pipe.expire(m_key, 70)
        pipe.incr(h_key); pipe.expire(h_key, 3_700)
        pipe.incr(d_key); pipe.expire(d_key, 90_000)
        res = pipe.execute()

        m_count = int(res[0])
        h_count = int(res[2])
        d_count = int(res[4])

        # ── Headers always included ─────────────────────────────────
        headers = {
            "X-RateLimit-Limit-Second":    str(LIMIT_SECOND),
            "X-RateLimit-Remaining-Second": str(tb_rem),
            "X-RateLimit-Limit-Minute":    str(LIMIT_MINUTE),
            "X-RateLimit-Remaining-Minute": str(max(0, LIMIT_MINUTE - m_count)),
            "X-RateLimit-Limit-Hour":      str(LIMIT_HOUR),
            "X-RateLimit-Remaining-Hour":  str(max(0, LIMIT_HOUR - h_count)),
            "X-RateLimit-Limit-Day":       str(LIMIT_DAY),
            "X-RateLimit-Remaining-Day":   str(max(0, LIMIT_DAY - d_count)),
        }

        # ── Check from smallest to largest window ───────────────────
        if not tb_ok:
            return False, {**headers,
                           "limit": LIMIT_SECOND, "window": "second",
                           "retry_after": 1}

        if m_count > LIMIT_MINUTE:
            retry = 60 - int(now % 60)
            return False, {**headers,
                           "limit": LIMIT_MINUTE, "window": "minute",
                           "retry_after": retry}

        if h_count > LIMIT_HOUR:
            retry = 3600 - int(now % 3600)
            return False, {**headers,
                           "limit": LIMIT_HOUR, "window": "hour",
                           "retry_after": retry}

        if d_count > LIMIT_DAY:
            retry = 86400 - int(now % 86400)
            return False, {**headers,
                           "limit": LIMIT_DAY, "window": "day",
                           "retry_after": retry}

        return True, headers

    except Exception as e:
        logger.warning(f"[shortener] rate limit check error: {e}")
        return True, {}
