---
name: financial-modeling
description: Use when building financial projections with evidence-based assumptions and Google Sheets output
---

# Financial Modeling

## Overview

Builds financial models and produces:
1. **Google Sheets** — PRIMARY human-readable format with formulas
2. **HTML Summary** — quick overview with evidence
3. **S3 URL** — public access
4. **Telegram** — notification with link

## Evidence Rules

Every assumption MUST have:
- **Source**: Where the number came from
- **Method**: How it was calculated
- **Confidence**: High/Medium/Low
- **Sensitivity**: What if this is wrong?

## Output Formats

| Format | Purpose | Tool |
|--------|---------|------|
| **Google Sheets** | Human analysis, formulas, charts | Google Sheets API |
| **HTML Summary** | Quick overview with key metrics | HTML |
| **Excel** | Backup, offline use | openpyxl |
| **JSON** | Pipeline only (internal) | — |

## Google Sheets Structure

### Sheet 1: Assumptions (with Evidence)

| Assumption | Value | Source | Method | Confidence | If Wrong |
|------------|-------|--------|--------|------------|----------|
| CAC | $200 | Comparable SaaS | Benchmarking | Medium | ±50% |
| ARPU | $100 | Market research | Survey data | High | ±20% |
| Churn | 5% | Industry standard | Benchmarking | Medium | ±30% |

### Sheet 2: Unit Economics

| Metric | Formula | Result | Source |
|--------|---------|--------|--------|
| LTV | =B2*B3/B4 | $2,160 | Standard SaaS formula |
| LTV/CAC | =B5/B1 | 10.8x | Target >3x |
| Payback | =B1/(B2*B3) | 3 months | Industry standard |

### Sheet 3: 5-Year Projections

| Year | Revenue | Customers | Team | EBITDA |
|------|---------|-----------|------|--------|
| 1 | =B2*B3*12 | 50 | 5 | -30% |
| 2 | =B2*1.2 | =B3*4 | 10 | 10% |

### Sheet 4: Sensitivity Analysis

| Variable | -20% | Base | +20% |
|----------|------|------|------|
| CAC | 13.5x | 10.8x | 9.0x |
| Churn | 13.5x | 10.8x | 9.0x |

## Workflow

### 1. Research Assumptions

For each assumption:
1. Search comparable companies
2. Find benchmarks
3. Calculate from data
4. Document sources

### 2. Build Model in Sheets

Use Google Sheets API with formulas (not hardcoded values).

### 3. Generate HTML Summary

```html
<h1>💰 Financial Model: TeamMemory AI</h1>
<div class="metrics">
  <div class="metric">
    <span class="value">$2,160</span>
    <span class="label">LTV</span>
    <span class="source">Source: Benchmark</span>
  </div>
  <div class="metric">
    <span class="value">10.8x</span>
    <span class="label">LTV/CAC</span>
    <span class="source">Source: Calculation</span>
  </div>
</div>
<p><strong>Full model:</strong> <a href="https://docs.google.com/spreadsheets/d/...">Google Sheets</a></p>
```

## Best Practices

- ✅ All formulas in Sheets (not hardcoded)
- ✅ Assumptions documented with sources
- ✅ Sensitivity analysis included
- ✅ Charts for visualization
- ❌ No hardcoded values without formula
- ❌ No model without sensitivity analysis
- ❌ No assumption without source
