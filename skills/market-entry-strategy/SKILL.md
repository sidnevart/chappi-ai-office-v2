---
name: market-entry-strategy
description: |
  Develop market entry strategy for new markets.
  Use when: (1) User asks about entering market, (2) Expansion planning,
  (3) Go-to-market strategy, (4) International expansion.

  Input: Market + Product + Resources
  Output: Entry strategy + timeline + budget
  Hashtags: #business #стратегия #выход_на_рынок #expansion
---

# MarketEntryStrategy Skill

## Workflow

1. **Market analysis**: Size, competition, regulations
2. **Entry modes**: Direct, partnership, acquisition
3. **Localization**: Product, pricing, marketing
4. **Timeline**: Phased approach
5. **Budget**: Investment required
6. **Risk assessment**: Mitigation strategies

## Entry Modes

| Mode | Pros | Cons |
|------|------|------|
| Direct | Full control | High investment |
| Partnership | Local knowledge | Shared profits |
| Acquisition | Fast | Expensive |
| Licensing | Low risk | Limited control |

## Output Format

```json
{
  "market": "Russia",
  "product": "AI Assistant",
  "strategy": {
    "mode": "Partnership",
    "partner": "Local tech company",
    "phases": [
      {
        "phase": 1,
        "duration": "6 months",
        "tasks": ["Regulatory compliance", "Localization"],
        "budget": "$200K"
      },
      {
        "phase": 2,
        "duration": "12 months",
        "tasks": ["Pilot launch", "Marketing"],
        "budget": "$500K"
      }
    ]
  },
  "localization": {
    "language": "Russian",
    "payments": "SberPay, Mir",
    "hosting": "Russia-based"
  },
  "risks": [
    {"risk": "Regulatory changes", "mitigation": "Legal counsel"},
    {"risk": "Currency fluctuation", "mitigation": "Hedging"}
  ],
  "roi_projection": "Break-even in 24 months"
}
```

## Memory Storage

- entity_type: "market_strategy"
- tags: "business,market-entry,{market}"
