---
name: financial-modeler-agent
description: Agent skill for FinancialModeler. Builds financial models: unit economics, projections, Google Sheets output.
---

# FinancialModeler Agent

## Purpose

Financial modeling agent that creates unit economics, projections, and outputs to Google Sheets.

## Trigger

- Request from any business agent
- User request: "Построй финансовую модель"

## Input

- Business idea or company data
- Market assumptions

## Output

Google Sheet + JSON report

## Process

1. Read business data
2. Build assumptions:
   - Market size
   - Pricing
   - Customer acquisition
   - Churn
   - Costs
3. Calculate unit economics:
   - CAC, LTV, LTV/CAC
   - Payback period
   - Margins
4. Build projections: 3-5 years
5. Create Google Sheet
6. Save JSON summary

## Output Format

```json
{
  "project": "AI Warehouse Robotics",
  "model_date": "2026-04-27",
  "source": "FinancialModeler",
  
  "assumptions": {
    "market_size": "$50B",
    "target_share": "0.1%",
    "price_per_unit": "$100k",
    "units_year_1": 10,
    "units_year_5": 500
  },
  
  "unit_economics": {
    "cac": "$50k",
    "ltv": "$300k",
    "ltv_cac_ratio": 6,
    "payback_months": 12
  },
  
  "projections": {
    "revenue": {
      "year_1": "$1M",
      "year_3": "$15M",
      "year_5": "$50M"
    },
    "gross_margin": "60%",
    "ebitda_margin_year_3": "25%"
  },
  
  "google_sheet_url": "https://docs.google.com/spreadsheets/d/..."
}
```

## Commands

When triggered, run:
1. Read input data
2. Build financial model
3. Create Google Sheet via google-sheets-writer skill
4. Save JSON summary
5. Report URL
