---
name: pitch-builder
description: Use when creating investor pitch decks, demo day presentations, or fundraising materials for startups and business ideas
---

# Pitch Builder

## Overview

Generates HTML pitch decks from business analysis data. Structured for investor presentations with professional design.

## When to Use

- User asks for "pitch deck" or "investor presentation"
- Pipeline: idea → analysis → financials → pitch
- Preparing for demo day or investor meetings

**When NOT to use:**
- Financial models → use financial-modeling
- Market analysis → use trend-monitor
- Technical specs → use tech-spec-writer

## Core Pattern

**Input:** Business idea + analysis + financials JSON
**Process:** Gather data → Design slides → Generate HTML → Upload to S3
**Output:** HTML file + S3 URL

## Workflow

### 1. Gather Data

Read from state:
```
research-state/business/ideas/{idea}.json
research-state/business/companies/*.json
research-state/business/strategies/{idea}.json
research-state/business/financial_models/{idea}.json
```

### 2. Design Slides

Standard 8-slide structure:
1. Title + tagline
2. Problem
3. Solution
4. Market size
5. Competition + differentiation
6. Business model
7. Traction/roadmap
8. Team + ask

### 3. Generate HTML

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    @page { size: 16:9; }
    .slide { min-height: 100vh; padding: 60px; }
    h1 { font-size: 48px; }
    .metric { display: inline-block; padding: 15px; ... }
  </style>
</head>
<body>
  <!-- slides -->
</body>
</html>
```

### 4. Upload

```
/mnt/files/research-state/business/pitches/{idea}.html
```

Then upload to S3:
```
https://chappi-ai-office.s3.yandexcloud.net/pitches/{idea}.html
```

## Slide Structure

| # | Slide | Content |
|---|-------|---------|
| 1 | Title | Company name, tagline, 3 key metrics |
| 2 | Problem | 3 pain points |
| 3 | Solution | Product screenshot, key features |
| 4 | Market | TAM/SAM/SOM, growth rate |
| 5 | Competition | 2x2 matrix, differentiation |
| 6 | Business | Pricing, unit economics |
| 7 | Traction | Metrics, roadmap |
| 8 | Ask | Amount, use of funds, contact |

## Quick Reference

| Action | Command |
|--------|---------|
| Read data | Read JSON from research-state |
| Generate HTML | Write to pitches/ |
| Upload S3 | Use s3-uploader skill |

## Common Mistakes

- **Too much text:** Max 6 bullets per slide
- **No metrics:** Investors want numbers
- **Ignoring design:** Professional look matters
- **Missing ask:** Always specify funding amount
