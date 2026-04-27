---
name: russian_market_analysis
description: |
  Analyze Russian market for products and ideas.
  Use when: (1) User asks about Russian market, (2) Market entry planning,
  (3) Localization strategy, (4) Competitive analysis in Russia.

  Input: Product / Idea
  Output: Market report with Russian specifics
  Hashtags: #business #россия #рынок #локализация
---

# RussianMarketAnalysis Skill

## Workflow

1. **Market research**: Russian market size, growth
2. **Competition**: Local players, international presence
3. **Regulations**: Legal requirements, compliance
4. **Localization**: Cultural adaptation
5. **Pricing**: Local pricing strategy
6. **Distribution**: Channels, partners

## Analysis Framework

| Dimension | Analysis |
|-----------|----------|
| Market Size | TAM in Russia |
| Growth | YoY growth rate |
| Competition | Local vs international |
| Regulations | Laws, restrictions |
| Culture | Localization needs |
| Pricing | Local pricing |
| Channels | Distribution |

## Output Format

```json
{
  "product": "AI Assistant",
  "market": {
    "size": "$500M TAM",
    "growth": "25% YoY",
    "key_players": ["Sber", "Yandex", "Tinkoff"]
  },
  "competition": {
    "local": ["Sber Salut", "Yandex Alice"],
    "international": ["OpenAI (limited)"],
    "market_share": {
      "Sber": "40%",
      "Yandex": "35%"
    }
  },
  "regulations": {
    "data_localization": "Required",
    "ai_ethics": "Draft law",
    "content_moderation": "Strict"
  },
  "localization": {
    "language": "Russian required",
    "culture": "Formal tone preferred",
    "payments": "SberPay, Mir"
  },
  "recommendations": [
    "Partner with local bank",
    "Ensure data localization",
    "Adapt to formal tone"
  ]
}
```

## Memory Storage

- entity_type: "market_analysis"
- tags: "business,russia,{product}"
