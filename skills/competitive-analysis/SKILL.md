---
name: competitive-analysis
description: Use when building competitive strategy with HTML output and evidence-based differentiation
---

# Competitive Strategy

## Overview

Builds competitive strategies and produces **HTML evidence report** with:
- Market gap analysis with proof
- Differentiation strategy with justification
- Investment calculation with ROI
- Risk matrix with mitigation
- Feature comparison matrix
- Timeline and milestones

## Output

1. **HTML Strategy Report** (`reports/html/strategies/[idea].html`) — PRIMARY
2. **S3 Upload** → public URL
3. **Telegram** → link to HTML (NEVER JSON)

## NEVER output JSON for humans. JSON is pipeline-internal only.

## HTML Structure

```html
<h1>⚔️ Competitive Strategy: [Idea Name]</h1>
<p>📅 Generated: [Date] | Confidence: [Score]/10</p>

<div class="market-gap">
  <h2>🔍 Market Gap Evidence</h2>
  <p><strong>Gap:</strong> [Description with proof]</p>
  <ul>
    <li>Evidence 1: [Description] (Source: <a href="...">URL</a>)</li>
    <li>Evidence 2: [Description] (Source: <a href="...">URL</a>)</li>
  </ul>
</div>

<div class="strategy">
  <h2>🎯 Strategy: [Name]</h2>
  
  <div class="why">
    <h3>Why This Strategy Works</h3>
    <p>[Evidence-based justification]</p>
  </div>
  
  <div class="investment">
    <h3>Investment Required</h3>
    <table>
      <tr><th>Category</th><th>Amount</th><th>Method</th></th></tr>
      <tr><td>Development</td><td>$200K</td><td>6mo × 3eng × $60K/yr</td></tr>
      <tr><td>Infrastructure</td><td>$50K/yr</td><td>Yandex Cloud pricing</td></tr>
      <tr><td>Marketing</td><td>$100K</td><td>Launch campaign</td></tr>
      <tr><td><strong>Total Year 1</strong></td><td><strong>$350K</strong></td><td></td></tr>
    </table>
  </div>
  
  <div class="roi">
    <h3>ROI Analysis</h3>
    <p><strong>Break-even:</strong> Month 14</p>
    <p><strong>Year 5 revenue:</strong> $8.4M</p>
    <p><strong>ROI:</strong> 24x (5-year)</p>
  </div>
</div>

<div class="feature-matrix">
  <h2>⚔️ Feature Comparison Matrix</h2>
  <table>
    <tr><th>Feature</th><th>Us</th><th>Otter</th><th>Notion</th><th>Fireflies</th></th></tr>
    <tr><td>Meeting transcription</td><td>✅</td><td>✅</td><td>❌</td><td>✅</td></tr>
    <tr><td>Telegram integration</td><td>✅</td><td>❌</td><td>❌</td><td>❌</td></tr>
  </table>
  <p class="source">Source: Product documentation, verified 2026-04</p>
</div>

<div class="risks">
  <h2>⚠️ Risk Matrix</h2>
  <table>
    <tr><th>Risk</th><th>Likelihood</th><th>Impact</th><th>Mitigation</th><th>Evidence</th></tr>
    <tr><td>Competitor adds feature</td><td>Low (20%)</td><td>High</td><td>6-12mo head start</td><td><a href="...">Source</a></td></tr>
  </table>
</div>

<div class="timeline">
  <h2>📅 Timeline</h2>
  <table>
    <tr><th>Phase</th><th>Duration</th><th>Deliverable</th><th>Milestone</th></tr>
    <tr><td>MVP</td><td>Months 1-3</td><td>Telegram bot + transcription</td><td>100 beta users</td></tr>
    <tr><td>Launch</td><td>Months 4-6</td><td>Full platform</td><td>1,000 users</td></tr>
    <tr><td>Scale</td><td>Months 7-12</td><td>Enterprise features</td><td>5,000 users</td></tr>
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
- ✅ Every strategy has investment calc with ROI
- ✅ Feature matrix from official docs
- ✅ Risk matrix with likelihood/impact/mitigation
- ✅ Timeline with milestones
- ❌ No assumed weaknesses
- ❌ No strategies without ROI
- ❌ No risks without plans
- ❌ NEVER output JSON to Telegram


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
