---
name: idea-generator
description: Use when generating business ideas from market gaps
---

# Idea Generator

## Overview

Generates scored business ideas. Output: **JSON** (for pipeline) + **HTML report** (for humans).

## Output Formats

1. **JSON** (`/mnt/files/research-state/business/ideas.json`) — for pipeline
2. **HTML** (`/mnt/files/research-state/reports/html/ideas-*.html`) — human-readable
3. **S3 URL** — public access
4. **Telegram** — notification with link

## What This Skill Does NOT Produce

- ❌ Excel (no financial data yet)
- ❌ Google Sheets
- ❌ PDF

## Workflow

### Step 1: Generate Ideas

Read trends + weaknesses → generate ideas.

### Step 2: Save JSON

```json
{
  "ideas": [
    {
      "name": "TeamMemory AI",
      "score": 9.0,
      "market_size": "$150M",
      "feasibility": "high"
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
  .idea { background: #f0f4ff; padding: 20px; border-radius: 8px; margin: 20px 0; }
  .score { font-size: 32px; color: #667eea; }
</style></head>
<body>
  <h1>💡 Generated Ideas</h1>
  <div class="idea">
    <h2>TeamMemory AI</h2>
    <div class="score">9.0/10</div>
    <p>AI-память команды...</p>
  </div>
</body>
</html>
```

### Step 4: Upload to S3

```python
s3.put_object(Bucket='ai-office', Key='reports/ideas-2026-04-28.html', Body=html, ContentType='text/html')
```

### Step 5: Send to Telegram

```
💡 Idea Generator: 3 ideas generated
Top: TeamMemory AI (9.0/10)

🔗 https://80.74.25.43:9000/ai-office/reports/ideas-2026-04-28.html
```

## Best Practices

- ✅ JSON for pipeline
- ✅ HTML for humans (scored ideas)
- ❌ Don't create Excel
- ❌ Don't create Google Sheets

## Commands

```bash
# Run agent
python3 skills/idea-generator/generate.py

# Generate HTML
python3 skills/html-builder/build.py --input=ideas.json --output=ideas.html

# Upload
python3 skills/s3-uploader/upload.py --file=reports/html/ideas.html

# Send to Telegram
python3 skills/telegram-reporter/send.py --message="💡 Ideas" --url=$URL
```
