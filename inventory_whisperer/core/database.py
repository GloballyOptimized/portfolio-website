import pathlib
import duckdb
from django.conf import settings

_PARQUET = str(pathlib.Path(settings.BASE_DIR) / "data" / "online_retail" / "online_retail_II.parquet")

# StockCodes that are fees/adjustments, not real products
_JUNK_CODES = "('POST','D','M','AMAZONFEE','BANK CHARGES','C2','DOT','PADS','ADJUST','ADJUST2')"

# Dataset ends 2011-12-09; we treat last 60 days as "recent" for demand signals
_RECENT_START  = "TIMESTAMP '2011-10-10'"
_PRIOR_START   = "TIMESTAMP '2011-08-11'"
_PRIOR_END     = "TIMESTAMP '2011-10-09'"


def get_connection() -> duckdb.DuckDBPyConnection:
    con = duckdb.connect(database=":memory:", read_only=False)
    p = _PARQUET.replace("\\", "/")

    con.execute(f"""
        CREATE VIEW sku_catalog AS
        SELECT
            StockCode,
            ANY_VALUE(Description)                           AS description,
            ROUND(AVG(Price), 2)                             AS avg_price,
            SUM(Quantity)                                    AS total_units_sold,
            ROUND(SUM(Quantity * Price), 2)                  AS total_revenue,
            COUNT(DISTINCT Invoice)                          AS total_orders,
            COUNT(DISTINCT TRY_CAST("Customer ID" AS INT))   AS unique_buyers,
            MIN(TRY_CAST(InvoiceDate AS TIMESTAMP))          AS first_sold,
            MAX(TRY_CAST(InvoiceDate AS TIMESTAMP))          AS last_sold
        FROM read_parquet('{p}')
        WHERE Price > 0
          AND Quantity > 0
          AND StockCode IS NOT NULL
          AND StockCode NOT IN {_JUNK_CODES}
        GROUP BY StockCode
    """)

    con.execute(f"""
        CREATE VIEW monthly_demand AS
        SELECT
            StockCode,
            YEAR(TRY_CAST(InvoiceDate AS TIMESTAMP))  AS yr,
            MONTH(TRY_CAST(InvoiceDate AS TIMESTAMP)) AS mo,
            SUM(Quantity)                             AS units_sold,
            ROUND(SUM(Quantity * Price), 2)           AS revenue,
            COUNT(DISTINCT Invoice)                   AS orders
        FROM read_parquet('{p}')
        WHERE Price > 0
          AND Quantity > 0
          AND StockCode NOT IN {_JUNK_CODES}
        GROUP BY StockCode, yr, mo
    """)

    con.execute(f"""
        CREATE VIEW abc_analysis AS
        WITH sku_rev AS (
            SELECT StockCode, ROUND(SUM(Quantity * Price), 2) AS revenue
            FROM read_parquet('{p}')
            WHERE Price > 0 AND Quantity > 0
              AND StockCode NOT IN {_JUNK_CODES}
            GROUP BY StockCode
        ),
        ranked AS (
            SELECT StockCode, revenue,
                   SUM(revenue) OVER (ORDER BY revenue DESC
                                      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_rev,
                   SUM(revenue) OVER ()                                                  AS total_rev
            FROM sku_rev
        )
        SELECT
            StockCode,
            revenue,
            ROUND(cum_rev / total_rev * 100, 2) AS cumulative_pct,
            CASE
                WHEN cum_rev / total_rev <= 0.80 THEN 'A'
                WHEN cum_rev / total_rev <= 0.95 THEN 'B'
                ELSE 'C'
            END AS abc_class
        FROM ranked
    """)

    con.execute(f"""
        CREATE VIEW demand_signals AS
        WITH recent AS (
            SELECT StockCode, SUM(Quantity) AS recent_units
            FROM read_parquet('{p}')
            WHERE Price > 0 AND Quantity > 0
              AND StockCode NOT IN {_JUNK_CODES}
              AND TRY_CAST(InvoiceDate AS TIMESTAMP) >= {_RECENT_START}
            GROUP BY StockCode
        ),
        prior AS (
            SELECT StockCode, SUM(Quantity) AS prior_units
            FROM read_parquet('{p}')
            WHERE Price > 0 AND Quantity > 0
              AND StockCode NOT IN {_JUNK_CODES}
              AND TRY_CAST(InvoiceDate AS TIMESTAMP) BETWEEN {_PRIOR_START} AND {_PRIOR_END}
            GROUP BY StockCode
        )
        SELECT
            r.StockCode,
            r.recent_units,
            COALESCE(p.prior_units, 0)                          AS prior_units,
            CASE
                WHEN r.recent_units > COALESCE(p.prior_units, 0) * 1.25 THEN 'rising'
                WHEN r.recent_units < COALESCE(p.prior_units, 0) * 0.75 THEN 'falling'
                ELSE 'stable'
            END                                                  AS trend,
            CASE
                WHEN r.recent_units >= 100 THEN 'high_velocity'
                WHEN r.recent_units <= 5
                     AND COALESCE(p.prior_units, 0) >= 30       THEN 'slow_mover'
                ELSE 'normal'
            END                                                  AS signal
        FROM recent r
        LEFT JOIN prior p ON r.StockCode = p.StockCode
    """)

    return con


def query(sql: str) -> dict:
    sql = sql.strip()
    first_word = sql.split()[0].lower() if sql.split() else ""
    if first_word not in {"select", "with", "describe", "show"}:
        return {"error": f"Only SELECT/WITH queries allowed, got: {first_word!r}",
                "rows": [], "columns": [], "row_count": 0, "result_preview": ""}
    forbidden = {"insert", "update", "delete", "drop", "attach", "install", "copy"}
    if any(kw in sql.lower() for kw in forbidden):
        return {"error": "Forbidden keyword in query.",
                "rows": [], "columns": [], "row_count": 0, "result_preview": ""}
    try:
        con = get_connection()
        rel = con.execute(sql)
        cols = [d[0] for d in rel.description]
        rows = [dict(zip(cols, row)) for row in rel.fetchall()]
        preview_lines = [" | ".join(cols)]
        for r in rows[:20]:
            preview_lines.append(" | ".join(str(r.get(c, "")) for c in cols))
        if len(rows) > 20:
            preview_lines.append(f"... ({len(rows)} rows total)")
        return {
            "rows": rows, "columns": cols,
            "row_count": len(rows),
            "result_preview": "\n".join(preview_lines),
            "error": None,
        }
    except Exception as e:
        return {"error": str(e), "rows": [], "columns": [], "row_count": 0, "result_preview": ""}


def get_watchlist() -> dict:
    """Returns reorder candidates and slow-movers for dashboard."""
    con = get_connection()
    reorder = con.execute("""
        SELECT d.StockCode, s.description, d.recent_units, d.prior_units, d.trend, d.signal,
               s.avg_price,
               ROUND(d.recent_units * s.avg_price, 0) AS recent_revenue
        FROM demand_signals d
        JOIN sku_catalog s ON d.StockCode = s.StockCode
        JOIN abc_analysis a ON d.StockCode = a.StockCode
        WHERE d.signal = 'high_velocity'
          AND a.abc_class IN ('A', 'B')
        ORDER BY d.recent_units DESC
        LIMIT 15
    """).fetchall()
    reorder_cols = ["stock_code","description","recent_units","prior_units","trend","signal","avg_price","recent_revenue"]

    slow = con.execute("""
        SELECT d.StockCode, s.description, d.recent_units, d.prior_units, d.trend,
               s.last_sold, s.total_units_sold
        FROM demand_signals d
        JOIN sku_catalog s ON d.StockCode = s.StockCode
        JOIN abc_analysis a ON d.StockCode = a.StockCode
        WHERE d.signal = 'slow_mover'
          AND a.abc_class IN ('A', 'B')
        ORDER BY d.prior_units DESC
        LIMIT 10
    """).fetchall()
    slow_cols = ["stock_code","description","recent_units","prior_units","trend","last_sold","total_units_sold"]

    return {
        "reorder": [dict(zip(reorder_cols, r)) for r in reorder],
        "slow_movers": [dict(zip(slow_cols, r)) for r in slow],
    }


def get_projection_data() -> list[dict]:
    """
    Monthly demand for top 5 A-class SKUs for all of 2011,
    plus a 3-month linear projection into 2012.
    """
    con = get_connection()
    top_skus = con.execute("""
        SELECT a.StockCode, s.description
        FROM abc_analysis a
        JOIN sku_catalog s ON a.StockCode = s.StockCode
        WHERE a.abc_class = 'A'
        ORDER BY a.revenue DESC
        LIMIT 5
    """).fetchall()

    rows = []
    for stock_code, desc in top_skus:
        label = (desc or stock_code)[:22]
        monthly = con.execute("""
            SELECT yr, mo, units_sold
            FROM monthly_demand
            WHERE StockCode = ?
              AND yr = 2011
            ORDER BY yr, mo
        """, [stock_code]).fetchall()

        if not monthly:
            continue

        for yr, mo, units in monthly:
            rows.append({
                "product": label,
                "month":   f"{yr}-{mo:02d}",
                "units":   units,
                "type":    "actual",
            })

        # linear projection: Jan–Mar 2012
        vals = [r[2] for r in monthly]
        n    = len(vals)
        avg  = sum(vals) / n
        denom = sum((i - n / 2) ** 2 for i in range(n)) or 1
        slope = sum((i - n / 2) * (v - avg) for i, v in enumerate(vals)) / denom
        last_val = vals[-1]
        for offset in range(1, 4):
            rows.append({
                "product": label,
                "month":   f"2012-{offset:02d}",
                "units":   max(0, round(last_val + slope * offset)),
                "type":    "projected",
            })

    return rows


def get_kpis() -> dict:
    con = get_connection()
    row = con.execute("""
        SELECT
            COUNT(*)                              AS total_skus,
            ROUND(SUM(total_revenue), 0)          AS total_revenue,
            SUM(total_orders)                     AS total_orders,
            COUNT(*) FILTER (
                WHERE last_sold >= TIMESTAMP '2011-10-10'
            )                                     AS active_skus
        FROM sku_catalog
    """).fetchone()
    abc = con.execute("""
        SELECT abc_class, COUNT(*) AS cnt
        FROM abc_analysis
        GROUP BY abc_class ORDER BY abc_class
    """).fetchall()
    abc_map = {r[0]: r[1] for r in abc}
    return {
        "total_skus":   f"{row[0]:,}",
        "total_revenue": f"£{row[1]:,.0f}",
        "total_orders":  f"{row[2]:,}",
        "active_skus":   f"{row[3]:,}",
        "a_class_skus":  f"{abc_map.get('A', 0):,}",
    }
