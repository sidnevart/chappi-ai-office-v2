---
name: edu-competition-scout
description: |
  Search for competitions and hackathons: Yandex Cup, ICSC, IAAC level.
  Use when: (1) Daily cron for new competitions, (2) User asks about contests,
  (3) Need to find competitive programming / ML challenges, (4) Update knowledge base.
  
  Agent: EduCompetitionScout
  Schedule: 0 9 * * * (daily 09:00 MSK)
  Output: HTML digest + Telegram message + knowledge base update
  Hashtags: #edu #соревнования #конкурс #AI #ML
---

# EduCompetitionScout Skill

## Workflow

1. **web_search**: Find competitions (Yandex Cup, ICSC, IAAC, hackathons)
2. **deep_research**: Extract prizes, deadlines, requirements, levels
3. **CV matching**: Compare with user's skills
4. **Store in memory**: Save to local-vector-db with category "edu_competitions"
5. **Generate digest**: HTML + Telegram format

## Search Queries

- "Yandex Cup 2026 registration"
- "ICSC competition 2026"
- "IAAC architecture competition 2026"
- "AI hackathon 2026"
- "machine learning competition deadline 2026"

## Competition Levels

| Level | Examples |
|-------|----------|
| International | ICSC, IAAC, ACM ICPC |
| National | Yandex Cup, VK Cup |
| Regional | Local hackathons |
| Student | University contests |

## Output Format

```json
{
  "competitions": [
    {
      "name": "Yandex Cup 2026",
      "level": "International",
      "prize": "$50K",
      "deadline": "2026-05-15",
      "requirements": ["Python", "ML basics"],
      "url": "https://...",
      "cv_match_score": 85
    }
  ]
}
```

## Memory Storage

- entity_type: "competition"
- tags: "edu,competitions,{level}"
