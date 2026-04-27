---
name: funding-scout
description: Use when searching for investors and funding opportunities
---

# Funding Scout

## Overview

Finds investors and produces **HTML report** + **JSON** for pipeline.

## Output Formats

1. **JSON** (`/mnt/files/research-state/business/funding/*.json`) — for pipeline
2. **HTML** (`/mnt/files/research-state/reports/html/funding-*.html`) — human-readable
3. **S3 URL** — public access
4. **Telegram** — notification with link

## What This Skill Does NOT Produce

- ❌ Excel (no financial modeling)
- ❌ Google Sheets (irrelevant)
- ❌ PDF

## Workflow

### Step 1: Search Investors

Search by stage, sector, geography.

### Step 2: Save JSON

```json
{
  "investors": [...],
  "accelerators": [...],
  "grants": [...]
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
  <h1>💰 Funding Landscape</h1>
  <h2>Investors</h2>
  <table>...</table>
  <h2>Accelerators</h2>
  <table>...</table>
</body>
</html>
```

### Step 4: Upload to S3

```python
s3.put_object(Bucket='ai-office', Key='reports/funding-team-memory-ai.html', Body=html, ContentType='text/html')
```

### Step 5: Send to Telegram

```
💰 Funding: 4 investors found
Runa Capital, Altair, Сколково, YC

🔗 https://80.74.25.43:9000/ai-office/reports/funding-team-memory-ai.html
```

## Best Practices

- ✅ JSON for pipeline
- ✅ HTML for humans (investor tables)
- ❌ Don't create Excel
- ❌ Don't create Google Sheets

## Commands

```bash
# Run agent
python3 skills/funding-scout/search.py

# Generate HTML
python3 skills/html-builder/build.py --input=funding/*.json --output=funding.html

# Upload
python3 skills/s3-uploader/upload.py --file=reports/html/funding.html

# Send to Telegram
python3 skills/telegram-reporter/send.py --message="💰 Funding" --url=$URL
```
