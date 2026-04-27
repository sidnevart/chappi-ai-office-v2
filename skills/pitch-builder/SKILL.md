---
name: pitch-builder
description: Use when creating investor pitch decks with evidence-based claims and proofs
---

# Pitch Builder (Evidence-Based)

## Overview

Generates investor pitch decks as **HTML** (primary) with:
- Every claim backed by evidence
- Source citations in speaker notes
- Market data with calculations
- Competitive analysis with proof
- Risk mitigation with data

## Output Formats

1. **HTML** (`/mnt/files/research-state/business/pitches/*.html`) — PRIMARY
2. **PDF** — converted from HTML for printing
3. **S3 URL** — public access
4. **Telegram** — notification with link

## Evidence Requirements

Every slide MUST have:
- **Speaker notes** with evidence URLs
- **Data sources** for every number
- **Calculation methods** shown
- **Counter-arguments** addressed

## HTML Structure

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    .slide { min-height: 100vh; padding: 60px; }
    h1 { font-size: 48px; color: #1a237e; }
    .metric { display: inline-block; padding: 15px; background: linear-gradient(135deg, #667eea, #764ba2); color: white; border-radius: 8px; }
    .evidence { font-size: 14px; color: #666; margin-top: 20px; }
    .source { color: #667eea; }
  </style>
</head>
<body>
  <!-- Slide 1: Title -->
  <div class="slide">
    <h1>TeamMemory AI</h1>
    <p>AI-память команды</p>
    <div class="metric">$150M</div>
    <div class="evidence">
      Market size calculation: 500K teams × $300/year = $150M
      Source: Rosstat, Habr survey
    </div>
  </div>
  
  <!-- Slide 2: Problem -->
  <div class="slide">
    <h1>Проблема</h1>
    <ul>
      <li>PM тратит 2-3 часа/день на статусы</li>
      <li>85% команд СНГ используют Telegram</li>
    </ul>
    <div class="evidence">
      Source 1: TASS survey (https://tass.ru/...)
      Source 2: Habr article (https://habr.com/...)
      Method: Survey of 1000 PMs
    </div>
  </div>
  
  <!-- Slide 3: Solution -->
  <div class="slide">
    <h1>Решение</h1>
    <p>Multi-source AI memory</p>
    <div class="evidence">
      Patent pending: USPTO #...
      Source: Patent filing (https://uspto.gov/...)
    </div>
  </div>
</body>
</html>
```

## Workflow

### Step 1: Evidence Collection

For each pitch claim:
1. Find source
2. Verify number
3. Check date
4. Document method

### Step 2: Self-Challenge

For each slide:
- "What would investor ask?"
- "What's the counter-argument?"
- "What if this number is wrong?"
- "Why us and not them?"

### Step 3: Generate Pitch

HTML with:
- Professional styling
- Evidence in speaker notes
- Source citations
- Counter-arguments addressed

### Step 4: Convert to PDF

```python
from reportlab.lib.pagesizes import A4
# Convert HTML to PDF
```

## Best Practices

- ✅ Every number has source
- ✅ Speaker notes with evidence
- ✅ Counter-arguments addressed
- ✅ Professional design
- ❌ No unsupported claims
- ❌ No "we believe" statements
- ❌ No numbers without calculation

## Commands

```bash
# Build pitch with evidence
python3 skills/pitch-builder/build.py --idea=team-memory-ai --with-evidence

# Convert to PDF
python3 skills/html-to-pdf/convert.py --input=pitches/team-memory-ai.html

# Upload
python3 skills/s3-uploader/upload.py --file=pitches/team-memory-ai.html
```
