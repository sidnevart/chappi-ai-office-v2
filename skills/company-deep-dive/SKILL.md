---
name: company-deep-dive
description: Use when analyzing companies and competitive landscape
---

# Company Deep Dive

## Overview

Analyzes companies and produces **HTML report** + **JSON** for pipeline.

## Output Formats

1. **JSON** (`/mnt/files/research-state/business/companies/*.json`) — for pipeline
2. **HTML** (`/mnt/files/research-state/reports/html/companies/*.html`) — human-readable
3. **S3 URL** — public access
4. **Telegram** — notification with link

## What This Skill Does NOT Produce

- ❌ Excel (no financial modeling)
- ❌ Google Sheets
- ❌ PDF (HTML sufficient)

## Workflow

### Step 1: Analyze Company

Research products, weaknesses, competitors.

### Step 2: Save JSON

```json
{
  "company": "OpenAI",
  "products": [...],
  "weaknesses": [...],
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
  <h1>🏢 Company Analysis: OpenAI</h1>
  <h2>Products</h2>
  <table>...</table>
  <h2>Competitors</h2>
  <table>...</table>
</body>
</html>
```

### Step 4: Upload to S3

```python
s3.put_object(Bucket='ai-office', Key='reports/companies/openai.html', Body=html, ContentType='text/html')
```

### Step 5: Send to Telegram

```
🏢 Company Analysis: OpenAI
3 products, 5 weaknesses found

🔗 https://80.74.25.43:9000/ai-office/reports/companies/openai.html
```

## Best Practices

- ✅ JSON for pipeline
- ✅ HTML for humans (comparison tables)
- ❌ Don't create Excel
- ❌ Don't create Google Sheets

## Commands

```bash
# Run agent
python3 skills/company-deep-dive/analyze.py --company=OpenAI

# Generate HTML
python3 skills/html-builder/build.py --input=companies/openai.json --output=companies/openai.html

# Upload
python3 skills/s3-uploader/upload.py --file=reports/html/companies/openai.html

# Send to Telegram
python3 skills/telegram-reporter/send.py --message="🏢 Company" --url=$URL
```
