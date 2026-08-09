import json
from .database import get_connection
from .guard import validate_sql, sanitize_sql, screen_result


def execute_sql(sql: str) -> dict:
    """
    Execute a SQL query against DuckDB.
    Returns {"rows": [...], "row_count": N, "columns": [...], "result_preview": str, "error": str|None}
    """
    sql = sanitize_sql(sql)
    valid, err = validate_sql(sql)
    if not valid:
        return {"rows": [], "row_count": 0, "columns": [], "result_preview": "", "error": err}

    try:
        con = get_connection()
        rel = con.execute(sql)
        columns = [d[0] for d in rel.description]
        rows = [dict(zip(columns, row)) for row in rel.fetchall()]

        safe, warning = screen_result(rows)
        if not safe:
            return {"rows": [], "row_count": 0, "columns": columns, "result_preview": "", "error": warning}

        # build a compact preview for the LLM (max 20 rows)
        preview_rows = rows[:20]
        if preview_rows:
            col_str = " | ".join(columns)
            row_strs = [" | ".join(str(r.get(c, "")) for c in columns) for r in preview_rows]
            preview = col_str + "\n" + "\n".join(row_strs)
            if len(rows) > 20:
                preview += f"\n... ({len(rows)} rows total)"
        else:
            preview = "(no rows)"

        return {
            "rows": rows,
            "row_count": len(rows),
            "columns": columns,
            "result_preview": preview,
            "error": None,
        }
    except Exception as e:
        return {"rows": [], "row_count": 0, "columns": [], "result_preview": "", "error": str(e)}


def rows_to_vega_values(rows: list[dict], limit: int = 500) -> list[dict]:
    """Convert rows to JSON-serialisable Vega-Lite values."""
    result = []
    for row in rows[:limit]:
        clean = {}
        for k, v in row.items():
            if hasattr(v, "isoformat"):
                clean[k] = v.isoformat()
            else:
                clean[k] = v
        result.append(clean)
    return result
