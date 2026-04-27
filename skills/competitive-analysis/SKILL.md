---
name: competitive-analysis
description: Use when analyzing competitive strategy with evidence-based differentiation and proof
---

# Competitive Analysis

## Overview

Analyzes competition and produces **HTML evidence report** with:
- Competitor feature matrices with proof
- Differentiation strategies with justification
- Market gaps with evidence
- Pricing comparisons with sources
- Risk analysis for each strategy

## Output

1. **HTML Report** (`reports/html/strategies/[idea].html`) — PRIMARY
2. **S3 Upload** → public URL
3. **Telegram** → link to HTML

No JSON for humans.

## Evidence Rules

Every strategy MUST have:
- **Competitor weakness proof** (screenshot, review, data)
- **Market gap evidence** (search data, user complaints)
- **Differentiation justification** (why this works)
- **Investment calculation** (cost vs impact)
- **Risk assessment** (what could go wrong)

## Workflow

### 1. Identify Market Gaps

Search for evidence:
```
Query 1: "[competitor] missing features" site:reddit.com
Query 2: "[competitor] vs [competitor]" comparison
Query 3: "best alternative to [competitor]"
Query 4: User reviews on G2/Capterra
```

### 2. Verify Gaps

For each gap:
1. Check competitor's official roadmap
2. Check user complaints (Reddit, Twitter)
3. Check if it's a technical limitation
4. Calculate cost to replicate

### 3. Strategy Justification

For each strategy:
- Why will this work? (with evidence)
- Why hasn't competitor done this? (with proof)
- What's the moat? (defensibility analysis)
- What if competitor copies? (response plan)

### 4. Generate HTML Evidence Report

```html
<h1>📊 Competitive Strategy Analysis</h1>

<div class="market-gap">
  <h2>🔍 Market Gap Evidence</h2>
  <p><strong>Gap:</strong> No multi-source AI memory for Russian teams</p>
  <p><strong>Evidence:</strong></p>
  <ul>
    <li>Search "AI team memory Telegram" — 0 relevant results (Source: <a href="...">Google Search</a>)</li>
    <li>Reddit r/startups: "Why no good team memory tool?" (Source: <a href="...">Reddit</a>)</li>
    <li>Survey: 73% of PMs want better context tracking (Source: <a href="...">ProductHunt</a>)</li>
  </ul>
</div>

<div class="strategy">
  <h2>🎯 Strategy: Multi-Source Integration</h2>
  
  <div class="why">
    <h3>Why This Strategy Works</h3>
    <p><strong>Evidence 1:</strong> Otter.ai users complain about missing chat context (Source: <a href="...">G2 Reviews</a>)</p>
    <p><strong>Evidence 2:</strong> Notion users want automatic meeting notes (Source: <a href="...">Reddit</a>)</p>
    <p><strong>Evidence 3:</strong> 85% of teams use 3+ tools for context (Source: <a href="...">Survey</a>)</p>
  </div>
  
  <div class="investment">
    <h3>Investment Required</h3>
    <pre>
Development: $200K (6 months × 3 engineers × $60K/yr)
Infrastructure: $50K/year (servers, API costs)
Marketing: $100K (launch campaign)
Total: $350K first year
Source: Internal estimation based on market rates
    </pre>
  </div>
  
  <div class="risk">
    <h3>Risk: Competitor Response</h3>
    <p><strong>Likelihood:</strong> Medium (50%)</p>
    <p><strong>Evidence:</strong> Notion acquired Cron in 2022 for calendar integration (Source: <a href="...">TechCrunch</a>)</p>
    <p><strong>Mitigation:</strong> Focus on Russian market first (152-ФЗ compliance)</p>
  </div>
</div>

<div class="feature-matrix">
  <h2>⚔️ Feature Comparison Matrix</h2>
  <table>
    <tr><th>Feature</th><th>Us</th><th>Otter</th><th>Notion</th><th>Fireflies</th><th>Source</th></tr>
    <tr><td>Meeting transcription</td><td>✅</td><td>✅</td><td>❌</td><td>✅</td><td><a href="...">Product docs</a></td></tr>
    <tr><td>Telegram integration</td><td>✅</td><td>❌</td><td>❌</td><td>❌</td><td><a href="...">Product docs</a></td></tr>
  </table>
</div>

<div class="sources">
  <h2>📚 Sources</h2>
  <ol>
    <li><a href="...">[Title]</a> — [What it proves]</li>
  </ol>
</div>
```

## Best Practices

- ✅ Every gap has user evidence
- ✅ Every strategy has investment calc
- ✅ Every risk has mitigation
- ✅ Feature matrix from official docs
- ❌ No assumed weaknesses
- ❌ No strategies without ROI
- ❌ No risks without plans
