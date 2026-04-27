---
name: job_cv_matcher
description: |
  Match CV with job descriptions. Calculate match score and gap analysis.
  Use when: (1) Weekly matcher cron, (2) User asks "am I fit for X job",
  (3) Need to compare CV with JD, (4) Generate recommendations.
  
  Input: CV data + Job description
  Output: Score (0-100) + gap analysis + recommendations
  Hashtags: #career #cv #matcher #вакансия #job
---

# JobCVMatcher Skill

## Workflow

1. **cv_parser**: Extract CV data
2. **JD analysis**: Extract requirements
3. **Match calculation**: Compare CV with JD
4. **Gap analysis**: Identify missing skills
5. **Recommendations**: Suggest improvements

## Matching Logic

| Factor | Weight | Description |
|--------|--------|-------------|
| Skills overlap | 40% | Required vs actual |
| Experience | 25% | Years, relevance |
| Education | 15% | Degree, field |
| Projects | 10% | Portfolio match |
| Culture fit | 10% | Company values |

## Output Format

```json
{
  "job": "AI Engineer at OpenAI",
  "match_score": 78,
  "breakdown": {
    "skills": 85,
    "experience": 70,
    "education": 80,
    "projects": 90,
    "culture": 65
  },
  "gaps": [
    "Missing distributed systems experience",
    "No PhD (preferred but not required)"
  ],
  "recommendations": [
    "Highlight LLM project experience",
    "Get recommendation from AI researcher"
  ],
  "priority": "medium"
}
```

## Memory Storage

- entity_type: "job_match"
- tags: "career,matcher,jobs"
