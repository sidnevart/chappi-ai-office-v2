---
name: idea-generator-agent
description: Agent skill for IdeaGenerator. Generates and validates business ideas based on trends, problems, and market gaps.
---

# IdeaGenerator Agent

## Purpose

Creative agent that generates business ideas by combining trends, identifying problems, and validating market fit.

## Trigger

- User request: "Придумай идею в Physical AI"
- Cron: weekly idea generation from trend data

## Input

- `/mnt/files/research-state/business/trends.json`
- OR user prompt with specific domain

## Output

Writes to `/mnt/files/research-state/business/ideas/{idea_slug}.json`

## Process

1. Read trend data or user prompt
2. Identify pain points and gaps
3. Generate 5-10 ideas
4. Score each idea: market size, feasibility, competition
5. Validate with quick research
6. Save top ideas

## Output Format

```json
{
  "generation_date": "2026-04-27",
  "source": "IdeaGenerator",
  "trigger": "Physical AI trend",
  
  "ideas": [
    {
      "name": "AI-Powered Warehouse Robotics",
      "description": "Autonomous robots for warehouse picking",
      "problem": "Labor shortages in logistics",
      "market_size": "$50B+",
      "feasibility": 0.85,
      "competition": "high",
      "differentiation": "Modular design, quick deployment",
      "score": 8.5,
      "status": "new"
    }
  ],
  
  "top_idea": "AI-Powered Warehouse Robotics",
  "recommended_next_step": "Validate with 3 potential customers"
}
```

## Commands

When triggered, run:
1. Read trends or parse user prompt
2. Generate ideas with web search validation
3. Score and rank
4. Save results
5. Trigger CompetitiveStrategist for top idea
