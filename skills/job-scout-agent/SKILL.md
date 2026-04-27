---
name: job-scout-agent
description: Agent skill for JobScout. Runs daily to find AI Engineer, Platform/DevOps, and Backend positions matching user's profile.
---

# JobScout Agent

## Purpose

Daily research agent that finds job openings for AI Engineer, Platform Engineer, DevOps, and Backend roles matching user's skills and preferences.

## Trigger

- Schedule: `0 10 * * *` (daily at 10:00 Europe/Moscow)
- Target: isolated session

## Output

Writes findings to `/mnt/files/research-state/career/jobs.json`

## Process

1. Search for job openings using web search
2. Focus on: AI Engineer, Platform, DevOps, Backend
3. Filter by user's preferences (location, level, company type)
4. Extract: title, company, location, requirements, salary range, URL
5. Deduplicate against existing jobs
6. Rank by relevance to user's CV
7. Save structured JSON

## Output Format

```json
{
  "scan_date": "2026-04-27",
  "source": "JobScout",
  "jobs": [
    {
      "title": "AI Engineer",
      "company": "TechCorp",
      "location": "London, UK",
      "type": "full_time",
      "level": "senior",
      "requirements": ["Python", "PyTorch", "MLops"],
      "salary_range": "£80k-120k",
      "url": "https://example.com",
      "relevance_score": 0.88,
      "status": "new"
    }
  ],
  "new_count": 4,
  "total_count": 23
}
```

## Commands

When triggered, run:
1. Use `web_search` to find current openings
2. Use `web_fetch` for detailed pages
3. Save to `/mnt/files/research-state/career/jobs.json`
4. Send summary to Telegram
