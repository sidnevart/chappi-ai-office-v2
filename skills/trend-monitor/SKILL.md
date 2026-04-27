---
name: trend-monitor
description: Use when monitoring market trends in AI and emerging technologies
---

# Trend Monitor

## Overview

Monitors trends and produces **HTML report** (human-readable) + **JSON** (for pipeline).

## Output Formats

1. **JSON** (`/mnt/files/research-state/business/trends.json`) — for pipeline
2. **HTML** (`/mnt/files/research-state/reports/html/trends-*.html`) — human-readable
3. **S3 URL** — public access to HTML
4. **Telegram** — notification with HTML link

## Workflow

### Step 1: Search Trends

Web search for recent developments in AI, bioengineering, etc.

### Step 2: Save JSON (for pipeline)

```json
{
  "scan_date": "2026-04-28",
  "trends": [
    {
      "trend": "Physical AI",
      "description": "Robots with human-like dexterity",
      "confidence": 0.9,
      "sources": ["TechCrunch"]
    }
  ]
}
```

### Step 3: Generate HTML Report

```html
<!DOCTYPE html>
<html>
<head><style>
  body { font-family: Arial; max-width: 900px; margin: 0 auto; padding: 40px; }
  h1 { color: #1a237e; }
  table { width: 100%; border-collapse: collapse; }
  th { background: #667eea; color: white; padding: 12px; }
  td { padding: 10px; border-bottom: 1px solid #ddd; }
  .metric { display: inline-block; padding: 15px; background: #f0f4ff; border-radius: 8px; }
</style></head>
<body>
  <h1>📈 AI Trends Report</h1>
  <table>
    <tr><th>Trend</th><th>Confidence</th><th>Impact</th></tr>
    <!-- rows from JSON -->
  </table>
</body>
</html>
```

### Step 4: Upload HTML to S3

```python
s3.put_object(Bucket='ai-office', Key='reports/trends-2026-04-28.html', Body=html, ContentType='text/html')
```

### Step 5: Send to Telegram

```
📈 Trend Monitor: 2 new trends found

🔗 https://80.74.25.43:9000/ai-office/reports/trends-2026-04-28.html
```

## Best Practices

- ✅ JSON for pipeline (other agents read it)
- ✅ HTML for humans (tables, metrics)
- ✅ S3 for sharing
- ❌ Don't create Excel (no financial data)
- ❌ Don't create Google Sheets (no calculations)

## Commands

```bash
# Run agent
python3 skills/trend-monitor/monitor.py

# Generate HTML from JSON
python3 skills/html-builder/build.py --input=trends.json --output=trends.html

# Upload to S3
python3 skills/s3-uploader/upload.py --file=reports/html/trends.html

# Send to Telegram
python3 skills/telegram-reporter/send.py --message="📈 Trends" --url=$URL
```
