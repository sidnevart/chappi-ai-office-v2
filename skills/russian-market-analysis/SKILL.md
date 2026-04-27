---
name: russian-market-analysis
description: Use when analyzing market entry strategy for Russia or CIS, regulatory compliance, or localization requirements for tech products
---

# Russian Market Analysis

## Overview

Analyzes Russian/CIS market entry: size, regulations, competitors, localization. Structured for 152-FZ compliance.

## When to Use

- User mentions "Russia", "CIS", "Россия"
- Pipeline: idea → market analysis → regulatory check
- Compliance review for data residency

**When NOT to use:**
- Global market → use trend-monitor
- Funding → use funding-scout
- General strategy → use competitive-analysis

## Core Pattern

**Input:** Business idea JSON
**Process:** Research market → Check regulations → Map competitors → Assess viability
**Output:** JSON with market data, compliance checklist

## Workflow

### 1. Market Size

Research:
- TAM/SAM/SOM
- Growth rate
- Key segments

### 2. Regulations

```json
{
  "regulation": "152-FZ",
  "requirement": "Data residency",
  "compliance_method": "Yandex Cloud / Self-hosted",
  "cost": "$...",
  "timeline": "..."
}
```

### 3. Competitors

| Company | Strength | Weakness | Local Presence |
|---------|----------|----------|----------------|
| ... | ... | ... | ... |

### 4. Localization

- Language: Russian
- Payments: Rubles, SBP
- Support: Russian-speaking
- Infrastructure: Yandex Cloud, Selectel

### 5. Report

```
/mnt/files/research-state/business/russian_market/{idea-slug}.json
```

## Output Format

```json
{
  "idea": "...",
  "market_size_usd": 0,
  "growth_rate": "35%",
  "regulations": [...],
  "compliance_required": true,
  "competitors": [...],
  "localization_requirements": [...],
  "entry_barriers": [...],
  "recommended_approach": "..."
}
```

## Quick Reference

| Topic | Search Query |
|-------|-------------|
| Market size | "{sector} market Russia 2026" |
| Regulations | "152-FZ compliance {product}" |
| Competitors | "{product} Russia alternatives" |
| Infrastructure | "Yandex Cloud vs AWS Russia" |

## Common Mistakes

- **Ignoring sanctions:** Check current restrictions
- **Wrong TAM:** Russia ≠ CIS (different markets)
- **Missing payment methods:** SBP, Mir cards required
- **No local support:** Russian-speaking support critical
