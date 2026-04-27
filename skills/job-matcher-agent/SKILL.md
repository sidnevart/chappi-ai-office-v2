---
name: job-matcher-agent
description: Agent skill for JobMatcher. Matches user CV with job openings and ranks by relevance.
---

# JobMatcher Agent

## Purpose

Weekly agent that matches user's CV with job openings and ranks by relevance.

## Trigger

- Schedule: Weekly (cron configured in OpenClaw)
- Target: isolated session

## Inputs

- `/mnt/files/research-state/career/jobs.json`
- User's CV

## Output

Writes findings to `/mnt/files/research-state/career/matched_jobs.json`

## Process

1. Read job openings
2. Read user's CV
3. Match CV skills with job requirements
4. Calculate relevance score
5. Identify gaps
6. Rank and save

## Output Format

```json
{
  "scan_date": "2026-04-27",
  "source": "JobMatcher",
  "matches": [
    {
      "title": "AI Engineer",
      "company": "TechCorp",
      "match_score": 0.88,
      "matching_skills": ["Python", "ML"],
      "missing_skills": ["Kubernetes"],
      "salary_range": "£80k-120k",
      "recommendation": "Apply - good match"
    }
  ],
  "top_picks": ["TechCorp AI Engineer"]
}
```

## Commands

When triggered, run:
1. Read state files
2. Read CV
3. Match and rank
4. Save results
5. Send digest
