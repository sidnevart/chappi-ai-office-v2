---
name: weekly_matcher
description: |
  Match CV with opportunities weekly: programs + jobs.
  Use when: (1) Weekly cron at Monday 11:00, (2) User asks for recommendations, 
  (3) Need personalized digest based on CV.
  
  Agent: WeeklyMatcher
  Schedule: 0 11 * * 1 (Monday 11:00 MSK)
  Output: Personalized HTML digest + Telegram message
  Hashtags: #career #edu #matcher #рекомендации
---

# WeeklyMatcher Skill

## Workflow

1. **Retrieve from MEM0**: Get latest CV, jobs, programs
2. **Semantic search**: Find best matches using vector similarity
3. **Rank**: Sort by relevance score
4. **Generate personalized digest**: HTML + Telegram
5. **Send to Telegram**: Via TELEGRAM_SEND_MESSAGE

## Matching Logic

| Factor | Weight |
|--------|--------|
| Skills overlap | 40% |
| Experience relevance | 25% |
| Education fit | 20% |
| Location preference | 10% |
| Deadline urgency | 5% |

## Output Format

```json
{
  "matches": [
    {
      "opportunity": "MIT MSRP 2026",
      "type": "program",
      "score": 92,
      "reasons": ["Strong ML background", "Research experience"],
      "action": "Apply before Dec 1"
    }
  ],
  "summary": {
    "total_matches": 5,
    "high_priority": 2,
    "apply_this_week": 1
  }
}
```

## Memory Storage

- user_id: "ai_office"
- categories: ["matcher", "recommendations"]
- metadata: {date, total_matches, high_priority}
