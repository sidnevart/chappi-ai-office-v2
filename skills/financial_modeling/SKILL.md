---
name: financial_modeling
description: |
  Build financial models: unit economics, projections, Excel files.
  Use when: (1) User asks for financial model, (2) Pitch deck needs numbers,
  (3) Business planning, (4) Investor requests.

  Input: Business data + Assumptions
  Output: Financial model (Excel) + Projections
  Hashtags: #business #финансы #модель #excel #unit-economics
---

# FinancialModeling Skill

## Workflow

1. **Data collection**: Revenue, costs, metrics
2. **Assumptions**: Growth rates, margins
3. **Model building**: Revenue model, cost structure
4. **Projections**: 3-5 year forecast
5. **Unit economics**: CAC, LTV, payback
6. **Output**: Excel file + summary

## Model Components

| Sheet | Content |
|-------|---------|
| Assumptions | Key inputs and drivers |
| Revenue | Revenue streams, pricing |
| Costs | COGS, OpEx, team |
| P&L | Profit & Loss statement |
| Cash Flow | Operating, investing, financing |
| Unit Economics | CAC, LTV, churn |

## Output Format

```json
{
  "model": {
    "assumptions": {
      "growth_rate": "20% MoM",
      "churn_rate": "5%",
      "arpu": "$100"
    },
    "projections": {
      "year_1": {
        "revenue": "$1.2M",
        "costs": "$800K",
        "ebitda": "$400K"
      },
      "year_3": {
        "revenue": "$10M",
        "costs": "$6M",
        "ebitda": "$4M"
      }
    },
    "unit_economics": {
      "cac": "$500",
      "ltv": "$2,000",
      "ltv_cac_ratio": "4:1",
      "payback_period": "6 months"
    }
  },
  "excel_file": "/path/to/model.xlsx",
  "summary": "Profitable by month 18"
}
```

## Memory Storage

- entity_type: "financial_model"
- tags: "business,finance,{company}"
