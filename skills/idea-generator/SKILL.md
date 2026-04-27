---
name: idea-generator
description: |
  Generate and validate business ideas based on trends and problems.
  Use when: (1) User asks for ideas, (2) Need innovation,
  (3) Brainstorming session, (4) Startup ideation.

  Input: Problem / Trend / Market gap
  Output: List of ideas with validation scores
  Hashtags: #business #идеи #стартап #инновации
---

# IdeaGenerator Skill

## Workflow

1. **Trend analysis**: Identify emerging trends
2. **Problem identification**: Find pain points
3. **Idea generation**: Brainstorm solutions
4. **Validation**: Score each idea
5. **Deep dive**: Top ideas analysis

## Validation Criteria

| Criteria | Weight | Description |
|----------|--------|-------------|
| Market size | 25% | TAM/SAM/SOM |
| Feasibility | 20% | Technical complexity |
| Competition | 15% | Market saturation |
| Differentiation | 20% | Unique value |
| Timing | 10% | Market readiness |
| Team fit | 10% | Skills alignment |

## Output Format

```json
{
  "trend": "Physical AI",
  "ideas": [
    {
      "name": "Robotic warehouse assistant",
      "description": "AI-powered robot for warehouse automation",
      "score": 85,
      "breakdown": {
        "market_size": 90,
        "feasibility": 80,
        "competition": 70,
        "differentiation": 85,
        "timing": 90,
        "team_fit": 80
      },
      "market": "$50B TAM",
      "competitors": ["Locus Robotics", "6 River Systems"],
      "differentiation": "Cheaper, more flexible",
      "next_steps": [
        "Validate with 3 warehouses",
        "Build MVP in 3 months"
      ]
    }
  ],
  "recommendation": "Top idea: [name] with score [score]"
}
```

## Memory Storage

- entity_type: "idea"
- tags: "business,ideas,{trend}"
