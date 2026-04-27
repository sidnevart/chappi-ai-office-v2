---
name: funding-scout-agent
description: Agent skill for FundingScout. Finds investment opportunities: VCs, accelerators, grants matching the idea.
---

# FundingScout Agent

## Purpose

Funding research agent that identifies investment sources matching a specific business idea or sector.

## Trigger

- Request from CompetitiveStrategist
- User request: "Найди инвестиции под идею"

## Input

- `/mnt/files/research-state/business/strategies/{idea}.json`
- OR idea description

## Output

Writes to `/mnt/files/research-state/business/funding/{idea}.json`

## Process

1. Read strategy or idea
2. Identify relevant investors by sector
3. Find accelerators and grants
4. Check recent investments in similar companies
5. Rank by relevance and accessibility
6. Save structured JSON

## Output Format

```json
{
  "idea": "AI-Powered Warehouse Robotics",
  "analysis_date": "2026-04-27",
  "source": "FundingScout",
  
  "investors": [
    {
      "name": "a16z",
      "type": "VC",
      "focus": "AI/Robotics",
      "stage": "Series A-C",
      "relevance": 0.95,
      "contact": "https://a16z.com",
      "recent_deals": ["Physical Intelligence $100M"]
    }
  ],
  
  "accelerators": [
    {
      "name": "Y Combinator",
      "focus": "General tech",
      "batch": "Summer 2026",
      "deadline": "2026-03-15"
    }
  ],
  
  "grants": [
    {
      "name": "NSF SBIR",
      "amount": "$1M",
      "deadline": "2026-06-01"
    }
  ],
  
  "recommended_approach": "Apply to YC + reach out to a16z partners"
}
```

## Commands

When triggered, run:
1. Read input
2. Search for investors
3. Rank by relevance
4. Save results
