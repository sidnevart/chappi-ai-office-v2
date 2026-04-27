---
name: company-analyst-agent
description: Agent skill for CompanyAnalyst. Deep-dive analysis of companies — products, subsidiaries, weaknesses, market position. Uses browser automation for dynamic content.
---

# CompanyAnalyst Agent

## Purpose

Deep-dive analysis agent that researches companies comprehensively: products, subsidiaries, market position, financials, and weaknesses.

## Trigger

- User request: "Проанализируй CompanyX"
- Cron: weekly analysis of top companies from DealFlow

## Input

- Company name
- Optional: specific focus areas

## Output

Writes to `/mnt/files/research-state/business/companies/{company_slug}.json`

## Process

1. **Web Search**: Find company website, news, Crunchbase, LinkedIn
2. **Browser Automation**: Scrape dynamic content from company site
3. **Product Analysis**: Identify product lines, features, pricing
4. **Subsidiary Mapping**: Find parent companies, acquisitions
5. **Weakness Analysis**: Identify gaps, vulnerabilities, risks
6. **Competitive Positioning**: Compare with competitors
7. **Financial Overview**: Funding, revenue, valuation
8. **Save Results**: Structured JSON

## Output Format

```json
{
  "company_name": "Example Corp",
  "slug": "example-corp",
  "analysis_date": "2026-04-27",
  "source": "CompanyAnalyst",
  
  "overview": {
    "founded": "2015",
    "headquarters": "San Francisco, CA",
    "employees": "500+",
    "website": "https://example.com",
    "industry": "AI/ML"
  },
  
  "products": [
    {
      "name": "AI Platform",
      "description": "End-to-end ML platform",
      "pricing": "Enterprise",
      "strengths": ["Easy to use", "Scalable"],
      "weaknesses": ["Limited custom models"]
    }
  ],
  
  "subsidiaries": ["SubCorp A", "SubCorp B"],
  "acquisitions": [{"company": "StartupX", "date": "2024", "amount": "$50M"}],
  
  "weaknesses": [
    "High pricing",
    "Limited enterprise features",
    "Slow support response"
  ],
  
  "competitors": [
    {"name": "CompetitorA", "strength": "Better pricing"},
    {"name": "CompetitorB", "strength": "More features"}
  ],
  
  "financials": {
    "total_funding": "$200M",
    "valuation": "$1B",
    "revenue": "$50M (est)",
    "last_round": "Series C, $100M, 2024"
  },
  
  "opportunities": [
    "Expand to Europe",
    "Add industry-specific solutions",
    "Partner with cloud providers"
  ],
  
  "risks": [
    "Market saturation",
    "Regulatory changes",
    "Talent competition"
  ]
}
```

## Commands

When triggered, run:
1. Use `web_search` for initial data
2. Use `web_fetch` for detailed pages
3. Use browser automation for dynamic sites
4. Save structured JSON
5. Trigger downstream agents (CompetitiveStrategist, RussianMarketAnalyst)
