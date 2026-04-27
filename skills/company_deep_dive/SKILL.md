---
name: company_deep_dive
description: |
  Deep analysis of companies: products, subsidiaries, weaknesses, opportunities.
  Use when: (1) User asks "analyze CompanyX", (2) Need competitive intelligence,
  (3) Preparing for investment or partnership, (4) Building competitive strategy.
  
  Agent: CompanyAnalyst
  Trigger: User request or cron (top from DealFlow)
  Output: JSON profile + HTML report + Telegram summary
  Hashtags: #business #анализ #компания #конкуренты
---

# CompanyDeepDive Skill

## Workflow

1. **web_search**: Find company info (website, Crunchbase, news)
2. **browser_automation**: Scrape detailed data if needed
3. **deep_research**: Analyze products, team, funding, market position
4. **Store in memory**: Save to local-vector-db as "company"
5. **Generate report**: JSON profile + HTML report

## Analysis Framework

| Area | What to analyze |
|------|----------------|
| Products | Main products, features, pricing |
| Team | Founders, key hires, culture |
| Funding | Investors, rounds, valuation |
| Market | TAM, SAM, SOM, growth |
| Weaknesses | Gaps, vulnerabilities |
| Opportunities | Expansion, partnerships |

## Output Format

```json
{
  "company": "CompanyX",
  "profile": {
    "founded": "2022",
    "location": "San Francisco",
    "employees": "50-200",
    "funding": "$50M Series B",
    "valuation": "$200M"
  },
  "products": [
    {"name": "Product A", "category": "SaaS", "pricing": "$99/mo"}
  ],
  "competitors": ["Competitor1", "Competitor2"],
  "weaknesses": ["Limited market", "High churn"],
  "opportunities": ["Enterprise segment", "International"]
}
```

## Memory Storage

- entity_type: "company"
- tags: "business,companies,deep-dive"
