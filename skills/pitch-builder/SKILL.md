---
name: pitch-builder
description: Use when creating investor pitch decks and presentations
---

# Pitch Builder

## Overview

Generates investor pitch decks as **HTML** (primary) with optional PDF conversion.

## Output Formats

1. **HTML** (`/mnt/files/research-state/business/pitches/*.html`) — primary, interactive
2. **PDF** — converted from HTML for printing
3. **S3 URL** — public access
4. **Telegram** — notification with link

## What This Skill Does NOT Produce

- ❌ JSON (pitch decks are visual presentations)
- ❌ Excel (irrelevant for pitches)
- ❌ Google Sheets (irrelevant)

## Workflow

### Step 1: Generate HTML Pitch

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    .slide { min-height: 100vh; padding: 60px; }
    h1 { font-size: 48px; color: #1a237e; }
    .metric { display: inline-block; padding: 15px; background: linear-gradient(135deg, #667eea, #764ba2); color: white; border-radius: 8px; }
  </style>
</head>
<body>
  <div class="slide">
    <h1>TeamMemory AI</h1>
    <div class="metric">$150M</div>
  </div>
</body>
</html>
```

### Step 2: Convert to PDF (optional)

```python
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
# OR use weasyprint if available
# OR use browser automation
```

### Step 3: Upload to S3

```python
s3.put_object(Bucket='ai-office', Key='pitches/team-memory-ai.html', Body=html, ContentType='text/html')
```

### Step 4: Send to Telegram

```
🎤 Pitch Deck: https://80.74.25.43:9000/ai-office/pitches/team-memory-ai.html
```

## Slide Structure

| # | Slide | Content |
|---|-------|---------|
| 1 | Title | Company name, tagline, metrics |
| 2 | Problem | 3 pain points |
| 3 | Solution | Product screenshot, features |
| 4 | Market | TAM/SAM/SOM |
| 5 | Competition | 2x2 matrix |
| 6 | Business | Pricing, unit economics |
| 7 | Traction | Metrics, roadmap |
| 8 | Team + Ask | Amount, use of funds |

## Best Practices

- ✅ HTML for interactive viewing
- ✅ PDF for printing/email
- ✅ Mobile-responsive
- ✅ Metrics in big numbers
- ❌ Don't create JSON
- ❌ Don't create Excel

## Commands

```bash
# Generate pitch
python3 skills/pitch-builder/build.py --idea=team-memory-ai

# Convert to PDF
python3 skills/html-to-pdf/convert.py --input=pitches/team-memory-ai.html

# Upload to S3
python3 skills/s3-uploader/upload.py --file=pitches/team-memory-ai.html

# Send to Telegram
python3 skills/telegram-reporter/send.py --message="🎤 Pitch Deck" --url=$URL
```
