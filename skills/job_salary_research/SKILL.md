---
name: job_salary_research
description: |
  Research salary ranges for roles, locations, and experience levels.
  Use when: (1) User asks about compensation, (2) Negotiating offer,
  (3) Comparing markets, (4) Budget planning.

  Input: Role + Location + Level
  Output: Salary range + sources + trends
  Hashtags: #career #salary #зарплата #компенсация
---

# JobSalaryResearch Skill

## Workflow

1. **web_search**: Find salary data (Levels.fyi, Glassdoor, PayScale)
2. **deep_research**: Extract ranges, trends, factors
3. **Analysis**: Compare across companies, locations
4. **Report**: Range + negotiation tips

## Data Sources

| Source | Type |
|--------|------|
| Levels.fyi | Tech companies |
| Glassdoor | General market |
| PayScale | Role-based |
| Blind | Anonymous data |

## Output Format

```json
{
  "role": "AI Engineer",
  "location": "San Francisco",
  "level": "L4 (Senior)",
  "salary_range": {
    "base": "$180K - $250K",
    "total": "$300K - $450K",
    "equity": "$100K - $200K/year"
  },
  "by_company": {
    "OpenAI": "$350K - $500K",
    "Google": "$300K - $400K",
    "Startup": "$200K - $300K"
  },
  "trends": "+15% YoY for AI roles",
  "negotiation_tips": [
    "Highlight LLM experience",
    "Compare with market data",
    "Consider equity vs cash"
  ]
}
```

## Memory Storage

- entity_type: "salary_data"
- tags: "career,salary,{role},{location}"
