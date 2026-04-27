---
name: edu_grant_scout
description: |
  Search for grants and scholarships for students and projects.
  Use when: (1) Daily cron at 09:00 to find new grants, (2) User asks about funding,
  (3) Need to find educational grants, research funding, (4) Update knowledge base.
  
  Agent: EduGrantScout
  Schedule: 0 9 * * * (daily 09:00 MSK)
  Output: HTML digest + Telegram message + knowledge base update
  Hashtags: #edu #грант #стипендия #фандинг #research
---

# EduGrantScout Skill

## Workflow

1. **web_search**: Find grants (NSF, ERC, Fulbright, local grants)
2. **deep_research**: Extract amounts, deadlines, eligibility, requirements
3. **CV matching**: Check eligibility
4. **Store in memory**: Save to local-vector-db with category "edu_grants"
5. **Generate digest**: HTML + Telegram format

## Search Queries

- "research grant 2026 AI machine learning"
- "student scholarship 2026"
- "PhD fellowship computer science 2026"
- "NSF grant deadline 2026"
- "ERC starting grant 2026"

## Grant Types

| Type | Examples |
|------|----------|
| Research | NSF, ERC, DARPA |
| Student | Fulbright, DAAD, Chevening |
| Project | Google Research, OpenAI Scholars |
| Travel | Conference grants |

## Output Format

```json
{
  "grants": [
    {
      "name": "NSF Graduate Research Fellowship",
      "amount": "$34K/year",
      "deadline": "2026-10-15",
      "eligibility": "US citizens, STEM grad students",
      "requirements": ["GPA 3.0+", "Research proposal"],
      "url": "https://...",
      "cv_match_score": 90
    }
  ]
}
```

## Memory Storage

- entity_type: "grant"
- tags: "edu,grants,{type}"
