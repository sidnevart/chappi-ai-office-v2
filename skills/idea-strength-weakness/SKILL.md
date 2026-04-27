---
name: idea-strength-weakness
description: |
  Analyze strengths and weaknesses of existing solutions.
  Find gaps and opportunities.
  Use when: (1) User asks about product weaknesses, (2) Need to find opportunities,
  (3) Competitive analysis, (4) Innovation hunting.

  Input: Product / Service / Market
  Output: SWOT analysis + opportunities
  Hashtags: #business #анализ #слабые_стороны #возможности
---

# IdeaStrengthWeakness Skill

## Workflow

1. **Product analysis**: Current solutions in market
2. **User reviews**: Find complaints and praise
3. **Feature gaps**: Missing capabilities
4. **Pain points**: User frustrations
5. **Opportunities**: Potential improvements

## Analysis Framework

| Category | Questions |
|----------|-----------|
| Strengths | What do users love? |
| Weaknesses | What do users complain about? |
| Opportunities | What's missing? |
| Threats | What could disrupt? |

## Output Format

```json
{
  "product": "AI Coding Assistants",
  "swot": {
    "strengths": [
      "Fast code generation",
      "Good integration"
    ],
    "weaknesses": [
      "Hallucinations",
      "Limited context",
      "Expensive"
    ],
    "opportunities": [
      "Enterprise features",
      "Local deployment",
      "Better accuracy"
    ],
    "threats": [
      "Open source alternatives",
      "IDE native features"
    ]
  },
  "gaps": [
    "No local/self-hosted option",
    "Limited to specific IDEs",
    "No team collaboration"
  ],
  "opportunities": [
    {
      "idea": "Self-hosted AI coding assistant",
      "market": "Enterprise security-conscious",
      "difficulty": "Medium"
    }
  ]
}
```

## Memory Storage

- entity_type: "swot_analysis"
- tags: "business,swot,{product}"
