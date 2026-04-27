---
name: deal-flow-tracker
description: Use when tracking startup funding and investment deals
---

# Deal Flow Tracker

## Overview

Tracks startup funding rounds and produces **HTML report** + **JSON** for pipeline.

## Output Formats

1. **JSON** (`/mnt/files/research-state/business/deals.json`) — for pipeline
2. **HTML** (`/mnt/files/research-state/reports/html/deals-*.html`) — human-readable
3. **S3 URL** — public access
4. **Telegram** — notification with link

## What This Skill Does NOT Produce

- ❌ Excel (no financial modeling)
- ❌ Google Sheets (no calculations)
- ❌ PDF (HTML is sufficient)

## Workflow

### Step 1: Search Deals

Search for recent funding rounds, acquisitions.

### Step 2: Save JSON

```json
{
  "scan_date": "2026-04-28",
  "deals": [
    {
      "company": "...",
      "round": "Series A",
      "amount": "$10M",
      "lead_investor": "..."
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
  <h1>💰 Deal Flow Report</h1>
  <table>
    <tr><th>Company</th><th>Round</th><th>Amount</th><th>Lead</th></tr>
    <!-- rows -->
  </table>
</body>
</html>
```

### Step 4: Upload to S3

```python
s3.put_object(Bucket='ai-office', Key='reports/deals-2026-04-28.html', Body=html, ContentType='text/html')
```

### Step 5: Send to Telegram

```
💰 Deal Flow: 3 new deals found
Total value: $50M

🔗 https://80.74.25.43:9000/ai-office/reports/deals-2026-04-28.html
```

## Best Practices

- ✅ JSON for pipeline
- ✅ HTML for humans (deal tables)
- ❌ Don't create Excel (no calculations)
- ❌ Don't create Google Sheets

## Commands

```bash
# Run agent
python3 skills/deal-flow-tracker/track.py

# Generate HTML
python3 skills/html-builder/build.py --input=deals.json --output=deals.html

# Upload
python3 skills/s3-uploader/upload.py --file=reports/html/deals.html

# Send to Telegram
python3 skills/telegram-reporter/send.py --message="💰 Deals" --url=$URL
```
