---
name: idea-generator
description: Use when generating business ideas with evidence-based analysis, proofs, and citations
---

# Idea Generator

## Overview

Generates business ideas and produces **HTML evidence document** with:
- Full justification for each claim
- Web search citations with URLs
- Self-challenge: why this idea, why now, why us
- Risk analysis with mitigation
- Score breakdown with reasoning

## Output

1. **HTML Report** (`reports/html/ideas-YYYY-MM-DD.html`) — PRIMARY
2. **S3 Upload** → public URL
3. **Telegram** → link to HTML

No JSON for humans.

## Evidence Rules

Every idea MUST answer:
- Why this problem exists? (with data)
- Why existing solutions fail? (with examples)
- Why now? (market timing evidence)
- Why us? (team/tech advantage)
- Why will customers pay? (willingness-to-pay data)
- What if we're wrong? (risk matrix)

## Workflow

### 1. Deep Research

For each trend/weakness pair:
1. **Web search** for market data
2. **Cross-reference** 3+ sources
3. **Calculate** market size with method shown
4. **Challenge** the idea: "Why will this work?"

### 2. Self-Challenge Questions

- Why this problem exists? (with data)
- Why existing solutions fail? (with examples)
- Why now? (market timing evidence)
- Why us? (team/tech advantage)
- Why will customers pay? (willingness-to-pay data)
- What if we're wrong? (risk matrix)

### 3. Evidence Collection

```
Claim: "85% of Russian teams use Telegram"
Proof:
- Source 1: https://vc.ru/... (VC.ru article)
- Source 2: https://tass.ru/... (TASS statistics)
- Method: Survey data from 2025
- Confidence: High (2 independent sources)

Claim: "LTV/CAC of 10.8x"
Proof:
- Calculation: (ARPU $120 × Gross Margin 80% × 18 months) / CAC $200
- Source: SaaS metrics benchmark https://...
- Method: Standard SaaS formula
- Confidence: Medium (based on comparable companies)
```

### 4. Generate HTML Evidence Document

```html
<h1>💡 Business Idea: [Name]</h1>
<p><strong>Generated:</strong> [Date] | <strong>Confidence:</strong> [Score]/10</p>

<div class="evidence-box">
  <h2>🎯 Core Insight</h2>
  <p>[The big idea]</p>
  <p><strong>Source:</strong> <a href="[URL]">[Title]</a></p>
  <p><strong>Why this matters:</strong> [Explanation]</p>
</div>

<div class="challenge-box">
  <h2>🤔 Self-Challenge</h2>
  <p><strong>Q:</strong> Why not just use Notion?</p>
  <p><strong>A:</strong> [Evidence-based answer with data]</p>
</div>

<div class="calculation">
  <h2>📐 Calculations</h2>
  <pre>
Market size calculation:
TAM = 10M teams × $100/month × 12 = $12B/year
Source: https://...
Method: Bottom-up from user count
Confidence: Medium (extrapolated from 3 sources)
  </pre>
</div>

<div class="risk-analysis">
  <h2>⚠️ Risks & Mitigation</h2>
  <table>
    <tr><th>Risk</th><th>Likelihood</th><th>Impact</th><th>Mitigation</th><th>Source</th></tr>
    <tr><td>Competition from OpenAI</td><td>High</td><td>High</td><td>Vertical focus</td><td><a href="...">Link</a></td></tr>
  </table>
</div>

<div class="sources">
  <h2>📚 Sources</h2>
  <ol>
    <li><a href="...">[Title]</a> — [What it proves]</li>
  </ol>
</div>
```

## Scoring with Evidence

| Criterion | Weight | Evidence Required |
|-----------|--------|-------------------|
| Market Size | 30% | Calculation + 2+ sources |
| Feasibility | 25% | Technical assessment + team match |
| Differentiation | 25% | Competitor comparison matrix |
| Timing | 20% | Trend data + adoption curves |

## Best Practices

- ✅ Every number has a source
- ✅ Every source has a URL
- ✅ Every calculation shown
- ✅ Every risk has mitigation
- ✅ Self-challenge in document
- ❌ No unsupported claims
- ❌ No "everyone knows" arguments
- ❌ No hand-waving


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
