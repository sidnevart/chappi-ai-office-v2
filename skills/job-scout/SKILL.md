---
name: job-scout
description: Use when searching for job opportunities
---

# Job Scout

## Overview

Finds jobs and produces **HTML report** + **JSON** for pipeline.

## Output Formats

1. **JSON** (`/mnt/files/research-state/career/jobs.json`) — for pipeline
2. **HTML** (`/mnt/files/research-state/reports/html/jobs-*.html`) — human-readable
3. **S3 URL** — public access
4. **Telegram** — notification with link

## What This Skill Does NOT Produce

- ❌ Excel (no financial data)
- ❌ Google Sheets
- ❌ PDF

## Workflow

### Step 1: Search Jobs

Search for jobs by role, location.

### Step 2: Save JSON

```json
{
  "jobs": [
    {
      "title": "AI Developer",
      "company": "...",
      "location": "London",
      "salary": "$100K"
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
  <h1>💼 Job Listings</h1>
  <table>
    <tr><th>Title</th><th>Company</th><th>Location</th><th>Salary</th></tr>
    <!-- rows -->
  </table>
</body>
</html>
```

### Step 4: Upload to S3

```python
s3.put_object(Bucket='ai-office', Key='reports/jobs-2026-04-28.html', Body=html, ContentType='text/html')
```

### Step 5: Send to Telegram

```
💼 Job Scout: 3 jobs found
AI Developer, Backend, DevOps

🔗 https://80.74.25.43:9000/ai-office/reports/jobs-2026-04-28.html
```

## Best Practices

- ✅ JSON for pipeline
- ✅ HTML for humans (job tables)
- ❌ Don't create Excel
- ❌ Don't create Google Sheets

## Commands

```bash
# Run agent
python3 skills/job-scout/search.py

# Generate HTML
python3 skills/html-builder/build.py --input=career/jobs.json --output=jobs.html

# Upload
python3 skills/s3-uploader/upload.py --file=reports/html/jobs.html

# Send to Telegram
python3 skills/telegram-reporter/send.py --message="💼 Jobs" --url=$URL
```
