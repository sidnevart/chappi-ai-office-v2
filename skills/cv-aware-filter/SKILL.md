---
name: cv-aware-filter
description: Use when filtering opportunities based on CV profile match scoring
---

# CV-Aware Filter

## Overview

Before ANY opportunity is included in report, it MUST pass CV match filter.
Loads Artem's CV profile and calculates match score for every item.

## Input
- CV profile: `/mnt/files/research-state/cv_profile.json`
- Opportunity list (jobs/bootcamps/competitions/grants)

## Output
- Filtered list with match scores
- Skip items with score < 50%
- Add match details to report

## Match Scoring

### Technology Match (40%)
```python
def tech_match(required_skills, cv_skills):
    required_set = set(required_skills)
    cv_set = set(cv_skills)
    match = len(required_set & cv_set)
    return (match / len(required_set)) * 100 if required_set else 100
```

### Level Match (30%)
| Required | CV Years | Score |
|----------|----------|-------|
| Junior (0-2y) | 3y | 100% |
| Middle (2-5y) | 3y | 90% |
| Senior (5+y) | 3y | 50% |
| Lead (7+y) | 3y | 30% |

### Location Match (15%)
| Required | CV Pref | Score |
|----------|---------|-------|
| Remote | Remote | 100% |
| Remote | EU | 80% |
| Office Moscow | Remote | 20% |
| Office EU | EU | 100% |

### Salary Match (15%)
| Offered | Target | Score |
|---------|--------|-------|
| > $150K | EU remote | 100% |
| $100-150K | EU remote | 80% |
| $60-100K | EU remote | 50% |
| < $60K | EU remote | 20% |

## Filter Rules

- Score >= 80%: ✅ Strong match (highlight)
- Score 60-79%: ⚠️ Partial match (include with notes)
- Score 50-59%: ⚠️ Weak match (include if interesting)
- Score < 50%: ❌ Skip (don't include)

## CV Profile (cached)

```json
{
  "name": "Artem Sidnev",
  "role": "Software Engineer (Backend)",
  "experience_years": 3,
  "skills": ["Java", "Kotlin", "Go", "Python", "TypeScript", 
             "Spring Boot", "PostgreSQL", "ClickHouse", "Redis", "Kafka",
             "GitLab CI", "n8n", "RAG", "AI agents"],
  "languages": ["Russian", "English"],
  "location_preference": "Remote / EU / UK",
  "current_company": "T-Bank"
}
```

## Best Practices

- ✅ Always load CV before filtering
- ✅ Show match score for every item
- ✅ Explain why item was filtered
- ✅ Include tech gap analysis for partial matches
- ❌ Never include items without score
- ❌ Never skip without reason
