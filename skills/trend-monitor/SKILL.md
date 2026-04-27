---
name: trend_monitor
description: |
  Monitor market trends: Physical AI, Bioengineering, B2B AI-native, Crypto.
  Use when: (1) Daily cron at 08:00, (2) User asks about trends, 
  (3) Need trend analysis for business strategy, (4) Update knowledge base with trend data.
  
  Agent: TrendMonitor
  Schedule: 0 8 * * * (daily 08:00 MSK)
  Output: HTML digest + Telegram message + knowledge base update
  Hashtags: #business #тренды #AI #crypto #bioengineering
---

# TrendMonitor Skill

## Workflow

1. **web_search**: Find latest trends in target sectors
2. **deep_research**: Analyze trend strength, adoption, key players
3. **Store in memory**: Save to MEM0 with category "business_trends"
4. **Generate digest**: HTML + Telegram format
5. **Send to Telegram**: Via TELEGRAM_SEND_MESSAGE

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

- user_id: "ai_office"
- categories: ["business", "trends", "{sector}"]
- metadata: {date, sector, strength, source}
