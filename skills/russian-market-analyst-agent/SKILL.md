---
name: russian-market-analyst-agent
description: Agent skill for RussianMarketAnalyst. Analyzes Russian market opportunities, regulations, and entry strategies.
---

# RussianMarketAnalyst Agent

## Purpose

Market analysis agent specializing in Russian market: opportunities, regulations, competition, and entry strategies.

## Trigger

- Request from CompetitiveStrategist
- User request: "Как выйти на рынок РФ?"

## Input

- `/mnt/files/research-state/business/strategies/{idea}.json`
- OR product/idea description

## Output

Writes to `/mnt/files/research-state/business/russian_market/{idea}.json`

## Process

1. Read strategy or idea
2. Research Russian market regulations
3. Identify local competitors
4. Analyze market size and demand
5. Evaluate entry barriers
6. Recommend localization strategy
7. Save structured JSON

## Output Format

```json
{
  "idea": "AI-Powered Warehouse Robotics",
  "analysis_date": "2026-04-27",
  "source": "RussianMarketAnalyst",
  
  "market_overview": {
    "size": "$2B (est)",
    "growth_rate": "15% YoY",
    "key_players": ["Yandex Robotics", "Skolkovo startups"]
  },
  
  "regulations": [
    "Data localization requirements",
    "Import restrictions on certain tech"
  ],
  
  "competition": [
    {"name": "Yandex Robotics", "strength": "Local knowledge"},
    {"name": "Local integrators", "strength": "Customer relationships"}
  ],
  
  "opportunities": [
    "Growing e-commerce logistics",
    "Government support for AI"
  ],
  
  "barriers": [
    "Currency volatility",
    "Sanctions impact",
    "Local certification"
  ],
  
  "entry_strategy": "Partner with local integrator",
  "timeline": "6-12 months"
}
```

## Commands

When triggered, run:
1. Read input
2. Research Russian market
3. Analyze competition
4. Save results
