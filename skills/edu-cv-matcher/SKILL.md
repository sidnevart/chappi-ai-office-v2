---
name: edu-cv-matcher
description: |
  Match CV with educational program requirements. Calculate match score and gap analysis.
  Use when: (1) Weekly matcher cron, (2) User asks "am I eligible for X program",
  (3) Need to compare CV with program requirements, (4) Generate recommendations.
  
  Input: CV data + Program data
  Output: Score (0-100) + gap analysis + recommendations
  Hashtags: #edu #cv #matcher #рекомендации
---

# EduCVMatcher Skill

## Workflow

1. **cv_parser**: Extract CV data (skills, experience, education)
2. **Program analysis**: Extract requirements from program description
3. **Match calculation**: Compare CV with requirements
4. **Gap analysis**: Identify missing skills/experience
5. **Recommendations**: Suggest improvements

## Matching Logic

| Factor | Weight | Description |
|--------|--------|-------------|
| Skills overlap | 40% | Required vs actual skills |
| Education level | 25% | Degree, GPA, university |
| Experience | 20% | Years, relevance |
| Projects | 10% | Portfolio quality |
| Language | 5% | TOEFL/IELTS scores |

## Output Format

```json
{
  "program": "MIT MSRP 2026",
  "match_score": 85,
  "breakdown": {
    "skills": 90,
    "education": 80,
    "experience": 85,
    "projects": 90,
    "language": 80
  },
  "gaps": [
    "Need 2+ years ML experience (have 1.5)",
    "Missing publication record"
  ],
  "recommendations": [
    "Complete Kaggle competition",
    "Publish preprint on arXiv"
  ],
  "priority": "high"
}
```

## Memory Storage

- entity_type: "match_result"
- tags: "edu,matcher,cv"
