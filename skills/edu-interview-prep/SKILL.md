---
name: edu-interview-prep
description: |
  Prepare for educational program interviews.
  Generate questions, mock interviews, preparation plans.
  Use when: (1) User has interview coming up, (2) Need practice questions,
  (3) Preparing for technical interviews, (4) Behavioral questions.
  
  Input: Program details + CV
  Output: Questions + answers + prep plan
  Hashtags: #edu #интервью #подготовка #собеседование
---

# EduInterviewPrep Skill

## Workflow

1. **Program analysis**: Extract focus areas
2. **CV review**: Identify talking points
3. **Question generation**: Technical + behavioral
4. **Answer preparation**: Model answers
5. **Mock interview**: Practice session
6. **Feedback**: Areas to improve

## Question Types

| Type | Examples |
|------|----------|
| Technical | "Explain backpropagation", "Compare CNN vs RNN" |
| Behavioral | "Why this program?", "Tell me about a challenge" |
| Research | "Describe your research interests" |
| Situational | "How would you handle X?" |

## Output Format

```json
{
  "program": "MIT MSRP 2026",
  "questions": [
    {
      "type": "technical",
      "question": "Explain your approach to [project]",
      "model_answer": "[generated answer]",
      "tips": ["Focus on methodology", "Mention results"]
    }
  ],
  "prep_plan": [
    "Day 1: Review CV and projects",
    "Day 2: Practice technical questions",
    "Day 3: Mock interview"
  ],
  "common_mistakes": [
    "Not knowing program details",
    "Vague answers about motivation"
  ]
}
```

## Memory Storage

- entity_type: "interview_prep"
- tags: "edu,interviews,{program}"
