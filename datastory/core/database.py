import duckdb
import pathlib
from django.conf import settings

PARQUET_PATH = pathlib.Path(settings.BASE_DIR) / "data" / "online_retail" / "online_retail_II.parquet"

_FORBIDDEN = {"attach", "install", "copy", "import_database", "export_database", "load"}


def _guard(sql: str):
    first = sql.strip().split()[0].lower()
    if first not in {"select", "with", "describe", "show"}:
        raise ValueError(f"Only SELECT/WITH/DESCRIBE allowed, got: {first!r}")
    for kw in _FORBIDDEN:
        if kw in sql.lower():
            raise ValueError(f"Forbidden keyword: {kw!r}")


def get_connection() -> duckdb.DuckDBPyConnection:
    con = duckdb.connect(database=":memory:", read_only=False)
    con.execute(f"""
        CREATE VIEW retail AS
        SELECT
            Invoice,
            StockCode,
            Description,
            Quantity,
            TRY_CAST(InvoiceDate AS TIMESTAMP) AS InvoiceDate,
            Price,
            "Customer ID"                            AS CustomerID,
            Country,
            Invoice LIKE 'C%'                        AS is_cancellation,
            Quantity * Price                         AS line_revenue,
            YEAR(TRY_CAST(InvoiceDate AS TIMESTAMP)) AS year,
            MONTH(TRY_CAST(InvoiceDate AS TIMESTAMP)) AS month,
            MONTHNAME(TRY_CAST(InvoiceDate AS TIMESTAMP)) AS month_name
        FROM read_parquet('{PARQUET_PATH.as_posix()}')
        WHERE Price >= 0 AND Quantity > 0
    """)
    con.execute("CREATE VIEW retail_clean AS SELECT * FROM retail WHERE NOT is_cancellation")
    con.execute("""
        CREATE VIEW customer_rfm AS
        SELECT
            CustomerID, Country,
            MAX(InvoiceDate)                                        AS last_purchase,
            COUNT(DISTINCT Invoice)                                 AS frequency,
            SUM(line_revenue)                                       AS monetary,
            DATEDIFF('day', MAX(InvoiceDate), TIMESTAMP '2011-12-10') AS recency_days
        FROM retail_clean
        WHERE CustomerID IS NOT NULL
        GROUP BY CustomerID, Country
    """)
    con.execute("""
        CREATE VIEW monthly_revenue AS
        SELECT
            year, month, month_name, Country,
            COUNT(DISTINCT Invoice)    AS orders,
            COUNT(DISTINCT CustomerID) AS customers,
            SUM(line_revenue)          AS revenue,
            SUM(Quantity)              AS units_sold
        FROM retail_clean
        GROUP BY year, month, month_name, Country
    """)
    return con


def query(sql: str) -> list[dict]:
    _guard(sql)
    con = get_connection()
    rel = con.execute(sql)
    cols = [d[0] for d in rel.description]
    return [dict(zip(cols, row)) for row in rel.fetchall()]


def get_kpis() -> dict:
    con = get_connection()
    row = con.execute("""
        SELECT
            ROUND(SUM(line_revenue), 2)          AS total_revenue,
            COUNT(DISTINCT Invoice)               AS total_orders,
            COUNT(DISTINCT CustomerID)            AS total_customers,
            ROUND(SUM(line_revenue) / COUNT(DISTINCT Invoice), 2) AS avg_order_value
        FROM retail_clean
    """).fetchone()
    return {
        "total_revenue": f"£{row[0]:,.0f}",
        "total_orders": f"{row[1]:,}",
        "total_customers": f"{row[2]:,}",
        "avg_order_value": f"£{row[3]:,.2f}",
    }
