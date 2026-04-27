---
name: competitive-analysis
description: |
  Analyze competitors, positioning, and differentiation.
  Use when: (1) User asks about competition, (2) Need market positioning,
  (3) Building competitive strategy, (4) Preparing pitch.

  Input: Company / Idea / Market
  Output: Competitive landscape report
  Hashtags: #business #конкуренты #анализ #рынок
---

# CompetitiveAnalysis Skill

## Workflow

1. **Market mapping**: Identify competitors
2. **Feature comparison**: Product capabilities
3. **Positioning analysis**: Market positioning
4. **Differentiation**: Unique advantages
5. **Strategy**: Recommendations

## Analysis Framework

| Dimension | Analysis |
|-----------|----------|
| Features | What each competitor offers |
| Pricing | Cost structure |
| Target | Customer segments |
| Strengths | What they do well |
| Weaknesses | Gaps and vulnerabilities |
| Market share | Position in market |

## Output Format

```json
{
  "market": "AI Coding Assistants",
  "competitors": [
    {
      "name": "GitHub Copilot",
      "strengths": ["Microsoft integration", "Large user base"],
      "weaknesses": ["Limited languages", "Expensive"],
      "market_share": "60%",
      "pricing": "$10/mo"
    },
    {
      "name": "Cursor",
      "strengths": ["Fast", "Good UX"],
      "weaknesses": ["New player", "Limited integrations"],
      "market_share": "5%",
      "pricing": "$20/mo"
    }
  ],
  "positioning": {
    "our_strength": "Better accuracy, cheaper",
    "market_gap": "Enterprise features",
    "strategy": "Focus on enterprise segment"
  },
  "recommendations": [
    "Build enterprise security features",
    "Partner with IDE vendors"
  ]
}
```

## Memory Storage

- entity_type: "competitive_analysis"
- tags: "business,competition,{market}"
