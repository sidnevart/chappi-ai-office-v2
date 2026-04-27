---
name: job-interview-prep
description: |
  Prepare for job interviews: technical questions, behavioral, system design.
  Use when: (1) User has interview coming up, (2) Need practice,
  (3) Preparing for specific company, (4) Technical deep-dive.
  
  Input: Company + Role + CV
  Output: Questions + answers + prep plan
  Hashtags: #career #интервью #собеседование #подготовка
---

# JobInterviewPrep Skill

## Workflow

1. **Company research**: Interview style, focus areas
2. **Role analysis**: Key competencies
3. **CV review**: Talking points
4. **Question generation**: Technical + behavioral + system design
5. **Answer prep**: Model answers
6. **Mock interview**: Practice session

## Question Categories

| Type | Examples |
|------|----------|
| Algorithm | "Implement LRU cache", "Binary tree traversal" |
| System Design | "Design Twitter", "Design URL shortener" |
| ML | "Explain gradient descent", "Bias vs Variance" |
| Behavioral | "Tell me about a conflict", "Why this company?" |
| Culture | "How do you handle feedback?" |

## Output Format

```json
{
  "company": "OpenAI",
  "role": "AI Engineer",
  "questions": [
    {
      "type": "technical",
      "difficulty": "medium",
      "question": "Explain transformer architecture",
      "model_answer": "[detailed answer]",
      "follow_ups": ["How would you optimize?", "Scaling laws?"]
    }
  ],
  "system_design": [
    "Design a recommendation system",
    "Design model serving infrastructure"
  ],
  "prep_plan": [
    "Day 1: Review algorithms",
    "Day 2: System design practice",
    "Day 3: Mock interview"
  ],
  "company_specific": {
    "focus_areas": ["LLMs", "Safety", "Scaling"],
    "recent_papers": ["GPT-4", "Constitutional AI"]
  }
}
```

## Memory Storage

- entity_type: "interview_prep"
- tags: "career,interviews,{company}"
