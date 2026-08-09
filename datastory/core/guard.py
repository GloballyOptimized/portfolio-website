import re

_FORBIDDEN_KEYWORDS = {
    "insert", "update", "delete", "drop", "truncate", "create", "alter",
    "attach", "install", "copy", "import_database", "export_database",
    "load", "pragma", "call",
}

_ALLOWED_STARTS = {"select", "with", "describe", "show", "explain"}


def validate_sql(sql: str) -> tuple[bool, str]:
    """Returns (is_valid, error_message). Empty error means valid."""
    if not sql or not sql.strip():
        return False, "Empty SQL"

    cleaned = sql.strip().lower()
    first_word = cleaned.split()[0]

    if first_word not in _ALLOWED_STARTS:
        return False, f"Only SELECT/WITH queries are allowed. Got: {first_word!r}"

    for kw in _FORBIDDEN_KEYWORDS:
        pattern = r'\b' + re.escape(kw) + r'\b'
        if re.search(pattern, cleaned):
            return False, f"Forbidden keyword detected: {kw!r}"

    return True, ""


def screen_result(rows: list[dict]) -> tuple[bool, str]:
    """Basic result screening. Returns (is_safe, warning)."""
    if len(rows) > 10_000:
        return False, f"Result too large: {len(rows)} rows. Add LIMIT."
    return True, ""


def sanitize_sql(sql: str) -> str:
    """Remove trailing semicolons and strip whitespace."""
    return sql.strip().rstrip(";").strip()
