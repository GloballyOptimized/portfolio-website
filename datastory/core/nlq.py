import os
import json
import httpx
from dotenv import load_dotenv

load_dotenv()

_API_KEY = os.getenv("OPENROUTER_KEY")
_BASE_URL = "https://openrouter.ai/api/v1"
_MODEL = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"

_SYSTEM_PROMPT = """You are a SQL expert analyst for an e-commerce dataset.

Dataset: Online Retail II (UCI) — UK-based online gift/homeware store, Dec 2009 – Dec 2011.

Available DuckDB views:
- retail           : all rows with Invoice, StockCode, Description, Quantity, InvoiceDate (TIMESTAMP), Price, CustomerID, Country, is_cancellation (BOOL), line_revenue, year, month, month_name
- retail_clean     : same as retail but cancellations excluded (safe for revenue/sales analysis)
- customer_rfm     : per customer — CustomerID, Country, last_purchase, frequency (distinct orders), monetary (total £ revenue), recency_days (days since last purchase before 2011-12-10)
- monthly_revenue  : year, month, month_name, Country, orders, customers, revenue, units_sold

Rules:
- Only write SELECT queries. No INSERT/UPDATE/DELETE/DROP.
- Use retail_clean for revenue and sales analysis.
- Use retail for cancellation/return analysis.
- Filter out special StockCodes (POST, D, M, AMAZONFEE, BANK CHARGES, C2, DOT) when analysing products.
- Revenue columns are in GBP (£).
- Wrap column names with spaces in double quotes e.g. "Customer ID" (already aliased as CustomerID in views).
- Always add LIMIT 100 unless the user asks for aggregations.

Respond ONLY with a JSON object in this exact format:
{"sql": "<your SQL query here>", "explanation": "<one sentence describing what this query does>"}

Do not include markdown, code blocks, or any text outside the JSON."""


def nlq_to_sql(question: str) -> dict:
    """Convert a natural language question to SQL. Returns {"sql": ..., "explanation": ...}"""
    headers = {
        "Authorization": f"Bearer {_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": _MODEL,
        "messages": [
            {"role": "system", "content": _SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ],
        "temperature": 0.1,
        "max_tokens": 512,
    }
    with httpx.Client(timeout=30) as client:
        resp = client.post(f"{_BASE_URL}/chat/completions", headers=headers, json=payload)
        resp.raise_for_status()

    content = resp.json()["choices"][0]["message"]["content"].strip()

    # strip markdown code fences if model ignores instructions
    if content.startswith("```"):
        content = content.split("```")[1]
        if content.startswith("json"):
            content = content[4:]
        content = content.strip()

    return json.loads(content)
