---
name: edu-bootcamp-scout-agent
description: Agent skill for EduBootcampScout. Runs daily to find bootcamps, summer schools, and educational programs matching user's profile.
---

# EduBootcampScout Agent

## Purpose

Daily research agent that finds bootcamps, summer schools, and educational programs in AI/ML, Software Engineering, and related fields.

## Trigger

- Schedule: `30 9 * * *` (daily at 09:30 Europe/Moscow)
- Target: isolated session

## Output

Writes findings to `/mnt/files/research-state/edu/bootcamps.json`

## Process

1. Search for bootcamps and summer schools using web search
2. Filter by: AI/ML, SWE, relevant to user's profile (from CV)
3. Extract: name, deadline, location, requirements, URL
4. Rank by relevance to user's skills and goals
5. Save structured JSON
6. Send digest to Telegram if new programs found

## Output Format

```json
{
  "scan_date": "2026-04-27",
  "source": "EduBootcampScout",
  "programs": [
    {
      "name": "EEML Summer School",
      "type": "summer_school",
      "field": "AI/ML",
      "location": "Virtual / Europe",
      "deadline": "2026-05-15",
      "requirements": ["Python", "ML basics"],
      "url": "https://example.com",
      "relevance_score": 0.92,
      "status": "new"
    }
  ],
  "new_count": 3,
  "total_count": 15
}
```

## Commands

When triggered, run:
1. Use `web_search` to find current bootcamps
2. Use `web_fetch` for detailed pages
3. Save to `/mnt/files/research-state/edu/bootcamps.json`
4. If new programs found, send summary to Telegram
