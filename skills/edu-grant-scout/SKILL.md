---
name: edu-grant-scout
description: Use when searching for grants and scholarships
---

# Edu Grant Scout

## Overview

Finds grants and produces **HTML report** + **JSON** for pipeline.

## Output Formats

1. **JSON** (`/mnt/files/research-state/edu/grants.json`) — for pipeline
2. **HTML** (`/mnt/files/research-state/reports/html/grants-*.html`) — human-readable
3. **S3 URL** — public access
4. **Telegram** — notification with link

## What This Skill Does NOT Produce

- ❌ Excel (no financial data)
- ❌ Google Sheets
- ❌ PDF

## Workflow

### Step 1: Search Grants

Search for grants by topic, eligibility.

### Step 2: Save JSON

```json
{
  "grants": [
    {
      "name": "Сколково",
      "amount": "25M ₽",
      "deadline": "2026-05-01"
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
</style></head>
<body>
  <h1>🎓 Grants & Scholarships</h1>
  <table>
    <tr><th>Name</th><th>Amount</th><th>Deadline</th></tr>
    <!-- rows -->
  </table>
</body>
</html>
```

### Step 4: Upload to S3

```python
s3.put_object(Bucket='ai-office', Key='reports/grants-2026-04-28.html', Body=html, ContentType='text/html')
```

### Step 5: Send to Telegram

```
🎓 Grants: 2 found
Сколково, NSU

🔗 https://80.74.25.43:9000/ai-office/reports/grants-2026-04-28.html
```

## Best Practices

- ✅ JSON for pipeline
- ✅ HTML for humans (grant tables)
- ❌ Don't create Excel
- ❌ Don't create Google Sheets

## Commands

```bash
# Run agent
python3 skills/edu-grant-scout/search.py

# Generate HTML
python3 skills/html-builder/build.py --input=edu/grants.json --output=grants.html

# Upload
python3 skills/s3-uploader/upload.py --file=reports/html/grants.html

# Send to Telegram
python3 skills/telegram-reporter/send.py --message="🎓 Grants" --url=$URL
```
