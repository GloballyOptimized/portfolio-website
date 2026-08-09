# Domain knowledge for Online Retail II (UCI) — Dec 2009 to Dec 2011
# UK-based non-store online retailer selling gift/homeware items wholesale & retail

DATASET_INFO = {
    "name": "Online Retail II (UCI)",
    "source": "UCI Machine Learning Repository via Kaggle",
    "license": "CC0-1.0",
    "rows": 1_067_371,
    "date_range": ("2009-12-01", "2011-12-09"),
    "grain": "One row per invoice line item",
    "primary_market": "United Kingdom (92% of orders)",
    "total_customers": 5942,
    "total_products": 5305,
    "total_countries": 43,
}

VIEWS = {
    "retail": "All rows with derived columns (includes cancellations filtered by price>=0 & qty>0)",
    "retail_clean": "retail WHERE NOT is_cancellation — use for revenue/sales analysis",
    "customer_rfm": "Per-customer RFM: recency_days, frequency (orders), monetary (revenue), last_purchase",
    "monthly_revenue": "Monthly aggregates by country: orders, customers, revenue, units_sold",
}

COLUMNS = {
    "Invoice": "Invoice number. Prefix 'C' means cancellation.",
    "StockCode": "Product code. Special codes: POST=postage, D=discount, M=manual, AMAZONFEE=Amazon fee.",
    "Description": "Product name. May be null (~4k rows).",
    "Quantity": "Units sold. Negative = return/cancellation.",
    "InvoiceDate": "Timestamp of transaction (UTC).",
    "Price": "Unit price in GBP. Negative values exist (adjustments).",
    "CustomerID": "Unique customer ID. Null = guest checkout (~243k rows).",
    "Country": "Customer's country.",
    # derived
    "is_cancellation": "True when Invoice starts with 'C'.",
    "line_revenue": "Quantity * Price — revenue for the line item.",
    "year": "Year extracted from InvoiceDate.",
    "month": "Month number extracted from InvoiceDate.",
    "month_name": "Month name extracted from InvoiceDate.",
    "recency_days": "(customer_rfm) Days since last purchase relative to 2011-12-10.",
    "frequency": "(customer_rfm) Number of distinct invoices.",
    "monetary": "(customer_rfm) Total revenue from customer.",
}

TOP_COUNTRIES = [
    "United Kingdom", "EIRE", "Germany", "France",
    "Netherlands", "Spain", "Belgium", "Switzerland",
    "Portugal", "Australia",
]

SPECIAL_STOCK_CODES = {
    "POST": "Postage charges",
    "D": "Discount",
    "M": "Manual entry / adjustment",
    "AMAZONFEE": "Amazon marketplace fee",
    "BANK CHARGES": "Bank charges",
    "C2": "Carriage charge",
    "DOT": "Dotcom postage",
}

KPI_QUERIES = {
    "total_revenue": "SELECT ROUND(SUM(line_revenue), 2) AS total_revenue FROM retail_clean",
    "total_orders": "SELECT COUNT(DISTINCT Invoice) AS total_orders FROM retail_clean",
    "total_customers": "SELECT COUNT(DISTINCT CustomerID) AS total_customers FROM retail_clean WHERE CustomerID IS NOT NULL",
    "cancellation_rate": """
        SELECT ROUND(100.0 * SUM(is_cancellation::INT) / COUNT(*), 2) AS cancellation_rate_pct
        FROM retail
    """,
    "avg_order_value": """
        SELECT ROUND(SUM(line_revenue) / COUNT(DISTINCT Invoice), 2) AS avg_order_value
        FROM retail_clean
    """,
    "top_country_by_revenue": """
        SELECT Country, ROUND(SUM(line_revenue), 2) AS revenue
        FROM retail_clean GROUP BY Country ORDER BY revenue DESC LIMIT 1
    """,
}

STARTER_QUESTIONS = [
    "What is the monthly revenue trend for 2011?",
    "Which 10 products generate the most revenue?",
    "What is the customer RFM distribution?",
    "How does UK revenue compare to the rest of the world?",
    "What is the repeat purchase rate?",
    "Which month had the highest number of unique customers?",
    "What are the top 5 countries by number of orders?",
    "Show the cancellation rate over time.",
]
