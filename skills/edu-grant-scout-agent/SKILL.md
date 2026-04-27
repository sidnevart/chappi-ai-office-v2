---
name: edu-grant-scout-agent
description: Agent skill for EduGrantScout. Runs daily to find grants and scholarships for students and projects.
---

# EduGrantScout Agent

## Purpose

Daily research agent that finds grants and scholarships for students and projects.

## Trigger

- Schedule: Daily (cron configured in OpenClaw)
- Target: isolated session

## Output

Writes findings to `/mnt/files/research-state/edu/grants.json`

## Process

1. Search for grants using web search
2. Focus: student grants, research funding, project grants
3. Extract: name, amount, deadline, requirements, URL
4. Rank by relevance to user's profile
5. Save structured JSON

## Output Format

```json
{
  "scan_date": "2026-04-27",
  "source": "EduGrantScout",
  "grants": [
    {
      "name": "Google PhD Fellowship",
      "amount": "$50k/year",
      "deadline": "2026-06-01",
      "requirements": ["PhD student", "ML research"],
      "url": "https://example.com",
      "relevance_score": 0.80,
      "status": "new"
    }
  ],
  "new_count": 1,
  "total_count": 10
}
```

## Commands

When triggered, run:
1. Use `web_search` to find grants
2. Use `web_fetch` for details
3. Save to state directory
4. Send digest
