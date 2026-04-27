---
name: edu-competition-scout
description: Use when searching for competitions and hackathons
---

# Edu Competition Scout

## Overview

Finds competitions and produces **HTML report** + **JSON** for pipeline.

## Output Formats

1. **JSON** (`/mnt/files/research-state/edu/competitions.json`) — for pipeline
2. **HTML** (`/mnt/files/research-state/reports/html/competitions-*.html`) — human-readable
3. **S3 URL** — public access
4. **Telegram** — notification with link

## What This Skill Does NOT Produce

- ❌ Excel (no financial data)
- ❌ Google Sheets
- ❌ PDF

## Workflow

### Step 1: Search Competitions

Search for competitions by topic, type.

### Step 2: Save JSON

```json
{
  "competitions": [
    {
      "name": "Yandex Cup 2026",
      "type": "hackathon",
      "prize": "$10K"
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
  <h1>🏆 Competitions</h1>
  <table>
    <tr><th>Name</th><th>Type</th><th>Prize</th></tr>
    <!-- rows -->
  </table>
</body>
</html>
```

### Step 4: Upload to S3

```python
s3.put_object(Bucket='ai-office', Key='reports/competitions-2026-04-28.html', Body=html, ContentType='text/html')
```

### Step 5: Send to Telegram

```
🏆 Competitions: 2 found
Yandex Cup, ICSC

🔗 https://80.74.25.43:9000/ai-office/reports/competitions-2026-04-28.html
```

## Best Practices

- ✅ JSON for pipeline
- ✅ HTML for humans (competition tables)
- ❌ Don't create Excel
- ❌ Don't create Google Sheets

## Commands

```bash
# Run agent
python3 skills/edu-competition-scout/search.py

# Generate HTML
python3 skills/html-builder/build.py --input=edu/competitions.json --output=competitions.html

# Upload
python3 skills/s3-uploader/upload.py --file=reports/html/competitions.html

# Send to Telegram
python3 skills/telegram-reporter/send.py --message="🏆 Competitions" --url=$URL
```
