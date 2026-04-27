---
name: competitive-analysis
description: Use when analyzing competitive strategy and differentiation
---

# Competitive Analysis

## Overview

Analyzes competition and produces **HTML report** + **JSON** for pipeline.

## Output Formats

1. **JSON** (`/mnt/files/research-state/business/strategies/*.json`) — for pipeline
2. **HTML** (`/mnt/files/research-state/reports/html/strategies/*.html`) — human-readable
3. **S3 URL** — public access
4. **Telegram** — notification with link

## What This Skill Does NOT Produce

- ❌ Excel
- ❌ Google Sheets
- ❌ PDF

## Workflow

### Step 1: Analyze Competition

Read company analysis → generate strategies.

### Step 2: Save JSON

```json
{
  "strategies": [
    {
      "name": "Vertical AI",
      "type": "differentiation",
      "target": "OpenAI"
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
  <h1>📊 Competitive Strategy</h1>
  <table>
    <tr><th>Strategy</th><th>Type</th><th>Target</th></tr>
    <!-- rows -->
  </table>
</body>
</html>
```

### Step 4: Upload to S3

```python
s3.put_object(Bucket='ai-office', Key='reports/strategies/team-memory-ai.html', Body=html, ContentType='text/html')
```

### Step 5: Send to Telegram

```
📊 Competitive Strategy: 4 strategies found

🔗 https://80.74.25.43:9000/ai-office/reports/strategies/team-memory-ai.html
```

## Best Practices

- ✅ JSON for pipeline
- ✅ HTML for humans (strategy tables)
- ❌ Don't create Excel
- ❌ Don't create Google Sheets

## Commands

```bash
# Run agent
python3 skills/competitive-analysis/analyze.py

# Generate HTML
python3 skills/html-builder/build.py --input=strategies.json --output=strategies.html

# Upload
python3 skills/s3-uploader/upload.py --file=reports/html/strategies.html

# Send to Telegram
python3 skills/telegram-reporter/send.py --message="📊 Strategy" --url=$URL
```
