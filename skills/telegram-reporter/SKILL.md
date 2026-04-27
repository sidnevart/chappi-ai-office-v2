---
name: telegram-reporter
description: Use when sending notifications to Telegram with links to reports
---

# Telegram Reporter

## Overview

Sends notifications to Telegram channel with formatted messages and links.

## When to Use

- After generating any report
- After uploading to S3
- For periodic summaries
- For error notifications

**When NOT to use:**
- Private messages → use Telegram bot directly
- File upload → use S3 + link instead
- Interactive chat → use main agent

## Configuration

```bash
# Check config
cat ~/.openclaw/openclaw.json | grep -A10 telegram

# Expected:
# tokenFile: /opt/openclaw-stack/secrets/telegram-bot-token
# chat_id: -1003891142888
```

## Message Format

### Standard Report

```
📊 Trend Monitor Report

• 2 new trends found
• Market: $26.4B

🔗 Full report: https://80.74.25.43:9000/ai-office/reports/trends-2026-04-28.html
```

### Financial Model

```
💰 Financial Model: TeamMemory AI

• LTV/CAC: 10.8x
• Payback: 3 months

📈 Google Sheets: https://docs.google.com/spreadsheets/d/.../edit
```

### Error

```
❌ Error in DealFlow Tracker

Details: Connection timeout
Retry: 5 minutes
```

## Workflow

### 1. Prepare Message

```python
message = f"""
📊 {agent_name} Report

• {metric_1}
• {metric_2}

🔗 {report_url}
"""
```

### 2. Send

```python
import requests

response = requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    data={
        "chat_id": chat_id,
        "parse_mode": "Markdown",
        "text": message,
        "disable_web_page_preview": False
    }
)
```

### 3. Verify

```python
if response.json().get("ok"):
    print("✅ Message sent")
else:
    print(f"❌ Error: {response.json()}")
```

## Icons by Report Type

| Type | Icon |
|------|------|
| Trends | 📈 |
| Deals | 💰 |
| Companies | 🏢 |
| Ideas | 💡 |
| Strategy | 📊 |
| Market | 🌍 |
| Funding | 💵 |
| Financial | 📉 |
| Pitch | 🎤 |
| Tech Spec | 📝 |
| Jobs | 💼 |
| Education | 📚 |
| Matches | 🎯 |
| Error | ❌ |
| Success | ✅ |

## Best Practices

- ✅ Always include report URL
- ✅ Use Markdown formatting
- ✅ Keep under 4000 characters
- ✅ Include key metrics in message
- ❌ Don't send raw JSON
- ❌ Don't send without link
- ❌ Don't use HTML tags (Markdown only)

## Commands

```bash
# Send report
python3 skills/telegram-reporter/send.py --agent="TrendMonitor" --url=$URL --metrics="2 trends found"

# Send error
python3 skills/telegram-reporter/send.py --error="Connection failed" --agent="DealFlow"

# Test
python3 skills/telegram-reporter/test.py
```
