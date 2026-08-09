DATASET_INFO = {
    "name": "Online Retail II (UCI)",
    "source": "Kaggle (CC0-1.0)",
    "rows": 1_067_371,
    "date_range": ("2009-12-01", "2011-12-09"),
    "grain": "One row per invoice line item",
    "primary_market": "United Kingdom",
    "total_customers": 5942,
    "total_products": 5305,
    "total_countries": 43,
}

VIEWS = {
    "retail": "All rows with derived columns (is_cancellation, line_revenue, year, month)",
    "retail_clean": "Sales only — cancellations, returns, bad prices excluded",
    "customer_rfm": "Per-customer: recency_days, frequency (orders), monetary (£ revenue)",
    "monthly_revenue": "Monthly × country: orders, customers, revenue, units_sold",
}

STARTER_QUESTIONS = [
    "Monthly revenue trend for 2011",
    "Top 10 products by revenue",
    "RFM distribution of customers",
    "UK vs rest of world revenue split",
    "Cancellation rate over time",
    "Top 5 countries by number of orders",
    "Highest revenue month overall",
    "Repeat vs one-time customer split",
]

SPECIAL_STOCK_CODES = ["POST", "D", "M", "AMAZONFEE", "BANK CHARGES", "C2", "DOT"]
