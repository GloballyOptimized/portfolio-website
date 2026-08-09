import logging
import time

logger = logging.getLogger(__name__)

MAX_RESULTS_PER_QUERY = 5
_RETRY_DELAYS = [2, 5, 10]  # seconds between retries


def search_query(query: str) -> list[dict]:
    """
    Execute a single DuckDuckGo text search with retry on rate-limit errors.
    Returns list of {title, url, snippet} dicts.
    """
    from ddgs import DDGS
    for attempt, wait in enumerate([0] + _RETRY_DELAYS):
        if wait:
            time.sleep(wait)
        try:
            results = []
            with DDGS() as ddgs:
                for r in ddgs.text(query, max_results=MAX_RESULTS_PER_QUERY):
                    results.append({
                        "title":   r.get("title", ""),
                        "url":     r.get("href", ""),
                        "snippet": r.get("body", ""),
                    })
            if results or attempt > 0:
                return results
            # empty on first try — retry once in case of transient issue
        except Exception as e:
            logger.warning("[market_analyst] search attempt %d failed for %r: %s", attempt + 1, query, e)
            if attempt == len(_RETRY_DELAYS):
                break
    return []
