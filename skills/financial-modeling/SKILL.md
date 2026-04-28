---
name: financial-modeling
description: Use when building SERIOUS financial models with Excel/Google Sheets output, formulas, charts, and sensitivity analysis
---

# Financial Modeling

## Overview

Builds **professional financial models** as Excel (.xlsx) or Google Sheets with:
- All formulas (not hardcoded values)
- Sensitivity analysis tables
- Charts (revenue, burn rate, unit economics)
- Assumptions with sources
- Unit economics (LTV, CAC, payback)
- 5-year projections
- Break-even analysis
- Burn rate analysis
- ROI calculations

## Output

1. **Excel** (`.xlsx`) with formulas — PRIMARY
2. **HTML Summary** (`reports/html/financial-[idea].html`) — for Telegram
3. **S3 Upload** → public URL for Excel + HTML
4. **Telegram** → link to HTML only (NEVER JSON)

## CRITICAL RULES

- ✅ **Excel/Google Sheets** — единственный формат для финмодели
- ✅ **HTML summary** — для Telegram (ссылка на Excel)
- ❌ **НИКОГДА** не отправлять JSON в Telegram
- ❌ **НИКОГДА** не отправлять сырые цифры без Excel
- ❌ **НИКОГДА** не отправлять JSON как финансовый отчёт

## NEVER output JSON for humans. JSON is pipeline-internal only.

## Sheet Structure (Excel/Google Sheets)

### Sheet 1: Dashboard
Key metrics at a glance:
| Metric | Value | Formula | Source |
|--------|-------|---------|--------|
| LTV | $2,160 | =Assumptions!B2*Assumptions!B3*Assumptions!B4 | Calculated |
| CAC | $200 | =Assumptions!B5 | Benchmark |
| LTV/CAC | 10.8x | =Dashboard!B1/Dashboard!B2 | Target >3x |
| Payback | 3 months | =Dashboard!B2/(Assumptions!B2*Assumptions!B3) | Standard |
| Break-even | Month 14 | =MATCH(0,Projections!E2:E6,0) | Calculated |
| Runway | 18 months | =Cash!B12/Cash!B13 | With current cash |

### Sheet 2: Assumptions (with Evidence)

| # | Assumption | Value | Source | Method | Confidence | If Wrong |
|---|------------|-------|--------|--------|------------|----------|
| 1 | ARPU monthly | $100 | Otter.ai pricing | Competitor analysis | High | ±20% |
| 2 | Gross Margin | 80% | SaaS standard | Benchmark | High | ±10% |
| 3 | LTV months | 18 | Industry avg | Benchmark | Medium | ±30% |
| 4 | CAC | $200 | SaaS benchmarks | Comparable analysis | Medium | ±50% |
| 5 | Churn monthly | 5% | Industry avg | Benchmark | Medium | ±30% |
| 6 | Team growth | 2x/year | Planning | Internal | Low | ±40% |

### Sheet 3: Unit Economics

| Metric | Formula | Result | Benchmark | Status |
|--------|---------|--------|-----------|--------|
| LTV | =B2*B3*B4 | $2,160 | >$1,000 | ✅ |
| CAC | =B5 | $200 | <$500 | ✅ |
| LTV/CAC | =B1/B2 | 10.8x | >3x | ✅ |
| Payback | =B2/(B2_monthly*B3) | 3 months | <12 months | ✅ |
| Gross Margin | =B3 | 80% | >70% | ✅ |
| Net Revenue Retention | =B6 | 105% | >100% | ✅ |

### Sheet 4: 5-Year Projections

| Year | Customers | Revenue | COGS | Gross Profit | OpEx | EBITDA | Cash |
|------|-----------|---------|------|--------------|------|--------|------|
| 1 | 50 | =B2*1200 | =C2*0.2 | =C2-D2 | =E2*1.5 | =E2-F2 | =G2+300000 |
| 2 | 200 | =B3*1200 | =C3*0.2 | =C3-D3 | =F2*1.8 | =E3-F3 | =H2+G3 |

### Sheet 5: Sensitivity Analysis

**LTV/CAC sensitivity to CAC and Churn:**

| CAC \ Churn | 3% | 5% | 7% | 10% |
|-------------|----|----|----|-----|
| $100 | =calc | =calc | =calc | =calc |
| $200 | =calc | =calc | =calc | =calc |
| $500 | =calc | =calc | =calc | =calc |

### Sheet 6: Burn Rate & Runway

| Month | Revenue | OpEx | Burn | Cumulative Burn | Cash Remaining | Runway |
|-------|---------|------|------|-----------------|----------------|--------|
| 1 | =B2 | =C2 | =C2-B2 | =D2 | =300000-E2 | =F2/D2 |
| 2 | =B2*1.1 | =C2*1.02 | =C3-B3 | =E2+D3 | =F2-E3 | =F3/D3 |

### Sheet 7: Break-Even Analysis

| Month | Fixed Costs | Variable/Unit | Units | Total Cost | Revenue | Profit |
|-------|-------------|---------------|-------|------------|---------|--------|
| 1 | =B2 | =C2 | =D2 | =B2+C2*D2 | =E2 | =E2-F2 |

### Sheet 8: Charts

1. **Revenue Growth** (Line chart: 5 years)
2. **Customer Growth** (Bar chart: 5 years)
3. **Burn Rate** (Area chart: 24 months)
4. **Unit Economics** (Waterfall: LTV components)
5. **Sensitivity Heatmap** (Conditional formatting)

## Workflow

### 1. Build Assumptions
- Research comparable companies
- Document sources with URLs
- Show calculation methods
- Mark confidence levels

### 2. Build Model with Formulas
- All values = formulas (never hardcoded)
- Named ranges for key assumptions
- Data validation for inputs
- Conditional formatting for alerts

### 3. Generate Charts
- Revenue growth line chart
- Customer acquisition bar chart
- Burn rate area chart
- Unit economics waterfall
- Sensitivity heatmap

### 4. Generate HTML Summary

```html
<h1>💰 Financial Model: TeamMemory AI</h1>
<p>📅 Generated: [Date] | Status: ✅ Complete</p>

<div class="metrics">
  <div class="metric">
    <span class="value">$2,160</span>
    <span class="label">LTV</span>
    <span class="source">Source: Calculation</span>
  </div>
  <div class="metric">
    <span class="value">10.8x</span>
    <span class="label">LTV/CAC</span>
    <span class="source">Target: >3x ✅</span>
  </div>
</div>

<p><strong>📊 Full Model:</strong> <a href="[S3_EXCEL_URL]">Download Excel (.xlsx)</a></p>

<p><strong>📈 Sheets:</strong></p>
<ul>
  <li>Dashboard — Key metrics</li>
  <li>Assumptions — Sources + evidence</li>
  <li>Unit Economics — LTV, CAC, payback</li>
  <li>5-Year Projections — Revenue, EBITDA</li>
  <li>Sensitivity Analysis — Risk scenarios</li>
  <li>Burn Rate — Monthly burn + runway</li>
  <li>Break-Even — Month-by-month</li>
  <li>Charts — Visualizations</li>
</ul>

<p><strong>⚠️ Key Risks:</strong></p>
<ul>
  <li>CAC could be 50% higher → LTV/CAC drops to 7.2x</li>
  <li>Churn could be 2x → LTV drops to $1,080</li>
  <li>Break-even at month 14 with base case</li>
</ul>
```

## Code Example (openpyxl)

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.chart import LineChart, Reference

wb = Workbook()

# Dashboard
ws = wb.active
ws.title = "Dashboard"
ws['A1'] = "LTV"
ws['B1'] = "=Assumptions!B2*Assumptions!B3*Assumptions!B4"
ws['C1'] = "Formula: ARPU × Margin × Months"

# Assumptions
ws2 = wb.create_sheet("Assumptions")
ws2['A1'] = "Assumption"
ws2['B1'] = "Value"
ws2['C1'] = "Source"
ws2['A2'] = "ARPU monthly"
ws2['B2'] = 100
ws2['C2'] = "Otter.ai pricing"

# Chart
chart = LineChart()
data = Reference(ws, min_col=2, min_row=1, max_row=6)
chart.add_data(data, titles_from_data=True)
ws.add_chart(chart, "E2")

wb.save("financial_model.xlsx")
```

## Best Practices

- ✅ ALL values are formulas (not hardcoded)
- ✅ Assumptions in separate sheet with sources
- ✅ Charts auto-update when inputs change
- ✅ Sensitivity analysis for key variables
- ✅ Break-even month clearly shown
- ✅ Burn rate with runway calculation
- ✅ Conditional formatting for alerts (red if <0)
- ❌ No hardcoded projections
- ❌ No model without sensitivity analysis
- ❌ No model without break-even calculation


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
