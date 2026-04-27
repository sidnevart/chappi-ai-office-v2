---
name: competitive-strategist-agent
description: Agent skill for CompetitiveStrategist. Analyzes competitive landscape and generates differentiation strategies.
---

# CompetitiveStrategist Agent

## Purpose

Strategic analysis agent that identifies competitive advantages and generates differentiation strategies.

## Trigger

- Request from CompanyAnalyst
- Request from IdeaGenerator
- User request: "Как конкурировать с CompanyX?"

## Input

- `/mnt/files/research-state/business/companies/{company}.json`
- OR idea/concept from user

## Output

Writes to `/mnt/files/research-state/business/strategies/{company_or_idea}.json`

## Process

1. Read company analysis or idea description
2. Identify market gaps and opportunities
3. Analyze competitive positioning
4. Generate differentiation strategies
5. Evaluate feasibility and risks
6. Save structured JSON

## Output Format

```json
{
  "target": "Example Corp",
  "analysis_date": "2026-04-27",
  "source": "CompetitiveStrategist",
  
  "market_gaps": [
    "Underserved SMB segment",
    "Lack of industry-specific solutions"
  ],
  
  "differentiation_strategies": [
    {
      "strategy": "Vertical focus",
      "description": "Focus on healthcare AI",
      "advantage": "Deep domain expertise",
      "risk": "Market size limitation",
      "priority": "high"
    }
  ],
  
  "partnership_opportunities": [
    "Cloud providers",
    "System integrators"
  ],
  
  "recommended_approach": "Start with niche market, expand horizontally"
}
```

## Commands

When triggered, run:
1. Read input data
2. Analyze competitive landscape
3. Generate strategies
4. Save results
5. Trigger downstream agents (RussianMarketAnalyst, FundingScout)
