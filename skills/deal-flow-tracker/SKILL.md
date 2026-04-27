---
name: deal-flow-tracker
description: Use when tracking startup funding and investment deals with verified data
---

# Deal Flow Tracker (Evidence-Based)

## Overview

Tracks startup funding and produces **HTML evidence document** with:
- Verified deal data from multiple sources
- Cross-referenced amounts
- Investor attribution
- Sector analysis
- Market impact assessment

## Output Formats

1. **HTML Report** (`/mnt/files/research-state/reports/html/deals-*.html`) — PRIMARY
2. **S3 URL** — public access
3. **Telegram** — notification with link

## Evidence Requirements

Every deal MUST have:
- **2+ independent sources** (Crunchbase + TechCrunch + company blog)
- **Amount verification** (not just "reported")
- **Investor attribution** (lead + co-investors)
- **Sector classification**
- **Date confirmation**

## HTML Structure

```html
<h1>💰 Deal Flow Report</h1>

<div class="summary">
  <h2>📊 Summary</h2>
  <p><strong>Period:</strong> [Date] | <strong>Deals found:</strong> 5 | <strong>Total value:</strong> $150M</p>
</div>

<div class="deal">
  <h2>🏢 Deal: Company Name</h2>
  
  <div class="verification">
    <h3>✅ Verification</h3>
    <p><strong>Amount claimed:</strong> $50M Series B</p>
    <p><strong>Sources:</strong></p>
    <ul>
      <li>Crunchbase: $50M (Source: <a href="...">Link</a>)</li>
      <li>TechCrunch: $50M (Source: <a href="...">Link</a>)</li>
      <li>Company blog: "$50M Series B" (Source: <a href="...">Link</a>)</li>
    </ul>
    <p><strong>Confidence:</strong> High (3 sources agree)</p>
  </div>
  
  <div class="investors">
    <h3>💼 Investors</h3>
    <p><strong>Lead:</strong> Andreessen Horowitz (Source: <a href="...">TechCrunch</a>)</p>
    <p><strong>Co-investors:</strong> Sequoia, Greylock (Source: <a href="...">Crunchbase</a>)</p>
  </div>
  
  <div class="impact">
    <h3>📈 Market Impact</h3>
    <p><strong>Sector:</strong> AI Infrastructure</p>
    <p><strong>Implications:</strong> Validates market demand for...</p>
    <p><strong>Evidence:</strong> Similar deals in Q1 2026...</p>
  </div>
</div>
```

## Workflow

### Step 1: Multi-Source Search

Search:
- Crunchbase (primary)
- TechCrunch
- PitchBook (if available)
- Company press releases
- Investor announcements

### Step 2: Cross-Verification

For each deal:
1. Check 2+ sources for amount
2. Verify lead investor
3. Verify round type
4. Check date consistency

### Step 3: Impact Analysis

For each deal:
- What sector? (with evidence)
- What trend does this validate?
- What does this mean for our idea?

### Step 4: Generate Evidence Document

HTML with:
- Deal cards with verification
- Investor details with sources
- Market impact analysis
- Trend validation

## Best Practices

- ✅ 2+ sources per deal
- ✅ Verify amounts
- ✅ Verify investors
- ✅ Analyze impact
- ❌ No single-source deals
- ❌ No unverified amounts
- ❌ No deals without context

## Commands

```bash
# Track with evidence
python3 skills/deal-flow-tracker/track.py --with-evidence --min-sources=2

# Verify deals
python3 skills/deal-flow-tracker/verify.py

# Generate HTML
python3 skills/html-builder/build.py --input=deals-evidence.json --template=evidence-based
```
