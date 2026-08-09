import uuid
import duckdb
import logging
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

logger = logging.getLogger(__name__)

_DB_PATH = None
_conn = None


def _get_path() -> str:
    global _DB_PATH
    if _DB_PATH is None:
        path = getattr(settings, "MARKET_ANALYST_DUCKDB", "").strip()
        if not path:
            raise ImproperlyConfigured(
                "settings.MARKET_ANALYST_DUCKDB is required. "
                "Set MARKET_ANALYST_DUCKDB in your .env to a writable .duckdb file path."
            )
        _DB_PATH = path
    return _DB_PATH


def get_conn() -> duckdb.DuckDBPyConnection:
    global _conn
    if _conn is None:
        _conn = duckdb.connect(_get_path())
    return _conn


def init_db():
    """Create tables if they don't exist."""
    try:
        conn = get_conn()
        conn.execute("""
            CREATE TABLE IF NOT EXISTS research_sessions (
                id          VARCHAR PRIMARY KEY,
                question    TEXT NOT NULL,
                query_count INTEGER DEFAULT 0,
                result_count INTEGER DEFAULT 0,
                analysis    TEXT,
                confidence  VARCHAR,
                created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS search_queries (
                id          VARCHAR PRIMARY KEY,
                session_id  VARCHAR NOT NULL,
                query       TEXT NOT NULL,
                rank        INTEGER
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS search_results (
                id              VARCHAR PRIMARY KEY,
                session_id      VARCHAR NOT NULL,
                query_id        VARCHAR NOT NULL,
                title           TEXT,
                url             TEXT,
                snippet         TEXT,
                rank_in_query   INTEGER
            )
        """)
        logger.info("[market_analyst] DuckDB initialised at %s", _get_path())
    except ImproperlyConfigured:
        raise
    except Exception as e:
        logger.error("[market_analyst] DB init failed: %s", e)
        raise


def save_session(session_id: str, question: str, queries: list[str],
                 results_map: dict, analysis: str, confidence: str) -> None:
    conn = get_conn()
    total_results = sum(len(v) for v in results_map.values())
    conn.execute("""
        INSERT OR REPLACE INTO research_sessions
            (id, question, query_count, result_count, analysis, confidence)
        VALUES (?, ?, ?, ?, ?, ?)
    """, [session_id, question, len(queries), total_results, analysis, confidence])

    for rank, query in enumerate(queries):
        qid = str(uuid.uuid4())
        conn.execute("""
            INSERT INTO search_queries (id, session_id, query, rank)
            VALUES (?, ?, ?, ?)
        """, [qid, session_id, query, rank])

        for r_rank, result in enumerate(results_map.get(query, [])):
            conn.execute("""
                INSERT INTO search_results
                    (id, session_id, query_id, title, url, snippet, rank_in_query)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, [str(uuid.uuid4()), session_id, qid,
                  result.get("title"), result.get("url"),
                  result.get("snippet"), r_rank])


def get_recent_sessions(limit: int = 10) -> list[dict]:
    conn = get_conn()
    rows = conn.execute("""
        SELECT id, question, query_count, result_count, confidence, created_at
        FROM research_sessions
        ORDER BY created_at DESC
        LIMIT ?
    """, [limit]).fetchall()
    cols = ["id", "question", "query_count", "result_count", "confidence", "created_at"]
    return [dict(zip(cols, r)) for r in rows]


def get_session(session_id: str) -> dict | None:
    conn = get_conn()
    row = conn.execute("""
        SELECT id, question, query_count, result_count, analysis, confidence, created_at
        FROM research_sessions WHERE id = ?
    """, [session_id]).fetchone()
    if not row:
        return None
    cols = ["id", "question", "query_count", "result_count", "analysis", "confidence", "created_at"]
    session = dict(zip(cols, row))
    queries = conn.execute("""
        SELECT id, query, rank FROM search_queries
        WHERE session_id = ? ORDER BY rank
    """, [session_id]).fetchall()
    session["queries"] = [{"id": q[0], "query": q[1], "rank": q[2]} for q in queries]
    return session
