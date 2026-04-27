---
name: edu_bootcamp_scout
description: |
  Search for educational programs: bootcamps, summer schools, research programs.
  Use when: (1) Daily cron at 09:30, (2) User asks about education, 
  (3) Need to match CV with programs, (4) Update edu knowledge base.
  
  Agent: EduBootcampScout
  Schedule: 30 9 * * * (daily 09:30 MSK)
  Output: HTML digest + Telegram message + knowledge base update
  Hashtags: #edu #образование #буткемп #стажировка #грант
---

# EduBootcampScout Skill

## Workflow

1. **web_search**: Find programs (MIT, Stanford, CMU, ETH, etc.)
2. **deep_research**: Extract deadlines, requirements, funding, location
3. **CV matching**: Compare with user's CV
4. **Store in memory**: Save to MEM0 with category "edu_programs"
5. **Generate digest**: HTML + Telegram format

## Search Queries

- "summer research program 2026 AI machine learning"
- "bootcamp AI engineering 2026 application"
- "PhD fellowship computer science 2026"
- "research internship 2026 deadline"

## Program Types

| Type | Examples |
|------|----------|
| Summer Schools | MIT MSRP, Stanford UGRR, CMU RISS |
| Bootcamps | 42 School, Recurse Center, Y Combinator |
| Fellowships | OpenAI Fellowship, Facebook AI Residency |
| Internships | SpaceX, DeepMind, Google Research |

## Output Format

```json
{
  "programs": [
    {
      "name": "MIT Summer Research Program",
      "type": "Summer School",
      "location": "Cambridge, MA",
      "deadline": "2026-12-01",
      "funding": "$5K stipend",
      "requirements": ["Python", "ML basics"],
      "url": "https://...",
      "cv_match_score": 90
    }
  ]
}
```

## Memory Storage

- user_id: "ai_office"
- categories: ["edu", "programs", "{type}"]
- metadata: {date, name, type, deadline, funding, match_score}
