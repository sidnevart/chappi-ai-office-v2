---
name: trend-monitor
description: Use when monitoring market trends with evidence-based analysis and source citations
---

# Trend Monitor (Evidence-Based)

## Overview

Monitors trends and produces **HTML evidence document** with:
- Verified trend data with sources
- Market size calculations with methods shown
- Confidence levels with justification
- Cross-referenced from multiple sources
- Risk of trend being wrong analyzed

## Output Formats

1. **HTML Report** (`/mnt/files/research-state/reports/html/trends-*.html`) — PRIMARY
2. **S3 URL** — public access
3. **Telegram** — notification with link

**NO JSON for humans.**

## Evidence Requirements

Every trend MUST have:
- **Minimum 2 independent sources**
- **URL for each source**
- **Method**: How trend was identified
- **Confidence**: With justification
- **Counter-evidence**: What could prove this wrong

## HTML Structure

```html
<h1>📈 Trend Analysis Report</h1>
<p><strong>Period:</strong> [Date] | <strong>Analyst:</strong> OpenClaw AI</p>

<div class="methodology">
  <h2>🔬 Methodology</h2>
  <p><strong>Sources checked:</strong></p>
  <ul>
    <li>TechCrunch (techcrunch.com)</li>
    <li>ArXiv (arxiv.org)</li>
    <li>VentureBeat (venturebeat.com)</li>
    <li>Company press releases</li>
  </ul>
  <p><strong>Criteria for inclusion:</strong></p>
  <ul>
    <li>2+ independent sources</li>
    <li>Funding or product announcement</li>
    <li>Clear market impact</li>
  </ul>
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
    <p><strong>What could prove this wrong:</strong></p>
    <ul>
      <li>Regulatory ban on humanoid robots</li>
      <li>Battery technology plateau</li>
      <li>Safety incidents slowing adoption</li>
    </ul>
  </div>
</div>
```

## Workflow

### Step 1: Systematic Search

Search multiple sources systematically:
```
Query 1: "AI trends 2026" site:techcrunch.com
Query 2: "artificial intelligence funding" site:crunchbase.com
Query 3: "AI breakthrough" site:arxiv.org
Query 4: "AI startups" after:2026-01-01
```

### Step 2: Source Verification

For each potential trend:
1. Find 2+ independent sources
2. Check publication dates (must be recent)
3. Verify source credibility
4. Cross-check numbers

### Step 3: Self-Challenge

For each trend:
- "Is this really a trend or just a one-time event?"
- "Could this be hype?"
- "What's the counter-argument?"
- "How long will this trend last?"

### Step 4: Evidence Document

HTML with:
- Methodology section
- Each trend with evidence block
- Market calculations with methods
- Counter-evidence section
- Sources list with URLs

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

## Commands

```bash
# Monitor with evidence
python3 skills/trend-monitor/monitor.py --with-evidence --min-sources=2

# Verify trends
python3 skills/trend-monitor/verify.py --trend=physical-ai

# Generate evidence HTML
python3 skills/html-builder/build.py --input=trend-evidence.json --template=evidence-based
```
