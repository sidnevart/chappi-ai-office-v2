---
name: financial-modeling
description: Use when building financial projections, unit economics, or valuation models for startups and business ideas
---

# Financial Modeling

## Overview

Builds 5-year financial projections, unit economics, and valuation models. Structured for investor presentations.

## When to Use

- User asks for "financial model" or "projections"
- Pipeline: idea → funding → financial model
- Preparing for fundraising

**When NOT to use:**
- Market analysis → use trend-monitor
- Funding search → use funding-scout
- Pitch deck → use pitch-builder

## Core Pattern

**Input:** Business idea JSON
**Process:** Define assumptions → Build model → Calculate metrics → Report
**Output:** JSON with 5-year projections, unit economics

## Workflow

### 1. Assumptions

```json
{
  "customers_year_1": 50,
  "arpu_monthly": 100,
  "cac": 200,
  "churn_monthly": 0.05,
  "gross_margin": 0.8,
  "team_size_year_1": 5,
  "avg_salary": 80000
}
```

### 2. Revenue Model

Year 1: Customers × ARPU × 12
Year 2+: Growth rate applied

### 3. Unit Economics

- LTV = ARPU × Gross Margin / Churn
- LTV/CAC ratio
- Payback period

### 4. Projections Table

| Year | Revenue | Customers | EBITDA | Team |
|------|---------|-----------|--------|------|
| 1 | $86K | 50 | -30% | 5 |
| 2 | $432K | 200 | 10% | 10 |
| 3 | $1.9M | 800 | 25% | 20 |
| 4 | $5.2M | 2500 | 35% | 40 |
| 5 | $10.4M | 6000 | 40% | 60 |

### 5. Report

```
/mnt/files/research-state/business/financial_models/{idea-slug}.json
```

## Output Format

```json
{
  "idea": "...",
  "assumptions": {...},
  "projections": [...],
  "unit_economics": {
    "ltv": 2160,
    "cac": 200,
    "ltv_cac_ratio": 10.8,
    "payback_months": 3
  },
  "funding_requirements": {
    "pre_seed": "$100K",
    "seed": "$1M",
    "series_a": "$5M"
  }
}
```

## Quick Reference

| Metric | Formula |
|--------|---------|
| LTV | ARPU × Gross Margin / Monthly Churn |
| CAC | Marketing + Sales / New Customers |
| Burn Rate | Monthly expenses |
| Runway | Cash / Burn Rate |

## Common Mistakes

- **Overly optimistic growth:** Base on comparable companies
- **Ignoring churn:** Critical for SaaS
- **Wrong market size:** TAM ≠ addressable market
- **No sensitivity analysis:** Test best/worst case
