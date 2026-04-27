---
name: deal-flow-tracker-agent
description: Agent skill for DealFlowTracker. Runs daily to find latest funding rounds, investments, and startup deals.
---

# DealFlowTracker Agent

## Purpose

Daily research agent that tracks startup funding rounds, investments, and deal flow in AI/ML, Bioengineering, Physical AI, and related sectors.

## Trigger

- Schedule: `0 9 * * *` (daily at 09:00 Europe/Moscow)
- Target: isolated session

## Output

Writes findings to `/mnt/files/research-state/business/deals.json`

## Process

1. Search for latest funding rounds using web search
2. Focus on: AI/ML, Bioengineering, Physical AI, B2B AI-native, Robotics
3. Extract: company, amount, stage, investors, sector, date
4. Deduplicate against existing deals
5. Save structured JSON
6. Send digest to Telegram if significant deals found

## Output Format

```json
{
  "scan_date": "2026-04-27",
  "source": "DealFlowTracker",
  "deals": [
    {
      "company": "PhysicalAI Corp",
      "amount": "$50M",
      "stage": "Series A",
      "investors": ["a16z", "Sequoia"],
      "sector": "Physical AI",
      "date": "2026-04-26",
      "url": "https://example.com",
      "status": "new"
    }
  ],
  "new_count": 5,
  "total_count": 42
}
```

## Commands

When triggered, run:
1. Use `web_search` to find latest deals
2. Use `web_fetch` for detailed pages
3. Deduplicate against `/mnt/files/research-state/business/deals.json`
4. Save updated data
5. Send summary if new deals found
