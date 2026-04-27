---
name: russian-market-analysis
description: Use when analyzing Russian and CIS market entry
---

# Russian Market Analysis

## Overview

Analyzes Russian market and produces **HTML report** + **JSON** for pipeline.

## Output Formats

1. **JSON** (`/mnt/files/research-state/business/russian_market/*.json`) — for pipeline
2. **HTML** (`/mnt/files/research-state/reports/html/russian-market-*.html`) — human-readable
3. **S3 URL** — public access
4. **Telegram** — notification with link

## What This Skill Does NOT Produce

- ❌ Excel
- ❌ Google Sheets
- ❌ PDF

## Workflow

### Step 1: Analyze Market

Research regulations, competitors, localization.

### Step 2: Save JSON

```json
{
  "market_size_usd": 150000000,
  "regulations": [...],
  "competitors": [...]
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
</style></head>
<body>
  <h1>🇷🇺 Russian Market Analysis</h1>
  <h2>Regulations</h2>
  <table>...</table>
  <h2>Competitors</h2>
  <table>...</table>
</body>
</html>
```

### Step 4: Upload to S3

```python
s3.put_object(Bucket='ai-office', Key='reports/russian-market-team-memory-ai.html', Body=html, ContentType='text/html')
```

### Step 5: Send to Telegram

```
🇷🇺 Russian Market: $150M
3 competitors found

🔗 https://80.74.25.43:9000/ai-office/reports/russian-market-team-memory-ai.html
```

## Best Practices

- ✅ JSON for pipeline
- ✅ HTML for humans (regulation tables)
- ❌ Don't create Excel
- ❌ Don't create Google Sheets

## Commands

```bash
# Run agent
python3 skills/russian-market-analysis/analyze.py

# Generate HTML
python3 skills/html-builder/build.py --input=russian_market/*.json --output=russian-market.html

# Upload
python3 skills/s3-uploader/upload.py --file=reports/html/russian-market.html

# Send to Telegram
python3 skills/telegram-reporter/send.py --message="🇷🇺 Market" --url=$URL
```
