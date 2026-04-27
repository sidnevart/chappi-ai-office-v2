---
name: weekly-matcher
description: Use when matching CV with opportunities
---

# Weekly Matcher

## Overview

Matches CVs and produces **HTML report** + **JSON** for pipeline.

## Output Formats

1. **JSON** (`/mnt/files/research-state/edu/matched_opportunities.json`) — for pipeline
2. **HTML** (`/mnt/files/research-state/reports/html/matches-*.html`) — human-readable
3. **S3 URL** — public access
4. **Telegram** — notification with link

## What This Skill Does NOT Produce

- ❌ Excel (no financial data)
- ❌ Google Sheets
- ❌ PDF

## Workflow

### Step 1: Match CV

Read CV + opportunities → calculate scores.

### Step 2: Save JSON

```json
{
  "matches": [
    {
      "opportunity": "AI Developer",
      "score": 0.92,
      "type": "job"
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
  .high-score { color: #4caf50; font-weight: bold; }
</style></head>
<body>
  <h1>🎯 Weekly Matches</h1>
  <table>
    <tr><th>Opportunity</th><th>Score</th><th>Type</th></tr>
    <!-- rows -->
  </table>
</body>
</html>
```

### Step 4: Upload to S3

```python
s3.put_object(Bucket='ai-office', Key='reports/matches-2026-04-28.html', Body=html, ContentType='text/html')
```

### Step 5: Send to Telegram

```
🎯 Matches: 3 found
AI Developer (92%), Backend (90%)

🔗 https://80.74.25.43:9000/ai-office/reports/matches-2026-04-28.html
```

## Best Practices

- ✅ JSON for pipeline
- ✅ HTML for humans (score tables)
- ❌ Don't create Excel
- ❌ Don't create Google Sheets

## Commands

```bash
# Run agent
python3 skills/weekly-matcher/match.py

# Generate HTML
python3 skills/html-builder/build.py --input=edu/matched_opportunities.json --output=matches.html

# Upload
python3 skills/s3-uploader/upload.py --file=reports/html/matches.html

# Send to Telegram
python3 skills/telegram-reporter/send.py --message="🎯 Matches" --url=$URL
```
