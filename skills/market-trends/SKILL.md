---
name: market-trends
description: |
  Monitor and analyze market trends: Physical AI, Bioengineering, B2B AI-native, Crypto.
  Use when: (1) Daily cron for trend monitoring, (2) User asks about market trends,
  (3) Need trend analysis for strategy, (4) Update knowledge base.
  
  Agent: TrendMonitor
  Schedule: 0 8 * * * (daily 08:00 MSK)
  Output: HTML digest + Telegram message + knowledge base update
  Hashtags: #business #тренды #рынок #AI #crypto
---

# MarketTrends Skill

## Workflow

1. **web_search**: Find latest trends in target sectors
2. **deep_research**: Analyze trend strength, adoption, key players
3. **Store in memory**: Save to local-vector-db with category "business_trends"
4. **Generate digest**: HTML + Telegram format

## Trend Categories

| Category | Search Terms |
|----------|-------------|
| Physical AI | "physical AI robotics 2026", "embodied intelligence" |
| Bioengineering | "synthetic biology trends 2026", "biohacking" |
| B2B AI-native | "AI-native SaaS", "vertical AI" |
| Crypto | "DeFi trends 2026", "blockchain funding" |

## Output Format

```json
{
  "trends": [
    {
      "category": "Physical AI",
      "headline": "Humanoid robots enter warehouses",
      "source": "The Information",
      "strength": "strong",
      "key_players": ["Figure AI", "Tesla Optimus"],
      "date": "2026-04-27"
    }
  ]
}
```

## Memory Storage

- entity_type: "trend"
- tags: "business,trends,{sector}"
