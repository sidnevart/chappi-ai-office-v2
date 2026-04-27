---
name: company-deep-dive
description: Use when analyzing a specific company, product portfolio, or competitive position in any industry, especially for investment or competitive strategy research
---

# Company Deep Dive

## Overview

Produces comprehensive analysis of companies: products, weaknesses, competitors, and market position. Structured for decision-making.

## When to Use

- User names a company for analysis
- Competitive research pipeline
- Due diligence preparation

**When NOT to use:**
- Market trends → use trend-monitor
- Funding data → use deal-flow-tracker

## Core Pattern

**Input:** Company name
**Process:** Search → Analyze → Compare → Report
**Output:** JSON with products, weaknesses, competitors

## Workflow

### 1. Products

Identify all products/services:
```json
{
  "name": "...",
  "category": "...",
  "description": "...",
  "market_share": "..."
}
```

### 2. Weaknesses

Find gaps vs competitors:
- Missing features
- Geographic limitations
- Pricing issues
- Technical debt

### 3. Competitors

Map competitive landscape:
| Company | Overlap | Differentiation |
|---------|---------|-----------------|
| ... | ... | ... |

### 4. Report

```json
{
  "company": "...",
  "products": [...],
  "weaknesses": [...],
  "competitors": [...],
  "market_position": "...",
  "analyzed_at": "2026-04-28"
}
```

## Output Location

```
/mnt/files/research-state/business/companies/{company-slug}.json
```

## Quick Reference

| Step | Method |
|------|--------|
| Find products | web_search "{company} products" |
| Find weaknesses | web_search "{company} vs {competitor}" |
| Find competitors | web_search "alternatives to {company}" |

## Common Mistakes

- **Missing products:** Check company's website, Crunchbase, G2
- **Ignoring geography:** Note regional limitations
- **Old data:** Check publication dates
- **No competitors:** Always identify at least 3
