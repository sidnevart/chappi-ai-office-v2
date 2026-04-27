---
name: deal_flow_tracker
description: |
  Track funding deals, investments, and startup rounds. 
  Use when: (1) Daily cron at 09:00 to find new deals, (2) User asks "what deals today", 
  (3) Need to update knowledge base with deal flow data, (4) Generate business digest for Telegram.
  
  Agent: DealFlowTracker
  Schedule: 0 9 * * * (daily 09:00 MSK)
  Output: HTML digest + Telegram message + knowledge base update
  Hashtags: #business #deals #инвестиции #AI #стартап
---

# DealFlowTracker Skill

## Workflow

1. **web_search**: Find recent funding rounds (seed, series A/B/C, mega rounds)
2. **deep_research**: Analyze each deal (company, amount, investors, sector)
3. **Store in memory**: Save to MEM0 with category "business_deals"
4. **Generate digest**: HTML + Telegram format
5. **Send to Telegram**: Via TELEGRAM_SEND_MESSAGE to @chappi_ai_office_digest

## Search Queries

- "startup funding round {date} seed series A"
- "venture capital investment {date}"
- "Y Combinator batch companies funding"
- "AI startup funding {date}"
- "mega round billion funding {date}"

## Output Format

```json
{
  "deals": [
    {
      "company": "CompanyName",
      "amount": "$10M",
      "round": "Series A",
      "field": "AI/ML",
      "location": "San Francisco",
      "date": "2026-04-27",
      "source": "TechCrunch",
      "url": "https://..."
    }
  ],
  "summary": {
    "total_count": 5,
    "total_amount": "$500M+",
    "ai_percentage": 80
  }
}
```

## Telegram Message Template

```
🎯 [#AI_OFFICE_DIGEST] | #business #deals

📅 {date}
🤖 Агент: DealFlowTracker

━━━━━━━━━━━━━━━━━━━━━━

📊 Обзор:
• Сделок: {total_count}
• Общая сумма: {total_amount}
• AI-related: {ai_percentage}%

🔥 Топ сделки:

{deal_list}

━━━━━━━━━━━━━━━━━━━━━━

#business #deals #инвестиции #AI #стартап #openclaw
```

## Memory Storage

Store each deal in MEM0:
- user_id: "ai_office"
- categories: ["business", "deals", "funding"]
- metadata: {date, company, amount, sector}

## Cron Configuration

```json
{
  "name": "business_deal_flow_tracker",
  "schedule": "0 9 * * *",
  "timezone": "Europe/Moscow",
  "agent": "DealFlowTracker"
}
```
