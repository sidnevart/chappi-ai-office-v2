---
name: trend-monitor-agent
description: Agent skill for TrendMonitor. Runs daily to track emerging trends in AI, Bioengineering, Physical AI, B2B AI-native, and Crypto sectors.
---

# TrendMonitor Agent

## Purpose

Daily research agent that tracks and analyzes emerging technology trends in AI/ML, Bioengineering, Physical AI, B2B AI-native, and related sectors.

## Trigger

- Schedule: `0 8 * * *` (daily at 08:00 Europe/Moscow)
- Target: isolated session

## Output

Writes findings to `/mnt/files/research-state/business/trends.json`

## Process

1. Search for trending topics using web search
2. Focus areas: Physical AI, Bioengineering, B2B AI-native, AI infrastructure, Robotics
3. Analyze: news articles, research papers, funding data, social signals
4. Identify: emerging patterns, breakout companies, technology shifts
5. Save structured JSON with trend analysis

## Output Format

```json
{
  "scan_date": "2026-04-27",
  "source": "TrendMonitor",
  "trends": [
    {
      "name": "Physical AI Robotics",
      "sector": "Physical AI",
      "momentum": "rising",
      "signals": [
        {"type": "funding", "source": "$200M round in Figure AI", "date": "2026-04-25"},
        {"type": "research", "source": "New paper on embodied AI", "date": "2026-04-20"}
      ],
      "companies": ["Figure AI", "Physical Intelligence", "Skild AI"],
      "description": "AI systems that interact with physical world through robotics",
      "confidence": 0.85
    }
  ],
  "rising_count": 3,
  "total_count": 12
}
```

## Commands

When triggered, run:
1. Use `web_search` for trend data
2. Use `web_fetch` for detailed analysis
3. Save to `/mnt/files/research-state/business/trends.json`
4. Send digest to Telegram
