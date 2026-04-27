---
name: funding-scout
description: Use when searching for investors, accelerators, or grants for a specific startup idea or sector, especially for pre-seed to Series A stages
---

# Funding Scout

## Overview

Finds investors, accelerators, and grants for startup ideas. Structured by stage, sector, and geography.

## When to Use

- User asks "who can fund this"
- Pipeline: idea → funding search → financial model
- Preparing for fundraising

**When NOT to use:**
- Market analysis → use trend-monitor
- Financial modeling → use financial-modeling
- Pitch creation → use pitch-builder

## Core Pattern

**Input:** Business idea JSON
**Process:** Search investors → Filter by fit → Structure → Report
**Output:** JSON with investors, accelerators, grants

## Workflow

### 1. Search Investors

By stage:
- Pre-seed: Angels, friends & family
- Seed: Micro-VCs, angels
- Series A: VC firms
- Growth: Late-stage VC, PE

### 2. Filter by Fit

```json
{
  "investor": "...",
  "type": "VC|Angel|Accelerator|Grant",
  "stage": "Pre-seed|Seed|Series A",
  "sectors": [...],
  "check_size": "$...",
  "geography": "...",
  "relevance_score": 0.0-1.0,
  "contact_info": "..."
}
```

### 3. Accelerators

| Accelerator | Focus | Application Deadline |
|-------------|-------|---------------------|
| Y Combinator | General | Rolling |
| Techstars | Vertical | Quarterly |
| 500 Startups | General | Rolling |

### 4. Grants

- SBIR/STTR (US)
- Horizon Europe (EU)
- Сколково (Russia)

### 5. Report

```
/mnt/files/research-state/business/funding/{idea-slug}.json
```

## Output Format

```json
{
  "idea": "...",
  "recommended_stage": "Seed",
  "recommended_amount": "$1M",
  "investors": [...],
  "accelerators": [...],
  "grants": [...],
  "total_opportunities": 0
}
```

## Quick Reference

| Stage | Search Query |
|-------|-------------|
| Seed | "seed investors AI 2026" |
| Series A | "Series A VC {sector}" |
| Grants | "SBIR {sector}" OR "Horizon Europe {topic}" |
| Angels | "angel investors {location}" |

## Common Mistakes

- **Wrong stage:** Don't approach Series A VC for pre-seed
- **Ignoring geography:** Check investor's region focus
- **Missing warm intros:** Note mutual connections
- **No follow-up strategy:** Include recommended next steps
