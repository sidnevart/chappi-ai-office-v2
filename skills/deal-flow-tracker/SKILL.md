---
name: deal-flow-tracker
description: Use when tracking startup funding and investment deals with verified data and evidence
---

# Deal Flow Tracker

## Overview

**Vector DB Integration:**
- Check /mnt/files/research-state/db/knowledge.db before research
- Save findings with embeddings
- Search related facts for context

Tracks startup funding rounds and produces **HTML evidence report** with:
- Verified deal data from multiple sources
- Cross-referenced amounts
- Investor attribution with proof
- Sector analysis with data
- Market impact assessment

## Output

1. **HTML Report** (`reports/html/deals-YYYY-MM-DD.html`) — PRIMARY
2. **S3 Upload** → public URL
3. **Telegram** → link to HTML

No JSON for humans.

## Evidence Rules

Every deal MUST have:
- **2+ independent sources** (Crunchbase + TechCrunch + company blog)
- **Amount verification** (not just "reported")
- **Investor attribution** (lead + co-investors)
- **Sector classification**
- **Date confirmation**

## Workflow

### 1. Multi-Source Search

Search:
- Crunchbase (primary)
- TechCrunch
- PitchBook (if available)
- Company press releases
- Investor announcements

### 2. Cross-Verification

For each deal:
1. Check 2+ sources for amount
2. Verify lead investor
3. Verify round type
4. Check date consistency

### 3. Impact Analysis

For each deal:
- What sector? (with evidence)
- What trend does this validate?
- What does this mean for our idea?

### 4. Generate HTML Evidence Report

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

<div class="sources">
  <h2>📚 Sources</h2>
  <ol>
    <li><a href="...">[Title]</a> — [What it proves]</li>
  </ol>
</div>
```

## Best Practices

- ✅ 2+ sources per deal
- ✅ Verify amounts
- ✅ Verify investors
- ✅ Analyze impact
- ❌ No single-source deals
- ❌ No unverified amounts
- ❌ No deals without context


## CRITICAL: Output Language

**ALL reports MUST be in Russian.**

- ✅ Report text, analysis, explanations — Russian
- ✅ Only proper nouns in English (company names, metrics)
- ✅ Source URLs can be in any language
- ❌ NEVER write full report in English
- ❌ NEVER send English analysis to Telegram (Russian users!)

### Examples

✅ **Correct:** "Рынок AI Meeting Assistants достиг $3.47B в 2025 году"
❌ **Wrong:** "AI Meeting Assistants market reached $3.47B in 2025"

✅ **Correct:** "LTV/CAC ratio составляет 10.8x"
❌ **Wrong:** "LTV/CAC ratio is 10.8x"

✅ **Correct:** "Источник: Grand View Research"
❌ **Wrong:** "Source: Grand View Research"
