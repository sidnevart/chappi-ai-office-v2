---
name: idea-generator
description: Use when generating business ideas with evidence-based analysis, proofs, and citations
---

# Idea Generator (Evidence-Based)

## Overview

Generates business ideas and produces **HTML evidence document** with:
- Full justification for each claim
- Web search citations with URLs
- Self-challenge: why this idea, why now, why us
- Risk analysis with mitigation
- Score breakdown with reasoning

## Output Formats

1. **HTML Report** (`/mnt/files/research-state/reports/html/ideas-*.html`) — PRIMARY, human-readable with evidence
2. **Google Sheets** (optional) — if financial data needed
3. **S3 URL** — public access
4. **Telegram** — notification with link

**NO JSON for humans.** JSON only for internal pipeline state.

## Evidence Requirements

Every claim MUST have:
- **Source:** URL or primary research
- **Method:** How the number was calculated
- **Confidence:** High/Medium/Low with justification
- **Challenge:** "Why not X instead?" answered

## HTML Structure

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
  <p>Market size calculation:</p>
  <pre>
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
```

## Workflow

### Step 1: Deep Research

For each trend/weakness pair:
1. **Web search** for market data
2. **Cross-reference** 3+ sources
3. **Calculate** market size with method shown
4. **Challenge** the idea: "Why will this work?"

### Step 2: Self-Challenge Questions

Every idea MUST answer:
- Why this problem exists? (with data)
- Why existing solutions fail? (with examples)
- Why now? (market timing evidence)
- Why us? (team/tech advantage)
- Why will customers pay? (willingness-to-pay data)
- What if we're wrong? (risk matrix)

### Step 3: Evidence Collection

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

### Step 4: Generate HTML Document

Professional HTML with:
- Executive summary with key metrics
- Problem definition with evidence
- Solution description with differentiation
- Market size with calculation method
- Competition analysis with source links
- Score breakdown with weights explained
- Risk matrix with mitigation plans
- Sources section (all URLs listed)

### Step 5: Upload & Share

```python
s3.put_object(Bucket='ai-office', Key='reports/ideas-2026-04-28.html', Body=html, ContentType='text/html')
```

Telegram:
```
💡 New Idea: TeamMemory AI (9.2/10)

Evidence:
• Market: $150M (source: linked)
• LTV/CAC: 10.8x (calculation shown)
• Competition: 6 analyzed (full table)

Self-challenge passed ✅

🔗 Full evidence: https://...
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

## Example Evidence Block

```html
<div class="evidence">
  <h3>Claim: AI Meeting Assistant market is $5.2B</h3>
  <p><strong>Sources:</strong></p>
  <ul>
    <li><a href="https://www.grandviewresearch.com/...">Grand View Research</a> — $4.8B (2025)</li>
    <li><a href="https://www.marketsandmarkets.com/...">MarketsandMarkets</a> — $5.5B (2026)</li>
  </ul>
  <p><strong>Method:</strong> Average of 2 market research firms</p>
  <p><strong>Confidence:</strong> High (independent sources agree)</p>
  <p><strong>Challenge:</strong> Could this be overestimated?</p>
  <p><strong>Answer:</strong> Conservative estimate used. If 50% lower, still viable.</p>
</div>
```

## Commands

```bash
# Generate idea with full evidence
python3 skills/idea-generator/generate.py --with-evidence --challenge-self

# Verify evidence
python3 skills/idea-generator/verify.py --idea=team-memory-ai

# Generate HTML
python3 skills/html-builder/build.py --input=idea-evidence.json --template=evidence-based

# Upload
python3 skills/s3-uploader/upload.py --file=reports/html/ideas-evidence.html
```
