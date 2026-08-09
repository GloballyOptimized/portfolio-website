QUERY_GEN_PROMPT = """You are a market research query strategist.

Given a market research question, generate exactly {n} distinct web search queries that together provide comprehensive market intelligence.

Cover these angles (spread across the queries):
- Market size and valuation (current year and historical)
- Market growth rate (CAGR)
- Key companies and market share
- Recent news and developments (last 12 months)
- Industry trends and drivers
- Challenges and headwinds
- Consumer/demand behaviour
- Regulatory environment
- Geographic breakdown (if applicable)
- Competitive landscape
- Investment and funding activity
- Technology and innovation

Rules:
- Each query must be specific and searchable (as if typed into Google)
- Include the year (2024 or 2025) in at least 5 queries
- Vary phrasing — no two queries should be near-identical
- Output ONLY a valid JSON array of strings. No markdown fences, no explanation, no preamble. Start with [ and end with ].

Example — if the question were "how is the paint industry in India":
[
  "India paint industry market size 2024",
  "India decorative paint market CAGR 2024 2029",
  "Asian Paints Berger Paints Kansai Nerolac market share 2024",
  "India paint industry revenue growth 2025",
  "Indian paint sector challenges raw material costs 2024",
  "decorative vs industrial paint demand India 2024",
  "India paint market consumer trends urbanisation",
  "paint industry India regulatory environment BIS standards",
  "Asian Paints Q3 Q4 results 2024 revenue profit",
  "Berger Paints India annual report 2024",
  "India paint industry new entrants competition 2024",
  "water-based paint demand India environment regulations",
  "India real estate construction impact paint industry 2025",
  "paint industry India export import data 2024",
  "India paint market rural urban split demand 2024",
  "Indigo Paints JSW Paints market expansion India",
  "India paint industry private equity investment 2024",
  "nano coatings smart paints technology India 2025",
  "India paint market post-COVID recovery growth drivers",
  "India paint industry outlook forecast 2025 2030"
]
"""


SYNTHESIS_PROMPT = """You are a senior market research analyst at a top-tier consultancy.

Below are web search snippets collected from {n_queries} search queries about the following market question:
"{question}"

Total snippets collected: {n_results}

Synthesise these into a structured market analysis JSON. Be factual — only include claims supported by the snippets. If data is unclear or missing, say so honestly. Do not fabricate numbers.

Output ONLY valid JSON. No markdown fences, no explanation, no preamble. Start with {{ and end with }}.

Required structure (copy this exactly, fill every field):
{{
  "headline": "India's paint market is a ₹75,000 Cr industry growing at 12% CAGR, led by Asian Paints with 40% market share.",
  "overview": "The Indian decorative paint market reached approximately ₹65,000–75,000 crore in FY2024, driven by rapid urbanisation, rising disposable incomes, and a booming real estate sector. Decorative paints account for nearly 75% of total volumes, with the industrial segment making up the rest.\\n\\nAsian Paints commands roughly 40% market share, followed by Berger Paints (~20%), Kansai Nerolac (~12%), and AkzoNobel India (~8%). Smaller players like Indigo Paints and JSW Paints have been aggressively expanding in Tier-2 and Tier-3 cities.\\n\\nRaw material costs — primarily titanium dioxide and crude-oil-derived inputs — remain the biggest margin pressure. Players have offset this through price hikes and premiumisation toward emulsions and luxury finishes.",
  "market_size": {{
    "current": "₹75,000 Cr (~$9 billion) FY2024",
    "growth": "CAGR 12–14% (2024–2029)",
    "note": "Estimates vary across sources; industrial segment excluded from some figures"
  }},
  "key_players": [
    {{"name": "Asian Paints", "detail": "Market leader, ~40% share, strong rural distribution"}},
    {{"name": "Berger Paints", "detail": "~20% share, aggressive premiumisation push"}},
    {{"name": "Kansai Nerolac", "detail": "~12% share, strong in industrial coatings"}},
    {{"name": "AkzoNobel India", "detail": "~8% share, focused on premium decorative"}},
    {{"name": "Indigo Paints", "detail": "Fast-growing challenger, strong in South India"}}
  ],
  "trends": [
    "Shift from distemper to premium emulsions in Tier-2/3 cities",
    "Water-based and low-VOC paints gaining share on regulatory push",
    "Digital colour visualisation tools driving consumer engagement",
    "Home renovation boom post-pandemic sustaining decorative demand",
    "Premiumisation — luxury and texture finishes growing 18%+ YoY"
  ],
  "challenges": [
    "Crude oil and titanium dioxide price volatility squeezing margins",
    "Intense competition from regional and unorganised players on price",
    "Longer repainting cycles in economic downturns reduce volume",
    "Regulatory tightening on solvent-based products requires reformulation capex"
  ],
  "opportunities": [
    "Underpenetrated rural market with rising incomes and electrification",
    "Construction pipeline of 10M+ affordable housing units through 2026",
    "Export opportunity in Southeast Asia and Africa for mid-tier brands",
    "Anti-microbial and functional coatings for healthcare and infrastructure"
  ],
  "outlook": "The Indian paint market is on a structural growth trajectory underpinned by housing demand, urban migration, and rising aspiration. Asian Paints and Berger are best positioned to capture premiumisation, while JSW Paints and Indigo represent credible volume challengers. Margins will remain under pressure from raw materials in the near term, but should recover as oil prices stabilise. The sector is likely to sustain 12–14% volume CAGR through 2029.",
  "confidence": "high",
  "sources": [
    {{"title": "Asian Paints Q3 FY2024 Investor Presentation", "url": "https://www.asianpaints.com/investor-relations"}},
    {{"title": "CRISIL Report: India Paint Industry Outlook 2024", "url": "https://www.crisil.com/reports/paint-industry-2024"}}
  ]
}}

Confidence guide: high = multiple sources confirm the claim; medium = limited or partially corroborating sources; low = single source or conflicting data.
"""


def build_query_gen_messages(question: str, n: int) -> list[dict]:
    return [{"role": "user", "parts": [{"text": QUERY_GEN_PROMPT.format(n=n) + f"\n\nQuestion: {question}"}]}]


def build_synthesis_messages(question: str, queries: list[str],
                             results_map: dict[str, list[dict]]) -> list[dict]:
    snippets_text = ""
    for i, query in enumerate(queries, 1):
        results = results_map.get(query, [])
        snippets_text += f"\n\n--- Query {i}: {query} ---\n"
        if not results:
            snippets_text += "(no results)\n"
        for j, r in enumerate(results, 1):
            snippets_text += f"\n[{i}.{j}] {r['title']}\n{r['url']}\n{r['snippet']}\n"

    n_results = sum(len(v) for v in results_map.values())
    prompt = SYNTHESIS_PROMPT.format(
        n_queries=len(queries),
        question=question,
        n_results=n_results,
    ) + f"\n\n--- SEARCH SNIPPETS ---{snippets_text}"

    return [{"role": "user", "parts": [{"text": prompt}]}]
