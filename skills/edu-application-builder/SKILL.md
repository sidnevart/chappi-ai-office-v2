---
name: edu-application-builder
description: |
  Help prepare application documents for educational programs.
  Generate checklists, draft essays, portfolio plans.
  Use when: (1) User asks "help me apply to X", (2) Need application package,
  (3) Preparing recommendation letters, (4) Timeline planning.
  
  Input: Program details + CV
  Output: Checklist + drafts + timeline
  Hashtags: #edu #заявка #документы #портфолио
---

# EduApplicationBuilder Skill

## Workflow

1. **Program analysis**: Extract requirements and deadlines
2. **CV review**: Identify strengths to highlight
3. **Checklist generation**: Required documents
4. **Essay drafts**: Personal statement, SOP
5. **Portfolio plan**: Projects to showcase
6. **Timeline**: Step-by-step schedule

## Output Format

```json
{
  "program": "MIT MSRP 2026",
  "checklist": [
    "✅ Transcript",
    "⏳ Personal Statement (due in 2 weeks)",
    "⏳ 2 Recommendation Letters",
    "⏳ Portfolio (3 projects)"
  ],
  "essays": {
    "personal_statement": "Draft: [generated text]",
    "sop": "Draft: [generated text]"
  },
  "portfolio_plan": [
    "Project 1: ML Research (highlight methodology)",
    "Project 2: Open Source Contribution",
    "Project 3: Kaggle Competition"
  ],
  "timeline": [
    {"week": 1, "task": "Finalize personal statement"},
    {"week": 2, "task": "Request recommendation letters"},
    {"week": 3, "task": "Prepare portfolio"},
    {"week": 4, "task": "Submit application"}
  ]
}
```

## Memory Storage

- entity_type: "application_package"
- tags: "edu,applications,{program}"
