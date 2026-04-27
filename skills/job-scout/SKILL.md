---
name: job_scout
description: |
  Search for job opportunities: AI Engineer, Backend, DevOps, Platform.
  Use when: (1) Daily cron at 10:00, (2) User asks about jobs, 
  (3) Need to match CV with openings, (4) Update career knowledge base.
  
  Agent: JobScout
  Schedule: 0 10 * * * (daily 10:00 MSK)
  Output: HTML digest + Telegram message + knowledge base update
  Hashtags: #career #работа #вакансия #AI #backend #devops
---

# JobScout Skill

## Workflow

1. **web_search**: Find job openings (LinkedIn, AngelList, company careers)
2. **deep_research**: Extract requirements, salary, location, tech stack
3. **CV matching**: Compare with parsed CV from knowledge base
4. **Store in memory**: Save to MEM0 with category "career_jobs"
5. **Generate digest**: HTML + Telegram format

## Search Queries

- "AI Engineer job opening {date}"
- "Backend Engineer hiring remote"
- "DevOps Platform Engineer vacancy"
- "Machine Learning Engineer {location}"

## Output Format

```json
{
  "jobs": [
    {
      "title": "AI Engineer",
      "company": "OpenAI",
      "location": "San Francisco / Remote",
      "salary": "$200K-$400K",
      "requirements": ["Python", "PyTorch", "LLMs"],
      "url": "https://...",
      "cv_match_score": 85
    }
  ]
}
```

## CV Matching

Use cv_parser skill to extract from user's CV:
- Skills
- Experience
- Education
- Projects

Calculate match score based on:
- Skill overlap (50%)
- Experience relevance (30%)
- Education fit (20%)

## Memory Storage

- user_id: "ai_office"
- categories: ["career", "jobs", "{role}"]
- metadata: {date, company, role, location, salary, match_score}
