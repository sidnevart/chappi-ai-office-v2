---
name: job-cover-letter
description: |
  Generate tailored cover letters for job applications.
  Use when: (1) User asks for cover letter, (2) Applying to specific company,
  (3) Need personalized application documents.
  
  Input: CV + Job description + Company info
  Output: Cover letter draft
  Hashtags: #career #coverletter #сопроводительное #работа
---

# JobCoverLetter Skill

## Workflow

1. **CV analysis**: Extract key achievements
2. **Company research**: Mission, values, culture
3. **JD matching**: Align CV with requirements
4. **Letter generation**: Personalized draft
5. **Review**: Grammar, tone, length

## Structure

| Section | Content |
|---------|---------|
| Header | Contact info, date |
| Greeting | Hiring manager name |
| Opening | Hook + position |
| Body | Why you fit |
| Closing | Call to action |
| Signature | Professional sign-off |

## Output Format

```json
{
  "job": "AI Engineer at OpenAI",
  "cover_letter": "Dear Hiring Manager,\n\n[Generated personalized letter]",
  "highlights": [
    "3 years ML experience",
    "Led team of 5 engineers",
    "Published 2 papers"
  ],
  "customization": {
    "company_mission": "Aligned with OpenAI's mission",
    "role_alignment": "Perfect fit for AI Engineer role"
  }
}
```

## Memory Storage

- entity_type: "cover_letter"
- tags: "career,cover-letters,{company}"
