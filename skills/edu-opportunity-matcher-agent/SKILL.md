---
name: edu-opportunity-matcher-agent
description: Agent skill for EduOpportunityMatcher. Matches user CV with educational programs and ranks by relevance.
---

# EduOpportunityMatcher Agent

## Purpose

Weekly agent that matches user's CV with educational programs (bootcamps, summer schools, grants) and ranks by relevance.

## Trigger

- Schedule: Weekly (cron configured in OpenClaw)
- Target: isolated session

## Inputs

- `/mnt/files/research-state/edu/bootcamps.json`
- `/mnt/files/research-state/edu/competitions.json`
- `/mnt/files/research-state/edu/grants.json`
- User's CV

## Output

Writes findings to `/mnt/files/research-state/edu/matched_opportunities.json`

## Process

1. Read all educational opportunities
2. Read user's CV
3. Match CV skills with program requirements
4. Calculate relevance score
5. Identify gaps
6. Rank and save

## Output Format

```json
{
  "scan_date": "2026-04-27",
  "source": "EduOpportunityMatcher",
  "matches": [
    {
      "program_name": "EEML Summer School",
      "type": "summer_school",
      "match_score": 0.92,
      "matching_skills": ["Python", "ML"],
      "missing_skills": ["Deep Learning"],
      "deadline": "2026-05-15",
      "recommendation": "Apply - strong match"
    }
  ],
  "top_picks": ["EEML Summer School", "Stanford OVAL"]
}
```

## Commands

When triggered, run:
1. Read state files
2. Read CV
3. Match and rank
4. Save results
5. Send digest
