---
name: weekly-matcher-agent
description: Agent skill for WeeklyMatcher. Runs weekly to match user CV against educational programs and job openings, ranking by relevance.
---

# WeeklyMatcher Agent

## Purpose

Weekly agent that cross-references user's CV with found educational programs and job openings, ranking matches by relevance.

## Trigger

- Schedule: `0 11 * * 1` (weekly on Monday at 11:00 Europe/Moscow)
- Target: isolated session

## Inputs

- `/mnt/files/research-state/edu/bootcamps.json`
- `/mnt/files/research-state/edu/competitions.json`
- `/mnt/files/research-state/edu/grants.json`
- `/mnt/files/research-state/career/jobs.json`
- User's CV (from Google Drive or local)

## Outputs

- `/mnt/files/research-state/edu/matched_opportunities.json`
- `/mnt/files/research-state/career/matched_jobs.json`

## Process

1. Read all current opportunity data
2. Read user's CV
3. For each opportunity:
   - Extract required skills, experience, location
   - Compare with CV skills and experience
   - Calculate relevance score (0-1)
   - Identify gaps and missing requirements
4. Rank by relevance score
5. Generate personalized recommendations
6. Save structured JSON

## Output Format

```json
{
  "scan_date": "2026-04-27",
  "source": "WeeklyMatcher",
  "education_matches": [
    {
      "program_name": "EEML Summer School",
      "type": "summer_school",
      "match_score": 0.92,
      "matching_skills": ["Python", "ML", "PyTorch"],
      "missing_skills": ["Transformer architecture"],
      "recommendation": "Strong match - apply before deadline",
      "deadline": "2026-05-15"
    }
  ],
  "job_matches": [
    {
      "title": "AI Engineer",
      "company": "TechCorp",
      "match_score": 0.88,
      "matching_skills": ["Python", "ML", "AWS"],
      "missing_skills": ["Kubernetes"],
      "recommendation": "Good match - highlight MLops experience",
      "salary_range": "£80k-120k"
    }
  ],
  "top_recommendations": [
    "Apply to EEML Summer School (deadline: 2026-05-15)",
    "Follow up on TechCorp AI Engineer role"
  ]
}
```

## Commands

When triggered, run:
1. Read current data from state directories
2. Read user CV
3. Use matching logic (manual or skill-based)
4. Save results
5. Send personalized digest to Telegram
