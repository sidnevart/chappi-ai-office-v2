---
name: edu-competition-scout-agent
description: Agent skill for EduCompetitionScout. Runs daily to find competitions like Yandex Cup, ICSC, IAAC matching user's level.
---

# EduCompetitionScout Agent

## Purpose

Daily research agent that finds programming and AI competitions matching user's skill level.

## Trigger

- Schedule: `0 9 * * *` (daily at 09:00 Europe/Moscow)
- Target: isolated session

## Output

Writes findings to `/mnt/files/research-state/edu/competitions.json`

## Process

1. Search for competitions using web search
2. Focus: Yandex Cup, ICSC, IAAC, Kaggle, Google Code Jam
3. Filter by user's skill level
4. Extract: name, type, deadline, prizes, requirements, URL
5. Rank by relevance
6. Save structured JSON

## Output Format

```json
{
  "scan_date": "2026-04-27",
  "source": "EduCompetitionScout",
  "competitions": [
    {
      "name": "Yandex Cup 2026",
      "type": "programming",
      "level": "advanced",
      "prizes": "$50k total",
      "deadline": "2026-05-30",
      "requirements": ["Algorithms", "Data Structures"],
      "url": "https://yandex.com/cup",
      "relevance_score": 0.85,
      "status": "new"
    }
  ],
  "new_count": 2,
  "total_count": 8
}
```

## Commands

When triggered, run:
1. Use `web_search` to find competitions
2. Use `web_fetch` for details
3. Save to state directory
4. Send digest
