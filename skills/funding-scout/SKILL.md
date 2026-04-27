---
name: funding-scout
description: |
  Search for funding: VCs, angels, accelerators, grants.
  Use when: (1) User asks for investors, (2) Raising round,
  (3) Need investor list, (4) Fundraising strategy.

  Input: Stage + Sector + Amount
  Output: Investor list + contacts + strategy
  Hashtags: #business #инвестиции #фонд #фандинг
---

# FundingScout Skill

## Workflow

1. **Profile analysis**: Stage, sector, amount
2. **Investor mapping**: VCs, angels, accelerators
3. **Fit analysis**: Match with investor thesis
4. **Contact info**: Partners, associates
5. **Outreach strategy**: Warm intros, cold emails

## Investor Types

| Type | Stage | Check Size |
|------|-------|------------|
| Angels | Pre-seed | $10K-$100K |
| Seed VCs | Seed | $100K-$2M |
| Series A | Series A | $2M-$15M |
| Growth | Series B+ | $15M+ |
| Corporate | Any | Strategic |

## Output Format

```json
{
  "profile": {
    "stage": "Seed",
    "sector": "AI Infrastructure",
    "amount": "$2M",
    "traction": "$50K MRR"
  },
  "investors": [
    {
      "name": "a16z",
      "type": "VC",
      "focus": ["AI", "Infrastructure"],
      "check_size": "$1M-$5M",
      "partner": "John Smith",
      "contact": "john@a16z.com",
      "fit_score": 95,
      "recent_deals": ["CompanyX", "CompanyY"]
    }
  ],
  "strategy": {
    "warm_intros": ["Via portfolio founder"],
    "pitch_focus": "Infrastructure scalability",
    "timeline": "Reach out in 2 weeks"
  },
  "materials": [
    "One-pager",
    "Pitch deck",
    "Financial model"
  ]
}
```

## Memory Storage

- entity_type: "investor"
- tags: "business,funding,{stage},{sector}"
