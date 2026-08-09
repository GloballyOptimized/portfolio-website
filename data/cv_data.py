PROFILE = {
    "name": "ayush suryawanshi",
    "tagline": "builds things. senior software engineer. ai infrastructure.",
    "email": "suryawanshiayush007@gmail.com",
    "phone": "+91-7000580565",
    "linkedin": "https://www.linkedin.com/in/ayush-suryawanshi-4b7290206/",
    "github": "https://github.com/GloballyOptimized",
    "x": "https://x.com/globlyoptimized",
    "location": "Bengaluru, India",
    "current_role": "Senior Software Engineer at Innoviti Technologies",
    "current_focus": "AI inference infrastructure, NLQ-to-SQL engines, and fraud detection systems.",
}

SKILLS = {
    "Languages": ["Python", "Go", "JavaScript", "SQL"],
    "Frameworks": ["FastAPI", "Django", "Flask", "Angular", "Celery", "LangGraph", "MCP", "Pydantic", "Selenium"],
    "Databases": ["PostgreSQL", "Redis", "MongoDB", "MySQL", "SQLite", "ChromaDB", "Milvus", "RabbitMQ"],
    "Cloud": ["AWS EC2", "RDS", "S3", "Lambda", "Bedrock"],
    "DevOps": ["Docker", "Kubernetes", "Linux", "Nginx", "Gunicorn", "Prometheus", "Grafana"],
    "Data & Protocols": ["Pandas", "WebSockets", "SSE"],
    "ML / AI": ["vLLM", "LightGBM", "YOLOv9", "OpenCV", "CUDA"],
    "Patterns": ["Event-Driven Architecture", "RAG", "Multi-Agent Systems", "LLM Orchestration", "Async Task Queues", "ETL Pipelines"],
    "LLMs (Production)": ["Claude Sonnet 4.6", "Claude Opus 4.7", "Qwen 3.6", "Gemini 1.5 Flash", "Gemma 3"],
    "LLMs (General Use)": ["Kimi K2", "MiniMax", "GLM 4.7", "Fable 5", "GPT-4o mini"],
    "Tools": ["Git", "VS Code", "Claude Code", "Postman", "Pytest"],
}

EXPERIENCE = [
    {
        "title": "Senior Software Engineer",
        "company": "Innoviti Technologies",
        "location": "Bengaluru",
        "start": "September 2024",
        "end": "Present",
        "bullets": [
            "Designed Sanchez — an internal production control platform on Django housing 8 isolated apps with Google OAuth, RBAC, and per-app data isolation; built an LLM-powered log monitoring pipeline with Slack alerting, per-app logical behaviour analytics, and a unified control plane — consolidating all scattered production tooling into a single governed environment.",
            "Built the AI inference stack from scratch — vLLM on 96 GB VRAM with tensor parallelism, 8-bit AWQ quantization, and continuous batching behind an async FastAPI gateway; achieved 128K context window locally, 50+ concurrent requests at 3,000+ tokens/sec, sub-3s p99 latency.",
            "Built Hermione — a natural language analytics engine on Django + Qwen3-VL 27B (8-bit) on AWS EC2; schema-aware SQL generation with an auto-visualization layer producing charts, graphs, and maps from PostgreSQL — handling 1,600+ queries/day at 92% accuracy.",
            "Built Holmes AI — an async image QC pipeline on FastAPI + RabbitMQ processing 5,000+ support ticket images daily; S3 artifact pull, preprocessing and compression, YOLOv9 checkbox detection, Qwen3-VL 32B semantic validation — reducing processing time from 1,260s to 7s (180×).",
            "Built Link — a fraud detection system for a 21,000+ merchant network; RabbitMQ event ingestion, feature engineering on transaction history and velocity, LightGBM classifier with tuned decision boundaries, low-latency scoring API at 100,000+ transactions/day — reducing LEA complaints by 78%.",
            "Redesigned field engineer dispatch across 20,000+ stores and 120 engineers — weighted bipartite matching with KPI-based priority scoring (SLA, skill, zone), Haversine geo-proximity via OpenStreetMap, priority queues on PostgreSQL with spatial indexing — reducing backlog by 37%.",
        ],
        "tags": ["FastAPI", "Python", "vLLM", "LightGBM", "AWS", "PostgreSQL", "Celery", "YOLOv9", "Django", "Sanchez"],
    },
    {
        "title": "Software Development Engineer",
        "company": "Pheonix Solutions",
        "location": "Bengaluru",
        "start": "July 2022",
        "end": "September 2024",
        "bullets": [
            "Built Disha-AI — a two-stage address normalization pipeline on FastAPI; Google Maps API for geocoding, Gemini 1.5 Flash for semantic correction, Redis-backed deduplication and rate limiting — 94%+ accuracy across 20,000+ records, $28,000 cost reduction.",
            "Built a high-throughput inventory system on Django REST + PostgreSQL — optimistic locking for concurrent mutations, write-through Redis caching with TTL invalidation, connection pooling — sustained 12K req/s across 50K+ stock units.",
            "Built a compliance portal on Django + Celery — EasyOCR license extraction, pHash duplicate detection, automated MVR checks with audit trails — reduced review time by 30%.",
            "Built a social profile intelligence crawler — distributed Selenium with rate-limit-aware scheduling and session rotation, Mistral 7B for structured extraction — 1,500+ profiles/day at 92%+ accuracy with zero manual tagging.",
        ],
        "tags": ["FastAPI", "Django", "Redis", "PostgreSQL", "Selenium", "Mistral 7B", "Gemini"],
    },
    {
        "title": "Intern",
        "company": "KPMG India",
        "location": "Ahmedabad",
        "start": "January 2022",
        "end": "June 2022",
        "bullets": [
            "Automated the client license audit pipeline — FastAPI bulk upload layer, PyPDF + EasyOCR extraction, Python normalization into SQLite — cutting processing time by 90% and eliminating manual document review.",
            "Unified $7M of fragmented license data from MySQL, Excel, and OCR sources into a single SQLite store via ETL; connected to a Power BI dashboard with utilization gap detection and cost optimization insights for KPMG stakeholders.",
        ],
        "tags": ["Python", "EasyOCR", "SQLite", "Pandas", "Power BI"],
    },
]

PROJECTS = [
    {
        "name": "AI Analyst",
        "short_desc": "NLQ-to-SQL engine handling 1,600+ queries/day at 92% accuracy.",
        "desc": "Context-aware natural language to SQL engine deployed on AWS EC2. Powered by Claude 3.7 Sonnet with integration to internal PostgreSQL servers. Handles 1,600+ queries/day at 92% accuracy.",
        "tags": ["FastAPI", "Claude 3.7 Sonnet", "PostgreSQL", "AWS EC2", "Python"],
        "impact": "1,600+ queries/day · 92% accuracy",
    },
    {
        "name": "vLLM Inference Stack",
        "short_desc": "50+ concurrent requests at 3,000+ tokens/sec on 96 GB VRAM.",
        "desc": "High-performance inference stack on 96 GB VRAM NVIDIA GPUs with CUDA 12.7 using vLLM. Enables Qwen3-VL (32B, 8-bit quantized) to serve 50+ concurrent requests with sub-3-second latency.",
        "tags": ["vLLM", "CUDA", "Qwen3-VL", "Python", "NVIDIA GPU"],
        "impact": "3,000+ tokens/sec · sub-3s latency",
    },
    {
        "name": "Sheldon",
        "short_desc": "Text-to-config engine eliminating $56,000 in annual misconfiguration losses.",
        "desc": "LLM-powered automation engine using Gemini 1.5 Flash that dynamically generates Python code to parse unstructured brand email and Excel data into PostgreSQL-compatible formats.",
        "tags": ["Gemini 1.5 Flash", "Python", "PostgreSQL", "LLM Orchestration"],
        "impact": "99.42% scheme accuracy · $56K saved/year",
    },
    {
        "name": "Link — Fraud Detection",
        "short_desc": "100,000+ transactions/day, 78% reduction in LEA complaints.",
        "desc": "Fraud detection system processing 100,000+ transactions daily across a 15,000+ merchant base. Built with Python and XGBoost with a fully automated data pipeline.",
        "tags": ["XGBoost", "Python", "PostgreSQL", "Data Pipeline"],
        "impact": "100K+ txns/day · 78% fewer complaints",
    },
    {
        "name": "KYC Verification Pipeline",
        "short_desc": "900+ artifacts/day at 96%+ accuracy, saving $20,000 annually.",
        "desc": "Automated KYC verification pipeline using Python and Celery for async processing, powered by Qwen3-VL 32B (8-bit quantized).",
        "tags": ["Python", "Celery", "Qwen3-VL", "FastAPI"],
        "impact": "96%+ accuracy · $20K saved/year",
    },
    {
        "name": "Freshdesk QC Automation",
        "short_desc": "Validation time from 1,260s to 7s per ticket across 5,000+ images/day.",
        "desc": "Automated QC pipeline using FastAPI and Celery, integrating Qwen3-VL 32B and YOLOv9 to auto-validate support evidence across 5,000+ image artifacts daily.",
        "tags": ["FastAPI", "Celery", "YOLOv9", "Qwen3-VL", "Python"],
        "impact": "1,260s → 7s per ticket",
    },
    {
        "name": "Disha-AI",
        "short_desc": "Address normalization API — 94%+ accuracy, $28,000 cost reduction.",
        "desc": "Address cleanup API leveraging Google Maps API for geocoding and Gemini 1.5 Flash for intelligent address normalization. Redis caching with IP-level rate limiting.",
        "tags": ["FastAPI", "Gemini 1.5 Flash", "Redis", "Google Maps API"],
        "impact": "94%+ accuracy · 20K+ records · $28K saved",
    },
    {
        "name": "ASO Dispatch Algorithm",
        "short_desc": "Geo-optimized field routing with 37% reduction in operational backlog.",
        "desc": "Geo-optimized dispatch algorithm using Haversine distance and priority-weighted allocation against a PostgreSQL backend for faster field engineer routing.",
        "tags": ["Python", "PostgreSQL", "Geospatial", "Algorithms"],
        "impact": "37% backlog reduction",
    },
    {
        "name": "AnotherURLShortener",
        "short_desc": "High-throughput URL shortener with Redis caching and 30-day auto-expiry.",
        "desc": "URL shortener with a Redis hot-path cache (30-day TTL, refreshed on every hit) and SQLite persistence. Redirect flow checks Redis first — cache miss falls back to DB and repopulates the cache. Stats updates on redirect run in a background thread to keep latency near zero. Inactive links auto-expire via an hourly daemon thread; also runnable as a management command. Built with Django, redis-py, and vanilla JS.",
        "tags": ["Django", "Redis", "SQLite", "Caching", "Background Threads", "SSE"],
        "category": "portfolio",
        "url": "/anotherurlshortner/",
    },
    {
        "name": "DataStory",
        "short_desc": "Ask your database anything in plain English — get SQL, charts, and narrative reports.",
        "desc": "Business intelligence platform powered by a 5-node LangGraph agent (planner → SQL gen → executor → analyst → narrator). Supports CSV/Excel upload and direct DB connections. Auto-selects chart type, detects anomalies, and generates plain English narrative. Conversational follow-up with persistent memory. Built with FastAPI, PostgreSQL, Celery, React, and RAGAS eval pipeline.",
        "tags": ["LangGraph", "FastAPI", "React", "PostgreSQL", "NLQ-to-SQL", "RAGAS", "Docker"],
        "category": "portfolio",
        "url": "/datastory/",
    },
    {
        "name": "InventoryWhisperer",
        "short_desc": "Feed your sales data — get demand forecasts, reorder alerts, and supplier drafts.",
        "desc": "Inventory intelligence engine using Prophet for demand forecasting and XGBoost for anomaly detection. LangGraph orchestrates the full reorder workflow — detect low stock → forecast demand → calculate quantity → draft supplier email → await approval. Supports CSV upload and Google Sheets. NLQ over inventory data. Built with FastAPI, Celery Beat, PostgreSQL, and React.",
        "tags": ["LangGraph", "Prophet", "XGBoost", "FastAPI", "Celery", "React", "Docker"],
        "category": "portfolio",
        "url": "/inventory_whisperer/",
    },
    {
        "name": "MarketAnalytics",
        "short_desc": "Describe a market or company — get a real-time intelligence report from across the internet.",
        "desc": "Autonomous market research agent that searches the internet for real events, news, filings, social signals, and hiring trends — then synthesizes a structured intelligence report with source citations. Covers executive summary, event timeline, sentiment trend, competitor signals, and risk/opportunity breakdown. Supports on-demand reports and continuous monitoring with alerts. Built with LangGraph, web search tools, RAG, FastAPI, and React.",
        "tags": ["LangGraph", "Web Search", "RAG", "FastAPI", "React", "Multi-Agent", "Docker"],
        "category": "portfolio",
        "url": "/market_analyst/",
    },
]

BLOG_POSTS = [
    {
        "slug": "pandas-to-duckdb-parquet-analytics",
        "title": "Why I Replaced Pandas with DuckDB and Parquet in My Analytics Engine",
        "date": "Aug 11, 2026",
        "excerpt": "Pandas worked fine until it didn't. As query volume climbed and dataset sizes grew, our analytics engine started showing cracks — slow responses, memory spikes, timeouts on heavy aggregations. The fix wasn't more RAM or a bigger machine. It was rethinking how data moves from storage to query result.",
        "content": """
<p>The analytics engine I built — a natural language to SQL system that takes a plain English question, generates SQL from schema context, and executes it against production data — was working. 92% accuracy, 1,600+ queries a day, users happy. Then the dataset grew. And Pandas, which had been quietly doing the execution layer, started showing its limits.</p>
<p>This is the story of replacing Pandas with DuckDB and Parquet, why it matters technically, and what the actual numbers look like.</p>

<h2>What Was Wrong with Pandas</h2>
<p>Pandas is not a bad tool. It's an excellent tool for the wrong job. The job I was asking it to do was analytical query execution over datasets that were growing into the hundreds of megabytes and beyond. For that specific workload, Pandas has three fundamental problems.</p>
<p><strong>It loads everything into memory eagerly.</strong> When you call <code>pd.read_csv()</code> or <code>pd.read_parquet()</code>, Pandas reads the entire file into a DataFrame before you can touch it. If your query only needs 3 columns out of 40, Pandas still loads all 40. If your filter eliminates 90% of rows, Pandas still reads all the rows first. You pay the full I/O and memory cost before a single computation runs.</p>
<p><strong>It stores data in row-oriented format in memory.</strong> DataFrames are conceptually row-oriented — each row is contiguous in memory. Analytics workloads are column-oriented — a <code>GROUP BY merchant_id, SUM(amount)</code> query only touches two columns out of potentially dozens. Row-oriented storage means loading and scanning data that your query never uses.</p>
<p><strong>It doesn't parallelize across cores.</strong> Python's Global Interpreter Lock (GIL) prevents true multi-threaded execution in Pandas operations<sup>[5]</sup>. On a machine with 16 cores, heavy aggregations use one. The other 15 watch.</p>
<p>For a single analyst running exploratory queries on a laptop, none of this matters. For a system serving 1,600+ queries a day with response time SLAs, it mattered a lot. Average response latency was climbing. On heavy aggregation queries — <code>GROUP BY</code> across large date ranges, multi-table joins — we were hitting 8-12 seconds. Timeouts were occurring on the largest queries.</p>

<h2>The Alternative: Columnar Storage + Columnar Execution</h2>
<p>The combination that solved this was <strong>Parquet files</strong> as the storage format and <strong>DuckDB</strong> as the query engine. These two tools are designed around the same insight: for analytical workloads, reading less data is faster than reading all data quickly.</p>

<h2>Parquet: What's Actually Inside the File</h2>
<p>Parquet is a columnar file format, but "columnar" undersells what it actually does<sup>[3]</sup>. Understanding the internal structure is what makes the performance numbers make sense.</p>
<p>A Parquet file is organized into <strong>row groups</strong> — horizontal slices of the dataset, each containing the same N rows. Within each row group, data is stored by column — all values for column A together, then all values for column B, and so on. Each column within a row group is called a <strong>column chunk</strong>, which is further split into <strong>pages</strong> of compressed data.</p>
<p>This structure enables two critical optimizations:</p>
<ul>
  <li><strong>Projection pushdown.</strong> If your query only needs columns A and C out of 40 columns, a Parquet reader can seek directly to column chunks A and C in each row group and read only those. The other 38 columns are never touched — not read from disk, not loaded into memory. The DuckDB benchmark shows this delivers an <strong>11x speedup</strong> over Pandas on a simple projection query (0.19s vs 2.13s)<sup>[1]</sup>.</li>
  <li><strong>Predicate pushdown.</strong> Each row group stores <strong>statistics</strong> per column: the minimum and maximum value. Before reading any actual data, a query engine can compare the filter condition against these statistics and skip entire row groups where the filter can't possibly match. If you're filtering for <code>WHERE date = '2026-01-15'</code> and a row group's date column has min=2026-03-01, the entire row group is skipped without reading a single byte of row data. The benchmark result: <strong>57x speedup</strong> on filter-heavy queries (0.04s vs 2.29s)<sup>[1]</sup>.</li>
</ul>
<p>Additionally, Parquet applies <strong>dictionary encoding</strong> before compression on low-cardinality columns. A column with values like <code>active</code>, <code>inactive</code>, <code>pending</code> gets encoded as integers 0, 1, 2 — and the compression algorithm works on that integer stream, not the repeated string. This is why Parquet files are 3-5x smaller than equivalent CSV files for typical business data<sup>[6]</sup>, and why that compression compounds with ZSTD or Snappy applied on top.</p>

<h2>DuckDB: The Query Engine That Reads Only What It Needs</h2>
<p>DuckDB is an in-process OLAP database<sup>[2]</sup>. No server to run, no network round-trip — it runs embedded inside your Python process like SQLite, but designed for analytical rather than transactional workloads.</p>
<p>Its query execution model is <strong>vectorized</strong><sup>[4]</sup>: instead of processing one row at a time (like traditional row engines) or writing custom compiled code per query (like some JIT engines), DuckDB processes data in batches — vectors of 1,024 values by default. Each operation applies to an entire vector at once, taking advantage of SIMD CPU instructions. The hardware is doing multiple operations per CPU cycle instead of one.</p>
<p>DuckDB also parallelizes across all available cores automatically. A GROUP BY aggregation on a large dataset fans out across every thread, reduces locally, then merges. No GIL. No manual partition logic. The parallelism is the default.</p>
<p>When DuckDB queries a Parquet file, it performs the full optimization chain:</p>
<ol>
  <li>Reads the Parquet file footer (metadata only — column statistics, row group offsets, schema).</li>
  <li>Uses predicate pushdown to identify which row groups can be skipped based on the filter condition.</li>
  <li>Uses projection pushdown to identify which column chunks need to be read.</li>
  <li>Reads only the qualifying column chunks from qualifying row groups.</li>
  <li>Decompresses and applies vectorized operators (filter, aggregate, join) on the data.</li>
  <li>Returns the result — without the source data ever being fully materialized in memory.</li>
</ol>
<p>The memory difference is dramatic. For a streaming benchmark on the NYC Taxi dataset, DuckDB used <strong>0.3 GB peak memory</strong> vs Pandas' <strong>248 GB</strong> — an 800x reduction — because DuckDB processes row groups sequentially and discards them rather than holding the entire dataset in RAM<sup>[1]</sup>. For large datasets, this isn't an optimization. It's the difference between the query running and the machine running out of memory.</p>

<h2>The Migration</h2>
<p>The analytics engine's architecture before migration: the LLM generates SQL, the execution layer reads the relevant tables from PostgreSQL into Pandas DataFrames using <code>pd.read_sql()</code>, runs the SQL logic as Pandas operations, and returns results.</p>
<p>The problem with this approach is that PostgreSQL's strengths — transactional integrity, row-level locking, ACID compliance — are wasted on analytical read-only queries. And routing large analytical reads through Pandas on top of it compounded the inefficiency.</p>
<p>The new architecture:</p>
<ol>
  <li>Analytical data exports from PostgreSQL are written as Parquet files (partitioned by date where applicable) on the local filesystem or S3.</li>
  <li>The LLM generates SQL as before — same prompt, same schema context.</li>
  <li>Instead of Pandas, DuckDB executes the SQL directly against the Parquet files: <code>duckdb.sql("SELECT ... FROM 'data/transactions/*.parquet' WHERE ...")</code>.</li>
  <li>DuckDB returns an Arrow table; we convert to the response format needed downstream.</li>
</ol>
<p>The migration surface was small. DuckDB speaks standard SQL — the LLM's generated queries required almost no changes. The main adaptation was switching from <code>pd.read_sql()</code> against a live PostgreSQL connection to DuckDB querying Parquet snapshots. For analytical queries (aggregations, trend analysis, cross-table joins over historical data), this is the right architecture anyway — you don't want ad-hoc analytical loads hitting your transactional database.</p>

<h2>Concrete Code: Before and After</h2>
<p>Before — Pandas over PostgreSQL:</p>
<pre style="background: var(--bg-alt, #111); padding: 1rem; border-radius: 2px; font-size: 0.775rem; overflow-x: auto; color: var(--text-muted); margin-bottom: 1.25rem;">
df = pd.read_sql(generated_sql, postgres_conn)
result = df.to_dict(orient="records")
</pre>
<p>After — DuckDB over Parquet:</p>
<pre style="background: var(--bg-alt, #111); padding: 1rem; border-radius: 2px; font-size: 0.775rem; overflow-x: auto; color: var(--text-muted); margin-bottom: 1.25rem;">
result = duckdb.sql(generated_sql).fetchdf().to_dict(orient="records")
</pre>
<p>The SQL the LLM generates is the same. The table references resolve to Parquet paths instead of PostgreSQL tables. DuckDB handles the rest.</p>

<h2>What Changed After Migration</h2>
<p>The improvements weren't marginal. For aggregation-heavy queries — the ones Pandas was slowest at — average response time dropped from 8-12 seconds to under 1 second. Complex multi-table joins over large date ranges went from timeout territory to 2-3 seconds. Memory usage during peak query load dropped significantly, eliminating the spikes that were occasionally causing OOM conditions on the analytics server.</p>
<p>The Parquet storage format itself contributed independently: the same data that was stored as CSV for Pandas ingestion was now stored as Parquet with Snappy compression. Storage footprint dropped by roughly 3x on the same data. Read I/O dropped proportionally, since Parquet reads only the columns and row groups the query touches.</p>
<p>The performance characteristics align closely with the benchmarked numbers: DuckDB's 57x advantage on filter-heavy queries and 11x advantage on projection queries<sup>[1]</sup> map directly to the kinds of analytical SQL the NLQ engine generates — date filters, merchant filters, aggregations across a subset of columns.</p>

<h2>When This Swap Makes Sense</h2>
<p>This isn't a universal replacement for Pandas. Pandas remains the right tool for:</p>
<ul>
  <li>Row-level transformations and feature engineering where you're operating on individual records.</li>
  <li>Small datasets where load time is negligible and the API ergonomics matter more than raw speed.</li>
  <li>Exploratory data science workflows where you're mutating and inspecting DataFrames interactively.</li>
</ul>
<p>DuckDB + Parquet is the right stack when:</p>
<ul>
  <li>Your workload is predominantly <strong>analytical</strong> — aggregations, group-bys, multi-column filters, joins across large tables.</li>
  <li>Your dataset is large enough that eager full-load into memory creates latency or OOM risk.</li>
  <li>You need SQL semantics — DuckDB executes standard SQL directly, no DataFrame API translation required.</li>
  <li>You're already storing data in Parquet (or willing to) — the predicate and projection pushdown only help if the storage format supports them.</li>
</ul>
<p>The NLQ analytics use case sits squarely in the DuckDB + Parquet zone. The LLM generates SQL. The data is historical and append-only. The queries are read-only aggregations. Pandas was never the right fit — it was just the default.</p>

<h2>The Core Insight</h2>
<p>Pandas operates on a simple model: load data into memory, then operate on it. That model breaks down as datasets grow because the load step becomes the dominant cost — both in time and memory — before any computation runs.</p>
<p>DuckDB and Parquet together implement a different model: push the query into the data. Read only the columns you need. Skip the row groups you can prove are irrelevant. Process in parallel using all available cores. Return a result without ever fully materializing the source dataset in memory.</p>
<p>For analytical workloads, "read less" beats "read fast." The tools that implement this properly — columnar storage, vectorized execution, predicate and projection pushdown — deliver order-of-magnitude improvements not because they have faster CPUs, but because they do dramatically less work.</p>

<div class="post-references">
  <p class="references-label">references</p>
  <ol>
    <li><a href="https://duckdb.org/2021/12/03/duck-arrow.html" target="_blank" rel="noopener">DuckDB and Apache Arrow: Projection and Predicate Pushdown Benchmarks — DuckDB Blog</a></li>
    <li><a href="https://duckdb.org/why_duckdb" target="_blank" rel="noopener">Why DuckDB — DuckDB Official Documentation</a></li>
    <li><a href="https://parquet.apache.org/docs/file-format/" target="_blank" rel="noopener">Apache Parquet File Format Specification — Apache Parquet Official Docs</a></li>
    <li><a href="https://duckdb.org/docs/stable/internals/overview" target="_blank" rel="noopener">DuckDB Internals: Vectorized Query Execution — DuckDB Official Docs</a></li>
    <li><a href="https://wiki.python.org/moin/GlobalInterpreterLock" target="_blank" rel="noopener">Python Global Interpreter Lock (GIL) — Python Wiki</a></li>
    <li><a href="https://www.vldb.org/pvldb/vol17/p148-zeng.pdf" target="_blank" rel="noopener">An Empirical Evaluation of Columnar Storage Formats — VLDB 2024</a></li>
    <li><a href="https://duckdb.org/docs/stable/guides/performance/file_formats" target="_blank" rel="noopener">DuckDB File Format Performance Guide — DuckDB Official Docs</a></li>
    <li><a href="https://arrow.apache.org/docs/python/parquet.html" target="_blank" rel="noopener">Reading and Writing Parquet Files — Apache Arrow Python Docs</a></li>
  </ol>
</div>
""",
    },
    {
        "slug": "easyocr-sqlite-image-pipeline",
        "title": "I Was Given a Month of Image Analysis Work. I Automated It in Two Days.",
        "date": "Nov 2022",
        "excerpt": "Fresh at the firm, bored out of my mind staring at nearly 3,000 image files I was supposed to analyze manually. So I built a pipeline: EasyOCR for text extraction, a structural parser to make sense of the layout, and SQLite to store it all in queryable tables. The month's backlog was gone by Wednesday.",
        "content": """
<p>It was my first few weeks at the firm. I'd just joined, I didn't know anyone well enough to push back on assignments yet, and someone handed me a stack of image files — scanned documents, screenshots, mixed-format files — with a task: extract the data and organize it. Manually. The estimate was about a month of work.</p>
<p>I stared at the first image for maybe fifteen minutes. Then I opened a new Python file.</p>
<p>Two days later, the entire backlog was done. This is the technical story of how that pipeline worked — the OCR layer, the structural parsing problem, the database schema, and the parts that were harder than they looked.</p>

<h2>The Problem, Precisely Stated</h2>
<p>The images weren't random photographs. They were structured documents — forms, invoices, tables, ledger entries — that had been scanned or screenshotted and saved as PNGs and JPEGs. The task was to extract the text content and store it in a structured format that could be queried and reported on.</p>
<p>Doing this manually means: open image, read it, type the values into a spreadsheet, repeat. For a few dozen images, that's an afternoon. For hundreds, it's a month.</p>
<p>Automating it means solving three distinct problems in sequence:</p>
<ol>
  <li><strong>OCR:</strong> Extract raw text from the image pixels.</li>
  <li><strong>Structural parsing:</strong> Understand <em>what</em> the text means — which values are field labels, which are data, where the logical boundaries are.</li>
  <li><strong>Storage:</strong> Persist the extracted, structured data in a form that's queryable without additional transformation.</li>
</ol>
<p>Each of these looks straightforward until you start implementing it.</p>

<h2>The OCR Layer: EasyOCR</h2>
<p>OCR (Optical Character Recognition) is a solved problem in the sense that good libraries exist. Choosing the right one matters. The two main Python options I evaluated were <strong>Tesseract</strong> (via <code>pytesseract</code>) and <strong>EasyOCR</strong>.</p>
<p>Tesseract is older, faster on clean inputs, and widely used. EasyOCR is a deep learning-based approach — it runs a CRAFT (Character Region Awareness For Text detection) model for text detection followed by a CRNN (Convolutional Recurrent Neural Network) for recognition<sup>[1]</sup>. The distinction matters for document images specifically: Tesseract assumes relatively clean, typed text on white backgrounds. The documents I was working with had varying scan quality, occasional handwritten annotations, mixed fonts, and tables with thin ruling lines. EasyOCR's detection model handles irregular layouts more robustly.</p>
<p>The EasyOCR API is straightforward:</p>
<pre style="background: var(--bg-alt, #111); padding: 1rem; border-radius: 2px; font-size: 0.775rem; overflow-x: auto; color: var(--text-muted); margin-bottom: 1.25rem;">
import easyocr

reader = easyocr.Reader(['en'], gpu=False)
results = reader.readtext('document.png')
</pre>
<p><code>reader.readtext()</code> returns a list of tuples — one per detected text region — each containing three elements: a bounding box (four corner coordinates), the detected text string, and a confidence score between 0 and 1:</p>
<pre style="background: var(--bg-alt, #111); padding: 1rem; border-radius: 2px; font-size: 0.775rem; overflow-x: auto; color: var(--text-muted); margin-bottom: 1.25rem;">
[
  ([[12, 18], [210, 18], [210, 38], [12, 38]], 'Invoice No:', 0.97),
  ([[215, 18], [310, 18], [310, 38], [215, 38]], 'INV-20221104', 0.94),
  ([[12, 52], [180, 52], [180, 72], [12, 72]], 'Date:', 0.99),
  ([[185, 52], [280, 52], [280, 72], [185, 72]], '04/11/2022', 0.91),
  ...
]
</pre>
<p>The raw output gives you text with spatial position. That's the foundation — but spatial position alone doesn't tell you that "Invoice No:" is a label and "INV-20221104" is its value, or that these two form a key-value pair that should land in the same database row.</p>

<h2>The Hard Part: Structural Parsing</h2>
<p>This is where most OCR tutorials stop, and where the actual engineering starts.</p>
<p>A scanned document has implicit structure that humans read effortlessly: labels are visually paired with their values, table headers span columns, rows belong to sections, totals appear at the bottom of groups. None of this structure is encoded in the pixels. EasyOCR gives you text fragments with bounding boxes. Turning those fragments into structured records requires reasoning about spatial relationships.</p>
<p>I built the parser around two observations:</p>
<p><strong>1. Horizontal proximity on the same line is key-value pairing.</strong> If two text regions share approximately the same vertical center (within a tolerance, since scan alignment is imperfect) and are horizontally adjacent with no other text in between, they're probably a label-value pair. The rule:</p>
<pre style="background: var(--bg-alt, #111); padding: 1rem; border-radius: 2px; font-size: 0.775rem; overflow-x: auto; color: var(--text-muted); margin-bottom: 1.25rem;">
def same_line(box_a, box_b, y_tolerance=8):
    center_a = (box_a[0][1] + box_a[2][1]) / 2
    center_b = (box_b[0][1] + box_b[2][1]) / 2
    return abs(center_a - center_b) < y_tolerance
</pre>
<p>The Y-tolerance of 8 pixels handled the slight baseline drift from scanning. Too tight and you'd miss pairs on slightly misaligned scans; too loose and you'd pair text from adjacent rows.</p>
<p><strong>2. Labels end with a colon.</strong> This was the heuristic that made the key-value detection reliable on these specific documents. Fields like "Invoice No:", "Date:", "Amount:", "Vendor:" all terminated with a colon. If a text region ends with ":" and is on the same line as a subsequent region that doesn't, the first is the key and the second is the value. It sounds simple — it was. But it worked on 94% of the documents without exception handling.</p>
<p>The structural parsing pipeline:</p>
<ol>
  <li>Sort all OCR results by vertical position (Y-coordinate) to process top-to-bottom.</li>
  <li>Group results into "lines" by clustering on Y-center with the tolerance above.</li>
  <li>Within each line, sort by X-coordinate (left to right).</li>
  <li>Scan each line for colon-terminated tokens; pair them with the immediately following token on the same line.</li>
  <li>Collect all key-value pairs from the document into a flat dictionary.</li>
</ol>
<pre style="background: var(--bg-alt, #111); padding: 1rem; border-radius: 2px; font-size: 0.775rem; overflow-x: auto; color: var(--text-muted); margin-bottom: 1.25rem;">
def extract_kv_pairs(ocr_results, y_tolerance=8):
    # Sort by vertical position
    sorted_results = sorted(ocr_results, key=lambda r: (r[0][0][1] + r[0][2][1]) / 2)

    # Group into lines
    lines = []
    current_line = [sorted_results[0]]
    for result in sorted_results[1:]:
        if same_line(current_line[-1][0], result[0], y_tolerance):
            current_line.append(result)
        else:
            lines.append(sorted(current_line, key=lambda r: r[0][0][0]))
            current_line = [result]
    lines.append(current_line)

    # Extract key-value pairs
    pairs = {}
    for line in lines:
        for i, (box, text, conf) in enumerate(line):
            if text.strip().endswith(':') and i + 1 < len(line):
                key = text.strip().rstrip(':').strip()
                value = line[i + 1][1].strip()
                pairs[key] = value
    return pairs
</pre>
<p>For a typical invoice image, this produced a dictionary like:</p>
<pre style="background: var(--bg-alt, #111); padding: 1rem; border-radius: 2px; font-size: 0.775rem; overflow-x: auto; color: var(--text-muted); margin-bottom: 1.25rem;">
{
  "Invoice No": "INV-20221104",
  "Date": "04/11/2022",
  "Vendor": "Acme Supplies Pvt Ltd",
  "Amount": "₹48,200.00",
  "GST": "₹8,676.00",
  "Total": "₹56,876.00"
}
</pre>

<h2>Table Detection: The Harder Case</h2>
<p>Not all documents were forms. Some were tables — grids of data with headers and rows. These required a different parsing strategy because the colon heuristic doesn't apply and the horizontal grouping is two-dimensional.</p>
<p>For tables, I used a different approach: detect the header row (usually the topmost line with multiple tokens, often with bold or distinct styling that EasyOCR picks up as higher-confidence detections), then treat each subsequent row as a record keyed against those column headers.</p>
<p>The column alignment challenge: in a scanned table, the X-coordinates of values in a column aren't exactly aligned — there's pixel-level variation. I resolved this by building a column boundary map from the header row. For each header token, I recorded its X-range (left edge to right edge). Values in subsequent rows were assigned to columns by checking which header's X-range their X-center fell within, with a tolerance for slight misalignment:</p>
<pre style="background: var(--bg-alt, #111); padding: 1rem; border-radius: 2px; font-size: 0.775rem; overflow-x: auto; color: var(--text-muted); margin-bottom: 1.25rem;">
def assign_to_column(token_box, column_ranges, x_tolerance=15):
    token_center_x = (token_box[0][0] + token_box[1][0]) / 2
    for col_name, (col_left, col_right) in column_ranges.items():
        if col_left - x_tolerance <= token_center_x <= col_right + x_tolerance:
            return col_name
    return None  # token falls outside all known columns
</pre>
<p>This worked reliably on clean tables. For tables with merged cells or spanning headers, I fell back to manual flagging — the pipeline wrote those images to an <code>ambiguous/</code> folder for human review rather than silently producing wrong output.</p>

<h2>Storage: SQLite with Dynamic Schema</h2>
<p>The storage layer had one interesting constraint: the documents didn't all have the same fields. Different document types had different key sets. A purchase order had fields an invoice didn't; a receipt had fields neither had. I needed a schema that could accommodate this without requiring a different table per document type.</p>
<p>I used SQLite for two reasons: zero infrastructure (it's a file, no server), and the fact that the downstream consumer of this data was going to query it with SQL anyway. No point adding a translation layer.</p>
<p>The schema:</p>
<pre style="background: var(--bg-alt, #111); padding: 1rem; border-radius: 2px; font-size: 0.775rem; overflow-x: auto; color: var(--text-muted); margin-bottom: 1.25rem;">
CREATE TABLE IF NOT EXISTS documents (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    filename    TEXT NOT NULL,
    doc_type    TEXT,
    processed_at TEXT DEFAULT (datetime('now')),
    confidence_avg REAL
);

CREATE TABLE IF NOT EXISTS fields (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    document_id INTEGER REFERENCES documents(id),
    field_key   TEXT NOT NULL,
    field_value TEXT,
    confidence  REAL
);

CREATE INDEX IF NOT EXISTS idx_fields_key ON fields(field_key);
CREATE INDEX IF NOT EXISTS idx_fields_doc ON fields(document_id);
</pre>
<p>Every document gets a row in <code>documents</code>. Every extracted key-value pair gets a row in <code>fields</code>, referencing its parent document. The <code>field_key</code> index makes querying across documents for a specific field fast — <code>SELECT d.filename, f.field_value FROM documents d JOIN fields f ON f.document_id = d.id WHERE f.field_key = 'Invoice No'</code> runs in milliseconds even with thousands of documents because the index covers the predicate.</p>
<p>I also stored the OCR confidence score per field and the average per document. This turned out to be useful immediately — documents with low average confidence (below 0.75) were flagged for review, and the threshold caught every genuinely bad extraction in the test set.</p>

<h2>The Orchestrator</h2>
<p>The top-level pipeline tied it together:</p>
<pre style="background: var(--bg-alt, #111); padding: 1rem; border-radius: 2px; font-size: 0.775rem; overflow-x: auto; color: var(--text-muted); margin-bottom: 1.25rem;">
import os, sqlite3, easyocr

reader = easyocr.Reader(['en'], gpu=False)
conn = sqlite3.connect('documents.db')
init_schema(conn)

image_dir = 'inputs/'
for fname in os.listdir(image_dir):
    if not fname.lower().endswith(('.png', '.jpg', '.jpeg')):
        continue

    path = os.path.join(image_dir, fname)
    ocr_results = reader.readtext(path)

    if is_table_document(ocr_results):
        records = extract_table_records(ocr_results)
        store_table_records(conn, fname, records)
    else:
        kv_pairs = extract_kv_pairs(ocr_results)
        avg_conf = sum(r[2] for r in ocr_results) / len(ocr_results)
        store_kv_document(conn, fname, kv_pairs, avg_conf)

conn.close()
</pre>
<p>The <code>is_table_document()</code> heuristic was simple: if the topmost detected line had more than 3 tokens and none ended with a colon, it was a table header. That covered every table in the dataset without a single misclassification.</p>

<h2>EasyOCR Initialization: The One Footgun</h2>
<p>One thing worth calling out explicitly: <code>easyocr.Reader</code> downloads model weights on first instantiation and loads them into memory — this takes 10-30 seconds and several hundred MB of RAM. Initialize the reader <em>once</em> at startup, never inside a loop. The code above does this correctly, but it's easy to miss if you're iterating quickly, and the performance penalty of re-initializing per file is severe enough to make the pipeline feel broken.</p>

<h2>Numbers</h2>
<p>The full dataset was close to 3,000 image files. Processing time end-to-end was about 36 hours on CPU (no GPU) — I kicked it off overnight and let it run. The EasyOCR model is the bottleneck: each image takes 1-4 seconds depending on content density. With GPU inference that drops by roughly 5x, but the machine I was running this on didn't have a GPU and it didn't matter: 36 hours of unattended compute to do a month of manual work is an excellent trade.</p>
<p>Accuracy: 94% of key-value pairs extracted correctly on the first pass. The remaining 6% fell into two buckets — genuinely poor scan quality (blurry or skewed images where EasyOCR confidence was already low and flagging worked correctly) and a handful of two-line field values that the single-line parser missed. I fixed the two-line case in about 20 minutes after reviewing the flagged outputs.</p>
<p>The SQLite database ended up at around 18 MB for ~3,000 documents and ~42,000 extracted fields. Query time for any field lookup: under 5ms.</p>

<h2>What I'd Do Differently</h2>
<p>The colon-heuristic for label detection is brittle outside the specific document types I was working with. A more robust approach would be to use a layout analysis model — LayoutLM<sup>[2]</sup> or a similar document understanding model — which reasons about document structure semantically rather than with geometric heuristics. For the scope of this project, the heuristic was the right call: it took an hour to implement and worked. A transformer-based layout model would have taken days and delivered marginal accuracy improvement on these specific documents.</p>
<p>I'd also separate the confidence-based flagging threshold into a config parameter exposed at the CLI level. Hardcoding 0.75 worked here, but different document types have different baseline confidence distributions, and making this tunable without touching code would make the tool more reusable.</p>
<p>The schema is also intentionally simple. For a production system with many document types, you'd want a <code>document_types</code> table and a way to define expected fields per type — so you can detect when a supposedly standard document is missing required fields, rather than silently storing an incomplete record.</p>

<h2>The Actual Lesson</h2>
<p>The technical decisions here were all reasonable, but the more interesting thing is what the exercise revealed about the nature of "manual" knowledge work. The person who assigned me this task had done the same type of image-to-spreadsheet work before, by hand. It had taken roughly a month. The expectation was that it would take me a month too — that the work was inherently proportional to the number of files.</p>
<p>It isn't. Most structured manual data extraction is pattern-following. If it's pattern-following, it can be described as rules. If it can be described as rules, it can be automated. The limiting factor is rarely the complexity of the automation — the EasyOCR + SQLite pipeline is maybe 200 lines of Python — it's whether you recognize that the pattern exists and whether you have the tools to exploit it.</p>
<p>The boredom was useful. If the task had been interesting, I might have just done it manually.</p>

<div class="post-references">
  <p class="references-label">references</p>
  <ol>
    <li><a href="https://github.com/JaidedAI/EasyOCR" target="_blank" rel="noopener">EasyOCR — CRAFT + CRNN architecture, JaidedAI GitHub</a></li>
    <li><a href="https://arxiv.org/abs/2006.01038" target="_blank" rel="noopener">LayoutLM: Pre-training of Text and Layout for Document Image Understanding — Microsoft Research, arXiv 2006.01038</a></li>
    <li><a href="https://www.sqlite.org/whentouse.html" target="_blank" rel="noopener">When to Use SQLite — SQLite Official Documentation</a></li>
  </ol>
</div>
""",
    },
    {
        "slug": "kafka-explained-with-harry-potter",
        "title": "Kafka, Explained with Harry Potter",
        "date": "Jul 17, 2026",
        "excerpt": "Apache Kafka is one of those systems that sounds simple until you actually try to explain it. Topics, partitions, consumer groups, offsets — the terminology piles up fast. So let's explain it the way it should have been explained from the start: through Hogwarts.",
        "content": """
<p>Apache Kafka is described in official documentation as "a distributed event streaming platform." That sentence is accurate and tells you almost nothing useful. Let's try a different approach.</p>
<p>Imagine Hogwarts has a messaging system. Not owls — owls are too slow and too stateful. Something faster. Something that can handle millions of messages at once, replay them on demand, let multiple independent groups read the same message without interfering with each other, and survive broker failures without losing a single event.</p>
<p>That system is Kafka. Let's build it completely, one Harry Potter analogy at a time — from the basics to the parts most tutorials skip.</p>

<h2>The Daily Prophet is a Topic</h2>
<p>In Kafka, a <strong>topic</strong> is a named, ordered, append-only log of events<sup>[2]</sup>. Not a mailbox. Not a queue. A newspaper. The Daily Prophet publishes news. Everyone who wants wizard news reads The Daily Prophet. The paper doesn't disappear after one person reads it. Multiple people read the same edition independently. A new edition is published and appended — old ones stay.</p>
<p>A Kafka topic works the same way. Events are appended to the end of the log in the order they arrive, and they stay there. One topic can be <code>payment_events</code>, another <code>user_signups</code>, another <code>fraud_alerts</code>. Each is a separate, ordered, immutable stream. The default retention is <strong>7 days</strong><sup>[1]</sup> — configurable per topic, from seconds to indefinitely.</p>
<p>The critical difference from a traditional message queue: consuming a message doesn't destroy it. The Daily Prophet doesn't shred itself after you read it. Every reader gets their own independent copy.</p>

<h2>The Owlery is a Broker</h2>
<p>A <strong>broker</strong> is a Kafka server — it stores partitions and handles all reads and writes. A Kafka cluster is multiple brokers working together. Think of each broker as an owlery: a physical building that receives, stores, and dispatches messages across different wings of the castle.</p>
<p>A single broker can handle roughly <strong>1 million messages per second</strong> with storage capacity in the terabytes<sup>[1]</sup>. The cluster distributes load so no single owlery gets overwhelmed. If one burns down, the others keep running.</p>
<p>One broker in the cluster acts as the <strong>controller</strong> — it tracks which brokers are alive, manages partition leadership assignments, and handles failover. If the controller itself fails, a new one is elected. In older Kafka versions, ZooKeeper handled this coordination externally. From Kafka 3.3+, this is handled internally via <strong>KRaft</strong> — Kafka's own Raft-based consensus protocol — eliminating the ZooKeeper dependency entirely<sup>[3]</sup>.</p>

<h2>Replication and the Order of the Phoenix (ISR)</h2>
<p>Each topic partition has one <strong>leader</strong> replica and multiple <strong>follower</strong> replicas spread across different brokers. The leader handles all reads and writes. Followers passively replicate the leader's log.</p>
<p>Not all followers are equal. Kafka tracks which followers are actually caught up — these are the <strong>In-Sync Replicas (ISR)</strong><sup>[6]</sup>. Think of the ISR as the Order of the Phoenix: a trusted inner circle of members who are current, present, and reliable. A follower falls out of ISR if it lags too far behind (configurable via <code>replica.lag.time.max.ms</code>).</p>
<p>When the leader fails, only an ISR member can be promoted to leader. This is the safety guarantee: a new leader is always current. If Kafka allowed out-of-sync followers to become leaders, you'd get a new leader with stale data — some messages would silently vanish.</p>
<p>The replication factor is typically set to 3: one leader and two followers. This means the cluster can survive the loss of two brokers for that partition before data is at risk.</p>

<h2>Producers and the Three Levels of Trust</h2>
<p>A <strong>producer</strong> is any application that writes events to a topic. But how much confirmation does the producer need before moving on? Kafka gives you three levels, controlled by the <code>acks</code> setting:</p>
<ul>
  <li><strong>acks=0 — Fire and forget.</strong> The producer sends the message and doesn't wait for any acknowledgment. Like sending an owl with no return receipt. Maximum throughput, zero durability. If the broker crashes mid-receive, the message is gone and you'll never know.</li>
  <li><strong>acks=1 — Leader confirms.</strong> The leader broker writes the message and acknowledges it. Like your owl arriving at the owlery and you getting a confirmation signal. Fast, but if the leader crashes before its followers replicate the message, data is lost during the failover.</li>
  <li><strong>acks=all — Every ISR member confirms.</strong> The leader writes the message and waits for every in-sync replica to confirm before acknowledging. Every backup owlery receives the message before you're told it's safe. This is the strongest durability guarantee available<sup>[1]</sup>. Slower, but a message acknowledged at <code>acks=all</code> survives any single broker failure.</li>
</ul>
<p>Producers can also batch multiple messages into a single send call and compress them (GZIP, Snappy, or LZ4) — trading some latency for significantly higher throughput. Keep individual messages under <strong>1MB</strong> for optimal performance<sup>[1]</sup>.</p>

<h2>Partitions are the Owlery's Sorting Slots</h2>
<p>A single topic receiving millions of events per second can't be handled by one machine. This is what <strong>partitions</strong> solve.</p>
<p>Each topic is split into N partitions — independent, ordered sub-logs distributed across brokers. Think of the owlery as having 12 sorting slots: each slot handles a specific range of mail, independently and in parallel. The total throughput of the owlery is the sum of all slots.</p>
<p>Producers route messages to partitions using a key: <code>partition = hash(key) % num_partitions</code><sup>[1]</sup>. All messages with the same key go to the same partition, preserving order for that key. Messages without a key are distributed round-robin across partitions.</p>
<p>Partitions are the primary scaling lever in Kafka. More partitions → more parallelism → more throughput. But they come with a constraint: partitions are permanent. You can add partitions to a topic, but you cannot remove them. Plan your partition count at topic creation time.</p>

<h2>The Hot Partition Problem: When One Slot Gets All the Mail</h2>
<p>If your partition key isn't well-chosen, you can end up with one slot receiving almost all the traffic while the others sit idle. A hot partition is a real production failure mode<sup>[1]</sup>.</p>
<p>Imagine keying all payment events by <code>merchant_id</code>, but one merchant processes 80% of your transactions. Every message for that merchant goes to one partition. One consumer handles that partition. That consumer is crushed; the others are bored.</p>
<p>Solutions:</p>
<ul>
  <li><strong>Compound keys.</strong> Combine <code>merchant_id</code> with <code>transaction_date</code> or a random suffix to distribute load.</li>
  <li><strong>Random salting.</strong> Append a random number (0–N) to the key. Spreads load across N×partitions. Breaks strict ordering — acceptable if ordering per key isn't required.</li>
  <li><strong>No key at all.</strong> Go round-robin. Loses per-key ordering, gains perfect load distribution.</li>
  <li><strong>Back pressure at the producer.</strong> Rate-limit production from hot sources so downstream partitions don't saturate.</li>
</ul>

<h2>Consumers are Students Reading the Board</h2>
<p>A <strong>consumer</strong> is any application that reads events from a topic. Crucially, Kafka consumers are <strong>pull-based</strong> — they poll the broker for messages at their own pace<sup>[2]</sup>. The broker doesn't push messages at consumers. This matters: a slow consumer doesn't get overwhelmed by a fast producer. It reads what it can, when it can, and picks up from where it left off.</p>
<p>That "where it left off" is the <strong>offset</strong>. Every message in a partition has a sequential integer — 0, 1, 2, 3... — its offset. A consumer commits its current offset to Kafka's internal <code>__consumer_offsets</code> topic after processing. If it crashes and restarts, it reads the last committed offset and resumes from there.</p>
<p>This creates a choice: commit <strong>before</strong> or <strong>after</strong> processing?</p>
<ul>
  <li><strong>Commit after processing (at-least-once).</strong> If the consumer crashes between processing and committing, the message is reprocessed on restart. Safe — no messages dropped. Requires idempotent consumers.</li>
  <li><strong>Commit before processing (at-most-once).</strong> If the consumer crashes after committing but before finishing, the message is skipped. Faster, but data loss is possible. Only acceptable where missing events is tolerable.</li>
</ul>
<p>Kafka also supports <strong>exactly-once semantics</strong> via transactional producers and atomic offset commits — but this requires explicit opt-in configuration and is more complex to operate<sup>[7]</sup>.</p>

<h2>Consumer Groups are Hogwarts Houses</h2>
<p>What if your fraud detection service, analytics pipeline, and audit logger all need to process every payment event? You don't want them sharing a single consumer that hands off events one-at-a-time. You want each system to get every event, independently.</p>
<p>This is what <strong>consumer groups</strong> solve. Each group is like a Hogwarts house — Gryffindor, Slytherin, Hufflepuff, Ravenclaw. Each house reads the notice board independently. Gryffindor reading an announcement doesn't consume it for Slytherin. Their progress is tracked separately.</p>
<p>In Kafka: each service gets its own consumer group ID. Every group subscribes to the same topic. Every group gets its own offset pointer per partition. One group being slow, crashing, or reprocessing events has zero effect on any other group<sup>[4]</sup>.</p>
<p>Within a group, partitions are divided among consumers — each partition is owned by exactly one consumer in the group at any time. This is how a group scales horizontally: add more consumers to a group, and they take on more partitions in parallel.</p>

<h2>Consumer Rebalancing: When a Prefect Leaves</h2>
<p>When a consumer joins or leaves a group — because a new instance started, an instance crashed, or a deployment happened — Kafka triggers a <strong>rebalance</strong>. All partition assignments across the group are redistributed.</p>
<p>Think of a Prefect leaving Hogwarts mid-year. Their responsibilities don't disappear — they get redistributed among the remaining Prefects. A new Prefect joins? Responsibilities are redistributed again.</p>
<p>During a rebalance, all consumers in the group pause processing. This is the cost. Rebalances can cause consumer lag spikes and processing delays. Kafka mitigates this with <strong>incremental cooperative rebalancing</strong> (since Kafka 2.4) — only the partitions that need to move are reassigned, rather than revoking everything and starting over. This reduces pause time significantly<sup>[3]</sup>.</p>

<h2>Consumer Lag: Falling Behind on the Daily Prophet</h2>
<p>Consumer lag is the gap between the latest message produced to a partition and the last offset committed by a consumer group. If a consumer group is on offset 10,000 and the producer is at offset 15,000, the lag is 5,000 messages.</p>
<p>Lag is normal during traffic bursts. It becomes a problem when it grows continuously — indicating a consumer that can't keep up with the production rate. Left unmonitored, a consumer group can fall so far behind that it starts reading messages that have already been deleted by Kafka's retention policy. At that point, the consumer group resets to the earliest available offset, potentially missing events permanently.</p>
<p>Monitor lag. Alert on it. Scale consumers (or partitions) when it trends upward consistently.</p>

<h2>The Pensieve is Log Replay</h2>
<p>Dumbledore's Pensieve lets you step back into any memory from the beginning. Kafka's offset system provides the same capability.</p>
<p>Any consumer can reset its offset to an earlier position and replay the log from there. A new service comes online? Replay the last 30 days of events and build state from scratch. A bug corrupted downstream data? Reset the offset and reprocess clean. An analyst needs historical data? Read from offset 0.</p>
<p>This is the defining feature that separates Kafka from a message queue. Once a queue delivers a message, it's gone. Kafka's append-only log is a permanent record — replayable, re-consumable, queryable from any point — for as long as retention keeps it.</p>

<h2>Log Compaction: Hermione's Revised Notes</h2>
<p>Standard retention deletes messages by age or total size. But there's a second retention mode: <strong>log compaction</strong>.</p>
<p>Hermione doesn't keep every draft of her notes. She keeps the latest version. If she revised her notes on Polyjuice Potion three times, only the final revision matters.</p>
<p>Log compaction works the same way. For a given message key, Kafka guarantees that the <strong>latest value</strong> for that key is always retained — even after the time-based retention window has passed. Old values for the same key get cleaned up during compaction runs. The result is a topic that acts as a compacted snapshot: for every key, you always have the most recent state.</p>
<p>This is perfect for use cases like user profile updates, product catalog changes, or configuration state — where you only care about the current value, not the full history. It's also the foundation of how Kafka Streams builds stateful applications: compacted topics serve as persistent state stores.</p>

<h2>The Room of Requirement: Dead Letter Queues</h2>
<p>Sometimes a message genuinely can't be processed. The payload is malformed, the downstream service is broken, the business logic throws an exception. If you let the consumer retry forever, it blocks all subsequent messages in that partition.</p>
<p>The Room of Requirement appears when you need it most and holds things that have nowhere else to go. Dead Letter Queues (DLQs) work the same way: a separate Kafka topic where failed messages are routed after exhausting retries<sup>[1]</sup>. The main consumer moves on. The DLQ topic accumulates failed events for investigation, replay, or manual resolution.</p>
<p>A common pattern: a retry topic with increasing delay, followed by a DLQ for persistent failures. The consumer reads from the main topic, on failure writes to <code>topic.retry</code>, on exhausted retries writes to <code>topic.dlq</code>.</p>

<h2>Howlers are At-Least-Once Delivery</h2>
<p>A Howler keeps screaming until acknowledged. Kafka's default guarantee is <strong>at-least-once</strong> — a message will be delivered to a consumer at least one time. In crash scenarios (consumer processes the message, crashes before committing the offset), the message is redelivered on restart<sup>[1]</sup>.</p>
<p>The correct response is idempotent consumer design: processing the same event twice produces the same result as processing it once. Use a unique event ID as a deduplication key, check before applying side effects, or use a transactional write that is naturally idempotent.</p>

<h2>The Floo Network: Kafka Connect</h2>
<p>The Floo Network connects Hogwarts to every fireplace in the wizarding world — you can step into one and emerge from any other without writing custom transportation logic.</p>
<p><strong>Kafka Connect</strong> is Kafka's integration framework for the same purpose. Pre-built connectors move data between Kafka and external systems — databases, cloud storage, search indexes, data warehouses — without custom code<sup>[4]</sup>. A source connector reads from a Postgres table and writes to a Kafka topic. A sink connector reads from a Kafka topic and writes to S3 or Elasticsearch. Hundreds of connectors exist for common systems. You configure, not code.</p>
<p>Connectors run in a Connect cluster, handle their own fault tolerance and restart behavior, and scale independently of your producers and consumers.</p>

<h2>Kafka's Honest Tradeoff</h2>
<p>Hello Interview's deep dive<sup>[1]</sup> frames it clearly: <em>"Kafka is always available, sometimes consistent."</em> Because replication is asynchronous, a leader that acknowledges a write at <code>acks=1</code> and immediately fails could lose that write if the follower hasn't synced yet. Even at <code>acks=all</code>, if all ISR members fail simultaneously before a follower outside the ISR catches up, messages can be lost.</p>
<p>Kafka optimizes for availability and throughput, not for strict consistency. For most event-streaming workloads — where occasional reprocessing is acceptable and throughput matters — this is exactly the right tradeoff. If you need hard transactional guarantees across multiple systems, layer that on top via exactly-once semantics and idempotent consumers, or reconsider whether Kafka is the right primary store.</p>

<h2>When to Use Kafka (and When Not To)</h2>
<p>Kafka is the right tool when:</p>
<ul>
  <li>Multiple independent services need to consume the same event stream without coupling.</li>
  <li>You need event replay — bootstrapping new services, recovering from bugs, reprocessing for new logic.</li>
  <li>You have high throughput with spiky producers and slower consumers that need to catch up independently.</li>
  <li>You need durable, ordered event storage that outlasts any single consumer.</li>
  <li>You're building event-sourced systems where the log of what happened is as important as current state.</li>
</ul>
<p>Kafka is the wrong tool when:</p>
<ul>
  <li>You have one producer and one consumer — RabbitMQ or Redis Streams are simpler and far easier to operate.</li>
  <li>You need request/response patterns — Kafka is one-directional. You can simulate it, but you shouldn't.</li>
  <li>Your team isn't ready to operate distributed infrastructure. Kafka is powerful and genuinely complex. A misconfigured Kafka cluster in production is a painful place to be.</li>
</ul>

<h2>The Complete Picture</h2>
<p>Kafka is an append-only, distributed, replicated log. Producers write events to topics. Topics are split into partitions for horizontal scale. Each partition has a leader and ISR followers for fault tolerance. Consumers pull events at their own pace, tracking position with offsets. Consumer groups let multiple independent services consume the same topic without interfering. Rebalancing redistributes partitions when group membership changes. Log compaction preserves the latest value per key indefinitely. Kafka Connect integrates with external systems without custom code. And the whole thing is designed around one honest tradeoff: availability and throughput over strict consistency.</p>
<p>A notice board that never erases itself, runs across a dozen owleries simultaneously, survives owlery fires without losing mail, lets every Hogwarts house read independently at their own speed, and lets you replay every notice ever posted from the day the board was installed.</p>
<p>That's Kafka.</p>

<div class="post-references">
  <p class="references-label">references</p>
  <ol>
    <li><a href="https://www.hellointerview.com/learn/system-design/deep-dives/kafka" target="_blank" rel="noopener">Kafka Deep Dive — Hello Interview (primary technical reference for this article)</a></li>
    <li><a href="https://kafka.apache.org/documentation/#gettingStarted" target="_blank" rel="noopener">Apache Kafka Documentation: Introduction — Apache Kafka Official Docs</a></li>
    <li><a href="https://kafka.apache.org/documentation/#upgrade_3300_notable" target="_blank" rel="noopener">KRaft Mode: ZooKeeper-Free Kafka — Apache Kafka 3.3 Release Notes</a></li>
    <li><a href="https://developer.confluent.io/what-is-apache-kafka/" target="_blank" rel="noopener">What is Apache Kafka? — Confluent Developer</a></li>
    <li><a href="https://www.confluent.io/blog/apache-kafka-intro-how-kafka-works/" target="_blank" rel="noopener">Apache Kafka Intro: How Kafka Works — Confluent Blog</a></li>
    <li><a href="https://kafka.apache.org/documentation/#replication" target="_blank" rel="noopener">Apache Kafka Replication and ISR — Apache Kafka Official Docs</a></li>
    <li><a href="https://www.confluent.io/blog/exactly-once-semantics-are-possible-heres-how-apache-kafka-does-it/" target="_blank" rel="noopener">Exactly-Once Semantics in Apache Kafka — Confluent Blog</a></li>
    <li><a href="https://kafka.apache.org/documentation/#log_compaction" target="_blank" rel="noopener">Log Compaction — Apache Kafka Official Docs</a></li>
  </ol>
</div>
""",
    },
    {
        "slug": "redis-simplified",
        "title": "Redis — Simplified",
        "date": "Jun 3, 2026",
        "excerpt": "Redis shows up in almost every system design conversation. Caching, rate limiting, leaderboards, pub/sub, distributed locks — it does all of it. Here's what it actually is, why it's fast, and when you should (and shouldn't) reach for it.",
        "content": """
<p>Redis gets mentioned in system design discussions constantly. Cache this. Rate limit that. Leaderboard here. Pub/sub there. It's one of those tools that seems to solve everything — which usually means it's either genuinely versatile or people are overusing it. In Redis's case, it's genuinely versatile. But understanding <em>why</em> it works the way it does makes the difference between using it well and creating subtle production problems.</p>
<p>Here's the simplified version.</p>

<h2>What Redis Actually Is</h2>
<p>Redis is an in-memory data structure store. Everything lives in RAM. There's no disk read on the hot path — when you GET a key, Redis fetches it directly from memory and returns it. That's the entire reason it's fast.</p>
<p>It's also single-threaded. One command runs at a time. No locking, no concurrency primitives, no "which thread modified this first" bugs. Operations are atomic by definition. This design choice trades theoretical parallelism for practical simplicity — and in most real workloads, you're not CPU-bound, you're network-bound. Single-threaded Redis with sub-millisecond latency almost never becomes the bottleneck.</p>
<p>The numbers: a single Redis node handles around <strong>100,000 writes per second</strong> with sub-millisecond read latency. For most applications, that's more than enough headroom.</p>

<h2>The Data Structures</h2>
<p>Redis isn't just a key-value store — it's a collection of data structures you can operate on atomically. That distinction matters. Here are the ones you'll actually use:</p>
<ul>
  <li><strong>Strings.</strong> The default. Store any value — text, JSON, serialized objects, integers. Atomic increment (INCR) works on numeric strings, which is how counters and rate limiters are built.</li>
  <li><strong>Hashes.</strong> A map within a key. Instead of serializing an entire user object to a string and deserializing it on every read, you store fields individually. Update one field without touching the rest.</li>
  <li><strong>Lists.</strong> Ordered sequences with O(1) push/pop from either end. Natural fit for queues and recent-activity feeds.</li>
  <li><strong>Sets.</strong> Unordered collections of unique values. Useful for tracking membership — "has this user seen this notification?" — with O(1) add, remove, and contains.</li>
  <li><strong>Sorted Sets.</strong> Sets where every member has a score. Members are ordered by score. O(log N) insertion and ranked lookup. This is the data structure behind every leaderboard Redis serves.</li>
  <li><strong>Streams.</strong> Append-only logs with consumer groups. Each entry gets an auto-generated ID. Consumers track their own position. Useful for event pipelines and work queues.</li>
</ul>

<h2>What Redis Is Used For</h2>

<h2>Caching</h2>
<p>The most common use case. Your database query takes 200ms. Redis has the result in under 1ms. You set a TTL (time-to-live) on the key — after that, it expires and the next request hits the database and repopulates the cache.</p>
<p>The failure mode to know: the <strong>hot key problem</strong>. If a single key gets hit by a disproportionate amount of traffic — a viral post, a trending product — all that traffic concentrates on the one Redis node holding that key. The node saturates. Solutions: cache the hot item locally on your app servers with a short TTL, or duplicate it across multiple keys and distribute reads.</p>

<h2>Rate Limiting</h2>
<p>Two approaches, each simple to implement:</p>
<ul>
  <li><strong>Fixed window.</strong> INCR a key like <code>rate:user:123:2026-08-02-14</code> (per-hour bucket). Set an EXPIRE on first increment. If the count exceeds your limit, reject the request. The key expires at the end of the window, resetting the counter automatically.</li>
  <li><strong>Sliding window.</strong> Store each request timestamp in a Sorted Set, with the timestamp as the score. To check the rate: ZREMRANGEBYSCORE to drop old entries, ZCARD to count what's left in the window, ZADD to record the current request. More accurate than fixed window, slightly more expensive.</li>
</ul>

<h2>Distributed Locks</h2>
<p>When multiple servers need to coordinate — "only one worker should process this job" — Redis provides a simple lock primitive.</p>
<p>The pattern: <code>SET lock:resource-id unique-token NX PX 5000</code>. NX means "only set if not exists." PX 5000 means "expire in 5 seconds." If the SET returns OK, you have the lock. If it returns nil, someone else does.</p>
<p>Release is the tricky part: you must only delete the key if your token matches — otherwise you might release a lock held by someone else if yours expired. This check-and-delete must be atomic, which is why it's done with a Lua script.</p>
<p>The honest caveat: Redis replication is asynchronous. A lock written to the primary might not have reached replicas before a failover. In that scenario, two workers could hold the same lock simultaneously. For workloads where that's unacceptable, use a coordination service with stronger consistency guarantees. For most practical distributed locks where losing a bit of work is acceptable, Redis is fine.</p>

<h2>Leaderboards</h2>
<p>Sorted Sets make leaderboards trivial. ZADD adds a user with their score. ZRANK gives their rank. ZRANGE with WITHSCORES returns the top N entries. All of this is O(log N). The implementation that would be painful in a relational database is a few commands in Redis.</p>

<h2>Pub/Sub</h2>
<p>Clients subscribe to channels. Publishers send messages to channels. Redis routes messages to all active subscribers in real time. Delivery is "at most once" — if a subscriber is disconnected when a message is published, it misses it. No persistence, no replay.</p>
<p>This is appropriate for real-time notifications where missing a message is acceptable and you'll get the next one soon anyway: live activity feeds, presence indicators, collaborative editing cursors. It's not appropriate for reliable event delivery where every message must be processed — use Streams with consumer groups for that.</p>

<h2>When Not to Use Redis</h2>
<p>Redis is not a database. It is not a replacement for PostgreSQL. Three specific situations where Redis is the wrong tool:</p>
<ul>
  <li><strong>You need durability.</strong> Redis's persistence options — periodic snapshots (RDB) and write logging (AOF) — both have gaps. A crash can lose acknowledged writes. If you cannot afford to lose data, Redis is not your primary store.</li>
  <li><strong>Your working set exceeds RAM.</strong> Everything in Redis lives in memory. Memory is expensive. If you're storing terabytes of data, Redis becomes cost-prohibitive as a primary store (though it can still cache a hot subset of it).</li>
  <li><strong>You need relational queries.</strong> Redis has no joins, no SQL, no cross-key aggregations unless your keys live on the same cluster node. If your access patterns are complex and relational, a database is the right tool.</li>
</ul>

<h2>Scaling Redis</h2>
<p>A single Redis node can get you surprisingly far. When you need more, Redis Cluster distributes your keyspace across multiple nodes using 16,384 hash slots. Every key maps to a slot; every slot is owned by a node. Clients cache the slot-to-node mapping and talk directly to the right node for each operation.</p>
<p>The scaling lever you control is key design. Hash tags (<code>{user:123}:posts</code> and <code>{user:123}:profile</code>) force related keys onto the same node, enabling multi-key operations on them. Keys without hash tags are distributed independently, which spreads load but prevents cross-key operations.</p>
<p>Replication in Redis Cluster is asynchronous — writes are acknowledged before replicas receive them. Fast, but with the same durability caveat as standalone Redis.</p>

<h2>The Mental Model</h2>
<p>Redis is a fast, in-memory layer that sits in front of slower systems and handles the operations those systems are bad at doing quickly: caching expensive reads, coordinating distributed processes, maintaining real-time counters and rankings, and broadcasting events.</p>
<p>It does these things extraordinarily well because it's designed around one constraint: everything stays in memory, and every operation is atomic. That constraint is also its limit. Stay within it, and Redis is one of the most reliable tools you'll use.</p>

<div class="post-references">
  <p class="references-label">references</p>
  <ol>
    <li><a href="https://www.hellointerview.com/learn/system-design/deep-dives/redis" target="_blank" rel="noopener">Redis Deep Dive — Hello Interview (the original, comprehensive version of this article)</a></li>
    <li><a href="https://redis.io/docs/latest/develop/data-types/" target="_blank" rel="noopener">Redis Data Types — Official Redis Documentation</a></li>
    <li><a href="https://redis.io/docs/latest/operate/oss_and_stack/management/scaling/" target="_blank" rel="noopener">Scale with Redis Cluster — Official Redis Documentation</a></li>
    <li><a href="https://redis.io/docs/latest/develop/data-types/sorted-sets/" target="_blank" rel="noopener">Redis Sorted Sets — Official Redis Documentation</a></li>
    <li><a href="https://redis.io/docs/latest/develop/data-types/streams/" target="_blank" rel="noopener">Redis Streams — Official Redis Documentation</a></li>
  </ol>
</div>
""",
    },
    {
        "slug": "perceptual-hashing-gpu-compute-deduplication",
        "title": "Stop Inferencing the Same Image Twice: How pHash and dHash Cut GPU Compute by Caching What's Already Known",
        "date": "May 22, 2026",
        "excerpt": "GPU inference is expensive and slow. When I realized a significant portion of images flowing through our pipeline were near-duplicates of images we'd already processed, the answer wasn't better hardware — it was a filtering layer that ran in microseconds before any model was ever called.",
        "content": """
<p>The Holmes AI pipeline processes 5,000+ support ticket images a day. Field engineers close tickets by submitting evidence — photos of installed hardware, filled checklists, device screens. Every image goes through a QC chain: preprocessing, YOLOv9 checkbox detection, and Qwen3-VL 32B semantic validation.</p>
<p>Each full inference pass costs real GPU time. Qwen3-VL 32B at 8-bit quantization is not cheap to call. We had the throughput under control — but the compute bill was higher than it should have been. When I dug into the incoming image stream, the reason became obvious.</p>
<p><strong>A lot of images were the same image.</strong></p>

<h2>The Pattern</h2>
<p>Field engineers work across many tickets in a day. For certain device types or installation categories, the checklist form is identical — same template, same layout, same printed text. Engineers photograph the same form, filled in the same way, for ticket after ticket. The images aren't byte-for-byte identical (different lighting, slight angle shifts, compression artifacts from different phone cameras), but visually, structurally, semantically — they're the same.</p>
<p>Every one of those near-identical images was going through the full pipeline independently. 5,000 images. Meaningful redundancy. Compute burned on work that had already been done.</p>
<p>The fix wasn't complicated, but it required choosing the right tool for the problem: <strong>perceptual hashing</strong>.</p>

<h2>Why Not MD5 or SHA256?</h2>
<p>The first instinct for deduplication is cryptographic hashing — MD5 or SHA256. Compute a hash of the file, store it, check if you've seen this hash before. It works perfectly for exact duplicates.</p>
<p>But exact duplicates are rare in real-world image pipelines. A photo taken of the same form from a slightly different angle, or compressed by a different phone codec, or resized before upload — those files will have completely different SHA256 hashes. Cryptographic hashes are collision-resistant by design. A single changed bit produces a completely different hash. That property is a feature for security; it's a bug for image deduplication.</p>
<p>What we needed were hashes that change <em>gradually</em> as images change — where similar images produce similar hashes, and "similar" is measurable. That's perceptual hashing.</p>

<h2>pHash: The DCT Approach</h2>
<p>pHash (perceptual hash) works on the frequency domain of an image. The algorithm is deterministic and fast<sup>[1]</sup>:</p>
<ol>
  <li>Resize the image to a fixed small size (typically 32×32).</li>
  <li>Convert to grayscale.</li>
  <li>Apply a Discrete Cosine Transform (DCT) — the same transform used in JPEG compression.</li>
  <li>Take the top-left 8×8 block of DCT coefficients, which captures the low-frequency structure (the overall shape and pattern, not fine noise).</li>
  <li>Compute the mean of those 64 values.</li>
  <li>Produce a 64-bit hash: bit <em>i</em> is 1 if coefficient <em>i</em> is above the mean, 0 otherwise.</li>
</ol>
<p>The result is a 64-bit integer that encodes the perceptual structure of the image. Images that look similar produce hashes with similar bit patterns. The distance between two pHashes — measured in Hamming distance (number of bit positions that differ) — is a reliable proxy for visual similarity.</p>
<p>A Hamming distance of 0 means identical images. A distance below 10 generally indicates near-duplicates. A distance above 20 indicates meaningfully different images. These thresholds are empirical and tunable per domain<sup>[2]</sup>.</p>
<p>pHash is robust to: JPEG compression artifacts, minor brightness and contrast adjustments, small rotations, resizing, and watermarks in low-frequency regions. It is sensitive to: cropping, significant structural edits, and high-frequency content changes (which is a feature — if the checklist structure changes, we want to detect that).</p>

<h2>dHash: The Gradient Approach</h2>
<p>dHash (difference hash) is a simpler, faster algorithm that captures edge structure rather than frequency content<sup>[3]</sup>:</p>
<ol>
  <li>Resize the image to 9×8 pixels.</li>
  <li>Convert to grayscale.</li>
  <li>For each row, compare adjacent pixel pairs: if the left pixel is brighter than the right, the bit is 1; otherwise 0.</li>
  <li>This produces 64 bits (8 rows × 8 comparisons).</li>
</ol>
<p>dHash encodes horizontal gradient structure — the pattern of brightness changes across the image. It's extremely fast (no DCT required) and good at capturing structural similarity: images with the same layout and composition produce similar dHashes even under lighting variation.</p>
<p>Where pHash and dHash differ: pHash is better at overall perceptual similarity; dHash is better at structural layout similarity. Used together, they cover different failure modes — pHash catching frequency-level similarity, dHash catching edge-pattern similarity.</p>

<h2>The Filtering Layer</h2>
<p>The implementation sits between the image ingestion step and the inference pipeline. Before any model is called:</p>
<ol>
  <li><strong>Compute both hashes.</strong> For the incoming image, compute its pHash and dHash. This takes microseconds using the <code>imagehash</code> library<sup>[4]</sup> — orders of magnitude faster than any model call.</li>
  <li><strong>Check the cache.</strong> Look up both hashes in a Redis store keyed by hash value. We store a tuple: <code>(phash, dhash)</code> as the key, the serialized inference result JSON as the value.</li>
  <li><strong>Similarity match.</strong> For each candidate in the cache (bounded lookup using hash prefix bucketing), compute Hamming distance on both hashes. If pHash distance ≤ 8 <strong>and</strong> dHash distance ≤ 6, it's a near-duplicate. Return the cached result directly.</li>
  <li><strong>Cache miss → inference.</strong> If no near-duplicate is found, run the full pipeline. Store the result in the cache with both hashes before returning.</li>
</ol>
<p>The dual-hash requirement (both pHash <em>and</em> dHash must be within threshold) reduces false positives significantly. A form photographed at a different fill level may have similar frequency content (pHash match) but different structural edges (dHash miss). Requiring both to match ensures we're only serving cached results when the image is genuinely the same document in the same state.</p>

<h2>The Output JSON Structure</h2>
<p>What gets cached is the full inference output — a structured JSON document containing:</p>
<ul>
  <li>YOLOv9 checkbox detection results: bounding boxes, confidence scores, boolean state per detected checkbox</li>
  <li>Qwen3-VL semantic validation output: per-field extracted values, anomaly flags, confidence per field</li>
  <li>Pipeline metadata: processing timestamp, model versions used, image dimensions</li>
</ul>
<p>When a near-duplicate is detected, this JSON is returned directly to the caller. From the caller's perspective, the response is identical to a fresh inference result. The cache is invisible. Only the latency is different — milliseconds instead of seconds.</p>
<p>One important design decision: we cache at the <em>inference output level</em>, not the intermediate level. Caching raw model outputs and re-running downstream logic on them would create subtle bugs if the downstream logic changed. Caching the final structured result and returning it as-is means the cache is a pure semantic cache — it says "for this image, the answer is X", not "here are some numbers to feed into your pipeline."</p>

<h2>Why Redis for the Hash Store</h2>
<p>The hash store needed to be fast (lookup on the hot path before every inference call), persistent (survive pipeline restarts), and expirable (old cache entries should expire — a form template might change). Redis with a TTL on each key was the natural fit.</p>
<p>The lookup is a single Redis GET per hash pair. The write is a single Redis SET with a TTL. Total added latency on the hot path: under 2ms. Total added latency on a cache hit: under 5ms including deserialization. Compare that to a Qwen3-VL 32B inference pass which runs in the seconds range.</p>
<p>Hash collision in Redis (two different images mapping to the same hash key) is theoretically possible but practically negligible for 64-bit perceptual hashes in a domain with bounded visual diversity. We log hash collisions for monitoring but haven't seen one cause an issue in production.</p>

<h2>The Numbers</h2>
<p>After deploying the filtering layer, we measured the duplicate rate across a week of production traffic. It settled at around <strong>15%</strong> of incoming images being near-duplicates that the pipeline had already processed — served from cache, no GPU touched.</p>
<p>15% might sound modest, but on a pipeline processing 5,000+ images a day, that's 750+ inference calls eliminated daily. Inference on Qwen3-VL 32B runs in the seconds range per image. At scale, that's real GPU time reclaimed — time that went back to the queue for the 85% of images that genuinely needed processing. GPU utilization dropped noticeably during peak hours, and P99 latency improved because the queue depth was lower.</p>
<p>More importantly: the cache hits were <em>correct</em>. We ran validation on a sample of cached responses by also running them through the full pipeline and comparing outputs. Agreement rate was 98%+. The 2% that differed were edge cases where images looked visually similar but had different fill states — which the dual-hash threshold is specifically designed to catch. In those cases, the thresholds correctly produced cache misses and routed to full inference.</p>

<h2>Threshold Tuning</h2>
<p>The right Hamming distance threshold depends on your domain. For our checklist form images:</p>
<ul>
  <li>pHash threshold of 8 (out of 64 bits): captures compression artifacts, lighting differences, minor angle shifts without over-matching forms with different content.</li>
  <li>dHash threshold of 6: captures structural layout matches without over-matching forms with different filled fields.</li>
</ul>
<p>These were tuned empirically on a labelled sample of image pairs. The right process: collect pairs of images you consider duplicates and pairs you consider distinct, sweep the threshold, measure precision and recall, pick the threshold that sits at the knee of the precision-recall curve<sup>[5]</sup>.</p>
<p>For a different domain — natural scene photos, medical images, product photographs — these numbers would be wrong. Perceptual hash thresholds are not universal. They're calibrated to the statistical distribution of your specific image corpus.</p>

<h2>What This Pattern Generalizes To</h2>
<p>The pHash/dHash caching layer is an instance of a broader pattern: <strong>compute-expensive operations on semantically stable inputs benefit from perceptual deduplication, not exact-match deduplication</strong>.</p>
<p>The same approach applies anywhere you have:</p>
<ul>
  <li>An expensive operation (GPU inference, API call, complex transformation)</li>
  <li>Inputs that are semantically equivalent but not byte-identical</li>
  <li>A meaningful repeat rate in your input stream</li>
</ul>
<p>Document OCR, image embedding generation, video frame analysis, audio transcription — all of these can benefit from perceptual deduplication upstream. The hash computation cost is negligible. The cache hit savings compound with traffic volume.</p>
<p>The insight is simple: the most expensive computation you can do is one you've already done once. If you can recognize that you've already done it, you don't have to do it again.</p>

<div class="post-references">
  <p class="references-label">references</p>
  <ol>
    <li><a href="https://www.phash.org/docs/pubs.html" target="_blank" rel="noopener">pHash: The Open Source Perceptual Hash Library — Official Documentation and Publications</a></li>
    <li><a href="https://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html" target="_blank" rel="noopener">Looks Like It — Neal Krawetz, The Hacker Factor (pHash explained)</a></li>
    <li><a href="https://www.hackerfactor.com/blog/index.php?/archives/529-Kind-of-Like-That.html" target="_blank" rel="noopener">Kind of Like That — Neal Krawetz, The Hacker Factor (dHash explained)</a></li>
    <li><a href="https://github.com/JohannesBuchner/imagehash" target="_blank" rel="noopener">imagehash — Python perceptual image hashing library (GitHub)</a></li>
    <li><a href="https://en.wikipedia.org/wiki/Precision_and_recall" target="_blank" rel="noopener">Precision and Recall — Wikipedia (threshold calibration methodology)</a></li>
    <li><a href="https://redis.io/docs/manual/keyspace-notifications/" target="_blank" rel="noopener">Redis Keyspace Notifications — Official Redis Documentation</a></li>
    <li><a href="https://en.wikipedia.org/wiki/Hamming_distance" target="_blank" rel="noopener">Hamming Distance — Wikipedia</a></li>
    <li><a href="https://pypi.org/project/imagehash/" target="_blank" rel="noopener">imagehash on PyPI — Installation and Usage Reference</a></li>
  </ol>
</div>
""",
    },
    {
        "slug": "60-percent-s3-cost-reduction-postgres-parquet",
        "title": "How I Cut S3 Storage Costs by 60% by Accident — PostgreSQL Backups, CSV, and the Parquet Revelation",
        "date": "Apr 9, 2026",
        "excerpt": "I wasn't trying to optimize anything. I was playing around with PostgreSQL backup data for an analytics side project and stumbled into a compression ratio that seemed wrong. It wasn't. Here's how an accidental benchmark turned into a 60% S3 storage cost reduction.",
        "content": """
<p>This one wasn't planned. No ticket, no objective, no cost optimization sprint. I was pulling PostgreSQL backup data into a local analytics project — just exploring, building some charts — and I happened to run the numbers on file size across formats. The result made me stop and check whether I'd made an error.</p>
<p>I hadn't. Parquet was just that much smaller.</p>

<h2>The Setup</h2>
<p>The project was simple: take some production data from a PostgreSQL backup, run analytics on it, build visualizations. The data lived in PostgreSQL. The backups were already being exported to S3 as CSV — standard practice, nothing fancy. I pulled the CSVs locally to work with them.</p>
<p>At some point during the exploration, I converted one of the CSV exports to Parquet using pandas just to see if querying would be faster. It was. But what caught my attention was the file size before I even ran a query.</p>
<p>The CSV was sitting at several hundred megabytes. The Parquet file — same data, same rows — was roughly a third of that. I ran it again on a larger table. Same story, bigger delta.</p>

<h2>The Numbers</h2>
<p>I started benchmarking more carefully across the tables I had. The compression ratio landed consistently between <strong>3x and 5x</strong> — Parquet files were 3 to 5 times smaller than their CSV equivalents for the same PostgreSQL data.</p>
<p>This isn't surprising in retrospect, but I hadn't internalized it before seeing it on my own data. Here's why the gap is that large:</p>
<ul>
  <li><strong>Columnar storage.</strong> Parquet stores data column-by-column rather than row-by-row. For analytical data, columns tend to be repetitive — status fields, category codes, date ranges. Columnar layout exposes this repetition directly to the compression algorithm.</li>
  <li><strong>Dictionary encoding.</strong> Before compression even runs, Parquet applies dictionary encoding on low-cardinality columns. A column with values like "active", "inactive", "pending" gets encoded as integers — 0, 1, 2 — before Snappy or ZSTD touches it.</li>
  <li><strong>No structural overhead per row.</strong> CSV pays a cost for every delimiter, every newline, every repeated column name implicitly encoded in position. Parquet pays schema overhead once at the file level.</li>
</ul>
<p>The VLDB 2024 paper "An Empirical Evaluation of Columnar Storage Formats"<sup>[1]</sup> formalizes this: columnar formats achieve 5–10× compression ratios typically, with low-cardinality columns reaching 20:1 or higher. My PostgreSQL data — with its status fields, merchant categories, and date columns — sat right in the middle of that range.</p>
<p>For reference: a DuckDB TPC-H benchmark at scale factor 20 showed Parquet at 3.2 GB vs CSV at 16 GB<sup>[2]</sup> — a 5× gap. Even gzip-compressed CSV remained 2–3× larger than Parquet with Snappy compression.</p>

<h2>From Curiosity to Production</h2>
<p>Once I saw the numbers, the question was obvious: why are we exporting PostgreSQL backups to S3 as CSV?</p>
<p>The answer was inertia. CSV is easy to inspect, works everywhere, requires no library to open. Those are real advantages for debugging. But for data that's being stored at scale and queried analytically, they don't outweigh the cost of keeping files 3–5× larger than they need to be.</p>
<p>Crunchy Data's work on incremental PostgreSQL-to-Parquet archival<sup>[3]</sup> confirmed the pattern: structured PostgreSQL data exported to columnar formats consistently achieves significant storage reduction without any loss of fidelity. Their recommendation was the same conclusion I'd arrived at — for analytical archival, Parquet is the right default.</p>
<p>The migration was straightforward. The export pipeline was already in Python. Swapping <code>df.to_csv()</code> for <code>df.to_parquet(compression='snappy')</code> was a one-line change. The harder part was validating that the data round-tripped correctly — row counts, nulls, type fidelity — which it did.</p>

<h2>The S3 Cost Impact</h2>
<p>S3 storage pricing is simple: you pay per GB stored. If your files are 3–5× smaller, your bill is 3–5× smaller for that data, plus reduced data transfer costs on every read.</p>
<p>In practice, the compression ratio on our specific data averaged around 3.2×, which translated to approximately <strong>60% reduction in S3 storage costs</strong> for the backup data we migrated. The number is consistent with what CloudForecast<sup>[4]</sup> and Sedai<sup>[5]</sup> report as typical for structured data migrations to Parquet: 60–80% storage reduction is the normal range.</p>
<p>There's a secondary benefit that compounds over time: Snappy-compressed Parquet is also faster to query analytically than CSV — 7–10× faster in Crunchy Data's benchmarks<sup>[3]</sup> — because columnar reads allow skipping irrelevant columns entirely. For a pipeline doing analytics on top of S3, this matters.</p>

<h2>Codec Choice</h2>
<p>One decision worth noting: compression codec. Parquet supports Snappy, GZIP, ZSTD, and LZ4. The right choice depends on your read/write pattern:</p>
<ul>
  <li><strong>Snappy</strong> — fast compression and decompression, moderate size reduction. Good default for frequently queried data.</li>
  <li><strong>ZSTD</strong> — better compression than Snappy (15–20% smaller files) with minimal performance cost<sup>[6]</sup>. Best for archival data that's read less frequently.</li>
  <li><strong>GZIP</strong> — best compression ratio, slowest. Only worth it for cold storage that's rarely touched.</li>
</ul>
<p>For backup data on S3 that's queried periodically, ZSTD is the right call. For data queried daily in hot analytical pipelines, Snappy wins on latency.</p>

<h2>The Takeaway</h2>
<p>I didn't set out to optimize S3 costs. I was playing with data for an analytics project and accidentally benchmarked two file formats side by side. The gap was large enough that it immediately changed how I thought about every CSV sitting in object storage.</p>
<p>The math is simple: if you have structured tabular data in S3 as CSV and you're not using Parquet, you're paying for 3–5× more storage than you need to. The migration is a few lines of Python. The savings compound with every GB you store and every byte you transfer.</p>
<p>Sometimes the best optimizations aren't the ones you plan — they're the ones you stumble into while doing something else entirely.</p>

<div class="post-references">
  <p class="references-label">references</p>
  <ol>
    <li><a href="https://www.vldb.org/pvldb/vol17/p148-zeng.pdf" target="_blank" rel="noopener">An Empirical Evaluation of Columnar Storage Formats — VLDB 2024, Xinyu Zeng et al.</a></li>
    <li><a href="https://aetperf.github.io/2023/03/30/TPC-H-benchmark-of-Hyper,-DuckDB-and-Datafusion-on-Parquet-files.html" target="_blank" rel="noopener">TPC-H Benchmark: Hyper, DuckDB and DataFusion on Parquet Files</a></li>
    <li><a href="https://www.crunchydata.com/blog/incremental-archival-from-postgres-to-parquet-for-analytics" target="_blank" rel="noopener">Incremental Archival from Postgres to Parquet for Analytics — Crunchy Data</a></li>
    <li><a href="https://www.cloudforecast.io/blog/using-parquet-on-athena-to-save-money-on-aws/" target="_blank" rel="noopener">Amazon Athena Cost Optimization with Apache Parquet — CloudForecast</a></li>
    <li><a href="https://sedai.io/blog/aws-s3-cost-optimization-practices" target="_blank" rel="noopener">14 Best AWS S3 Cost Optimization Strategies — Sedai</a></li>
    <li><a href="https://medium.com/dataengineeringxperts/zstd-vs-snappy-vs-gzip-the-compression-king-for-parquet-has-arrived-b4937a488b8e" target="_blank" rel="noopener">Zstd vs Snappy vs Gzip: The Compression King for Parquet Has Arrived — Medium</a></li>
    <li><a href="https://parquet.apache.org/docs/file-format/data-pages/compression/" target="_blank" rel="noopener">Apache Parquet — Official Compression Documentation</a></li>
    <li><a href="https://last9.io/blog/parquet-vs-csv/" target="_blank" rel="noopener">Parquet vs CSV: Key Differences & When to Use Each — Last9</a></li>
  </ol>
</div>
""",
    },
    {
        "slug": "blind-llm-problem-yolov9-checkbox-detection",
        "title": "The Blind LLM Problem: Why I Ditched Multimodal AI for YOLOv9 on Checkbox Detection",
        "date": "Mar 6, 2026",
        "excerpt": "LLMs are remarkably bad at knowing what they can't see. When I needed to detect ticked checkboxes on support ticket artifacts at scale, every multimodal model failed in ways that were hard to debug and impossible to trust. Here's how I diagnosed the problem and why a custom YOLOv9 model with hand-crafted training examples was the only real fix.",
        "content": """
<p>This is a story about a system that looked simple on paper and turned out to be one of the more humbling engineering problems I've worked on.</p>

<h2>The System</h2>
<p>We were building an automated QC pipeline for support ticket images. Field engineers submit evidence when closing a ticket: photos of devices, installation checklists, sign-off forms. The pipeline's job was to validate these images automatically before a ticket could be marked resolved.</p>
<p>One of the core validation requirements: <strong>detect whether specific checkboxes on a checklist form were ticked or not</strong>. A boolean signal per checkbox. Sounds trivial. It was not.</p>

<h2>First Attempt: Qwen3-VL 27B</h2>
<p>We were already running Qwen3-VL 27B (8-bit quantized) on our inference stack for other semantic validation tasks, so the natural first move was to throw the checkbox problem at it too.</p>
<p>The prompt was straightforward — here's the image, tell me which checkboxes are ticked. The model responded with confidence. It was also wrong. Consistently, structurally wrong.</p>
<p>The hallucination pattern was specific: the model would look at a partially filled form and infer checkbox state from surrounding context rather than the actual visual mark. If the text next to a checkbox said "installation complete", the model assumed it was ticked. If a checkbox was near the bottom of a crowded form, it got skipped entirely. The model was reading the document semantically and guessing — not doing pixel-level visual detection.</p>
<p>This is the blind LLM problem. The model doesn't admit it can't see something. It fills the gap with plausible inference, returns a confident answer, and you only find out it was wrong downstream. Research published in 2025 gave this a name — <em>perceptual hallucination</em>: when vision-language models generate information "as if perceived, despite absent or damaged visual evidence." The ACL 2026 DocHallu benchmark<sup>[1]</sup> found this occurs across all models, with hallucination rates higher for precise visual elements than for textual content. The vision encoder introduces the error; the language decoder amplifies it.</p>

<h2>Trying to Fix It with Prompting</h2>
<p>The next move was prompt engineering. We tried:</p>
<ul>
  <li>Explicit instructions: "do not infer checkbox state from surrounding text, only look at the visual mark inside the box"</li>
  <li>Chain-of-thought: asking the model to describe what it sees in each checkbox region before giving a boolean</li>
  <li>Coordinate-based prompting: splitting the image into regions and asking about each one individually</li>
  <li>Few-shot examples with ticked and unticked checkboxes labelled</li>
</ul>
<p>Some of these reduced the hallucination rate. None of them eliminated it. The model improved from confidently wrong to inconsistently right — which in a production QC pipeline is arguably worse, because you can't predict where it will fail.</p>
<p>This tracks with what researchers have found about spatial reasoning in VLMs. The "Mind the Gap" benchmark (2025)<sup>[2]</sup> found that models' apparent competence decreases dramatically under tasks requiring precise spatial localization — with accuracy across models approximating random chance in the hardest cases. Prompting cannot fix a representational gap: the physical world is geometric and continuous, but LLMs learn spatial concepts as discrete statistical patterns in text.</p>

<h2>Escalating to Top-Tier Models</h2>
<p>At this point the question was: is this a Qwen limitation, or is checkbox detection fundamentally hard for multimodal LLMs?</p>
<p>We ran evals against stronger models. The results were the same story at a higher confidence level.</p>
<p>It turns out this is a known, documented failure. The <strong>FormFactory benchmark (2026)</strong><sup>[3]</sup> evaluated GPT-4o, Gemini 2.5 Pro, Claude Sonnet 3.7, Qwen-VL-Max, and Grok 3 on form field detection — including checkboxes and radio buttons. <strong>No model surpassed 5% accuracy on atomic form field detection.</strong> Not a small gap. A fundamental one.</p>
<p>This isn't a capability problem. It's a training objective problem. VLMs are optimised to understand and generate language grounded in visual context. They are not trained to do precise binary spatial classification on small visual regions in low-quality document scans. As the "Vision Language Models Are Blind" paper (2025)<sup>[4]</sup> puts it bluntly: these models can describe a scene without actually seeing it.</p>
<p>The honest conclusion from our evals: no prompt, no model, no chain-of-thought was going to reliably produce a boolean from a checkbox.</p>

<h2>Switching to YOLOv9</h2>
<p>The right tool for checkbox detection is object detection. We switched to YOLOv9.</p>
<p>The approach was straightforward once the decision was made:</p>
<ol>
  <li><strong>Collect and annotate examples.</strong> We manually annotated checkbox regions from real ticket images — ticked and unticked — building a labelled dataset from the actual artifacts the system would encounter in production. Custom training data built on your own domain always outperforms a generic model on a specific task.</li>
  <li><strong>Fine-tune YOLOv9.</strong> Standard fine-tuning on our annotated dataset. The model learned to locate checkbox regions and classify each as ticked or unticked. YOLO's architecture — a unified regression framework that predicts bounding boxes and class labels in a single forward pass — is exactly suited to this: fast, local, spatially precise.</li>
  <li><strong>Output a boolean.</strong> For each detected checkbox, the model returns a confidence score and a binary state. We threshold the confidence and pass a clean boolean to the downstream pipeline. No ambiguity, no hallucination, fully auditable.</li>
  <li><strong>Plug into Holmes.</strong> The YOLOv9 output feeds directly into the same validation script that Qwen3-VL handles the semantic checks — each model doing the job it's actually good at.</li>
</ol>

<h2>Results</h2>
<p>Checkbox detection went from unreliable to production-grade. The boolean output was clean, consistent, and deterministic. The pipeline now runs both models together — YOLOv9 for spatial binary detection, Qwen3-VL for semantic content validation — covering the full QC surface across 5,000+ ticket images per day.</p>

<h2>The Takeaway</h2>
<p>LLMs are powerful and I use them heavily across production systems. But they have a failure mode that's worse than being wrong: <strong>being wrong with confidence</strong>. Checkbox detection exposed this clearly because the ground truth is binary — a box is ticked or it isn't — and the hallucinations were easy to audit.</p>
<p>The research backs this up. VLMs systematically fail at tasks that require them to count, locate, or classify small precise visual elements — not because they lack intelligence, but because that's not what they were built to do. The "Can Vision-Language Models Count?" paper (2025)<sup>[5]</sup> identified what it calls "enumerative binding failure" — models fail to count objects they can perceptually see. Every major model has a distinct failure signature: Claude under-counts, ChatGPT massively over-counts, Gemini template-hallucinates.</p>
<p>The fix wasn't a better prompt. It was choosing the right class of model for the problem. Computer vision problems need computer vision solutions. The moment we stopped trying to prompt our way around a fundamental limitation and trained a detector on our actual domain data, the problem was solved.</p>
<p>Know your tools. Know their failure modes. And when a foundation model fails at something a purpose-built model does easily, build the purpose-built model.</p>

<div class="post-references">
  <p class="references-label">references</p>
  <ol>
    <li><a href="https://aclanthology.org/2026.findings-acl.1237/" target="_blank" rel="noopener">Perceptual Hallucination in Vision–Language Models: Definition, Analysis and Verification — ACL 2026</a></li>
    <li><a href="https://arxiv.org/pdf/2503.19707" target="_blank" rel="noopener">Mind the Gap: Benchmarking Spatial Reasoning in Vision-Language Models — 2025</a></li>
    <li><a href="https://arxiv.org/html/2506.01520" target="_blank" rel="noopener">FormFactory: An Interactive Benchmarking Suite for Multimodal Form-Filling Agents — 2026</a></li>
    <li><a href="https://arxiv.org/html/2407.06581v1" target="_blank" rel="noopener">Vision Language Models Are Blind — 2025</a></li>
    <li><a href="https://arxiv.org/html/2511.17722v1" target="_blank" rel="noopener">Can Vision-Language Models Count? A Synthetic Benchmark and Analysis — 2025</a></li>
  </ol>
</div>
""",
    },
]

BLOGS_AND_VLOGS = [
    {
        "title": "Hello Interview — System Design",
        "type": "blog",
        "url": "https://www.hellointerview.com/learn/system-design/",
    },
    {
        "title": "Fireship",
        "type": "vlog",
        "url": "https://www.youtube.com/@Fireship",
    },
    {
        "title": "Theo Browne (t3.gg)",
        "type": "vlog",
        "url": "https://www.youtube.com/@t3dotgg",
    },
    {
        "title": "Arpit Bhayani",
        "type": "vlog",
        "url": "https://www.youtube.com/@AsliEngineering",
    },
    {
        "title": "NeetCode",
        "type": "vlog",
        "url": "https://www.youtube.com/@NeetCode",
    },
]

BOOKS = [
    {
        "title": "Designing Data-Intensive Applications",
        "author": "Martin Kleppmann",
    },
    {
        "title": "AI Engineering",
        "author": "Chip Huyen",
    },
    {
        "title": "System Design Interview",
        "author": "Alex Xu",
    },
]

EDUCATION = {
    "degree": "Bachelor of Engineering",
    "university": "Gujarat Technological University",
    "location": "Ahmedabad",
    "cgpa": "8.73",
    "years": "2018 – 2022",
}
