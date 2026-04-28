---
name: trend-monitor
description: Use when monitoring market trends with evidence-based analysis and source citations
---

# Trend Monitor

## Overview

Monitors trends and produces **HTML evidence report** with:
- Verified trend data from multiple sources
- Market size calculations with methods shown
- Confidence levels with justification
- Counter-evidence analysis
- Full URL citations

## Output

1. **HTML Report** (`reports/html/trends-YYYY-MM-DD.html`) — PRIMARY
2. **S3 Upload** → public URL
3. **Telegram** → link to HTML

No JSON for humans. JSON only for internal pipeline state.

## Evidence Rules

Every claim MUST have:
- **2+ independent sources**
- **URL for each source**
- **Method**: how trend was identified
- **Confidence**: High/Medium/Low with justification
- **Counter-evidence**: what could prove this wrong

## Workflow

### 0. Check Vector DB
- Load /mnt/files/research-state/db/knowledge.db
- Search for existing facts
- Skip if data is fresh (TTL not expired)


### 1. Systematic Search

```
Query 1: "AI trends 2026" site:techcrunch.com
Query 2: "artificial intelligence funding" site:crunchbase.com
Query 3: "AI breakthrough" site:arxiv.org
Query 4: "AI startups" after:2026-01-01
```

### 2. Source Verification

For each trend:
1. Find 2+ independent sources
2. Check publication dates
3. Verify source credibility
4. Cross-check numbers

### 3. Self-Challenge

For each trend:
- "Is this really a trend or just a one-time event?"
- "Could this be hype?"
- "What's the counter-argument?"
- "How long will this trend last?"

### 4. Generate HTML Evidence Report

```html
<!DOCTYPE html>
<html lang="ru">
<head>...CSS...</head>
<body>
  <h1>📈 Trend Analysis Report</h1>
  
  <div class="methodology">
    <h2>🔬 Methodology</h2>
    <p>Sources checked: TechCrunch, ArXiv, VentureBeat, company press releases</p>
    <p>Criteria: 2+ independent sources, funding or product announcement, clear market impact</p>
  </div>
  
  <div class="trend">
    <h2>📊 Trend: Physical AI</h2>
    
    <div class="evidence">
      <h3>Evidence</h3>
      <p><strong>Source 1:</strong> <a href="https://techcrunch.com/...">TechCrunch</a> — "Physical AI startups raised $500M in Q1 2026"</p>
      <p><strong>Source 2:</strong> <a href="https://arxiv.org/...">ArXiv</a> — "Breakthrough in dexterous manipulation"</p>
      <p><strong>Source 3:</strong> <a href="https://...">Company announcement</a> — Figure AI raises $200M</p>
    </div>
    
    <div class="calculation">
      <h3>Market Size Calculation</h3>
      <pre>
TAM = 1M robots × $100K avg price = $100B
Method: Bottom-up from industrial robot count
Source: IFR World Robotics Report (https://ifr.org/...)
Confidence: Medium (extrapolated from industrial to humanoid)
      </pre>
    </div>
    
    <div class="counter">
      <h3>Counter-Evidence</h3>
      <ul>
        <li>Regulatory ban on humanoid robots</li>
        <li>Battery technology plateau</li>
        <li>Safety incidents slowing adoption</li>
      </ul>
    </div>
  </div>
  
  <div class="sources">
    <h2>📚 Sources</h2>
    <ol>
      <li><a href="...">[Title]</a> — [What it proves]</li>
    </ol>
  </div>
</body>
</html>
```

## Scoring Trends

| Criterion | Weight | Evidence Required |
|-----------|--------|-------------------|
| Source quality | 30% | 2+ credible sources |
| Funding evidence | 25% | Crunchbase or official |
| Market impact | 25% | Quantified impact |
| Time sensitivity | 20% | Recent (last 30 days) |

## Best Practices

- ✅ Minimum 2 sources per trend
- ✅ Show calculation methods
- ✅ Include counter-evidence
- ✅ Date all sources
- ❌ No single-source claims
- ❌ No old data (older than 90 days)
- ❌ No unverified rumors


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
