---
name: company-deep-dive
description: Use when analyzing companies with deep evidence, competitor comparison, and source citations
---

# Company Deep Dive (Evidence-Based)

## Overview

Analyzes companies and produces **HTML evidence document** with:
- Competitor comparison matrices with sources
- Product analysis with screenshots/evidence
- Weakness identification with proof
- Market position with data
- Full URL citations for every claim

## Output Formats

1. **HTML Report** (`/mnt/files/research-state/reports/html/companies/*.html`) — PRIMARY
2. **S3 URL** — public access
3. **Telegram** — notification with link

**NO JSON for humans.** Internal JSON only for pipeline.

## Evidence Requirements

Every claim MUST have:
- **Source URL**: Where the information came from
- **Method**: How it was verified
- **Confidence**: High/Medium/Low
- **Date**: When the data was collected

## HTML Structure

```html
<h1>🏢 Company Analysis: [Name]</h1>
<p><strong>Date:</strong> [Date] | <strong>Analyst:</strong> OpenClaw AI</p>

<div class="executive-summary">
  <h2>📋 Executive Summary</h2>
  <p>[2-3 sentence summary with key numbers]</p>
  <p><strong>Key Metrics:</strong></p>
  <ul>
    <li>Revenue: $X (Source: <a href="...">...</a>)</li>
    <li>Users: Y (Source: <a href="...">...</a>)</li>
    <li>Valuation: $Z (Source: <a href="...">...</a>)</li>
  </ul>
</div>

<div class="product-analysis">
  <h2>🛠️ Product Analysis</h2>
  <table>
    <tr><th>Product</th><th>Category</th><th>Users</th><th>Price</th><th>Source</th></tr>
    <tr><td>Product 1</td><td>SaaS</td><td>10M</td><td>$15/mo</td><td><a href="...">Crunchbase</a></td></tr>
  </table>
  <p><strong>Evidence:</strong> Product screenshots, feature comparison from <a href="...">G2</a></p>
</div>

<div class="competitor-matrix">
  <h2>⚔️ Competitor Comparison Matrix</h2>
  <table>
    <tr><th>Feature</th><th>This Company</th><th>Competitor A</th><th>Competitor B</th><th>Source</th></tr>
    <tr><td>Telegram</td><td>❌</td><td>❌</td><td>✅</td><td><a href="...">Product docs</a></td></tr>
  </table>
  <p><strong>Method:</strong> Feature comparison based on official product documentation and user reviews</p>
</div>

<div class="weaknesses">
  <h2>🔍 Identified Weaknesses</h2>
  <div class="weakness">
    <h3>1. No Telegram Integration</h3>
    <p><strong>Evidence:</strong> Product roadmap shows no Telegram plans (Source: <a href="...">Official blog</a>)</p>
    <p><strong>Impact:</strong> 85% of CIS teams use Telegram (Source: <a href="...">TASS survey</a>)</p>
    <p><strong>Why it matters:</strong> [Explanation with numbers]</p>
  </div>
</div>

<div class="sources">
  <h2>📚 Sources</h2>
  <ol>
    <li><a href="https://...">[Title]</a> — [What it proves]</li>
  </ol>
</div>
```

## Workflow

### Step 1: Multi-Source Research

For each company:
1. **Official website** — products, pricing
2. **Crunchbase** — funding, revenue
3. **G2/Capterra** — user reviews, features
4. **LinkedIn** — team size, hiring
5. **News** — recent developments
6. **Social media** — user sentiment

### Step 2: Cross-Verification

Every fact must be confirmed by 2+ sources:
```
Claim: "Otter.ai has 8.3M users"
Source 1: Crunchbase (https://...) — 8M users
Source 2: TechCrunch article (https://...) — 8.3M users
Source 3: Company blog (https://...) — "over 8M"
Confidence: High (3 sources agree)
```

### Step 3: Self-Challenge

Every weakness must be challenged:
- "Is this really a weakness or just not their focus?"
- "Could they add this feature quickly?"
- "What's the cost for them to fix this?"
- "Why haven't they fixed it yet?"

### Step 4: Generate Evidence Document

HTML with:
- Executive summary with verified numbers
- Product table with pricing/sources
- Competitor matrix with feature comparison
- Weaknesses with evidence blocks
- Market position with data
- Sources section with all URLs

## Best Practices

- ✅ Every number has URL source
- ✅ Every feature verified against docs
- ✅ Every weakness has impact calculation
- ✅ Self-challenge for every claim
- ❌ No assumptions without evidence
- ❌ No "I think" statements
- ❌ No outdated data (check dates)

## Commands

```bash
# Analyze with full evidence
python3 skills/company-deep-dive/analyze.py --company=OpenAI --with-evidence

# Verify sources
python3 skills/company-deep-dive/verify.py --company=OpenAI

# Generate HTML
python3 skills/html-builder/build.py --input=company-evidence.json --template=evidence-based
```
