---
name: job-networking
description: |
  Find contacts and referrals for job opportunities.
  Use when: (1) User asks for referrals, (2) Need warm introductions,
  (3) Building professional network, (4) Informational interviews.

  Input: Company + Role
  Output: Contact list + outreach templates
  Hashtags: #career #networking #контакты #реферал
---

# JobNetworking Skill

## Workflow

1. **Company research**: Find employees in target roles
2. **LinkedIn search**: Find 2nd degree connections
3. **Alumni search**: University/school connections
4. **Outreach templates**: Personalized messages
5. **Follow-up**: Sequence planning

## Contact Types

| Type | How to Find |
|------|-------------|
| Recruiters | LinkedIn, company careers |
| Hiring managers | Team pages, LinkedIn |
| Alumni | University networks |
| Mutual connections | LinkedIn 2nd degree |

## Output Format

```json
{
  "company": "OpenAI",
  "role": "AI Engineer",
  "contacts": [
    {
      "name": "John Doe",
      "role": "Senior AI Engineer",
      "connection": "2nd degree via MIT",
      "linkedin": "https://linkedin.com/in/...",
      "outreach_template": "Hi John, I noticed we both..."
    }
  ],
  "alumni": [
    {"name": "Jane Smith", "year": "2020", "current_role": "Engineering Manager"}
  ],
  "outreach_sequence": [
    "Day 1: Initial connection request",
    "Day 3: Follow-up with value",
    "Day 7: Ask for informational interview"
  ],
  "informational_interview_questions": [
    "What does a typical day look like?",
    "What are the biggest challenges?"
  ]
}
```

## Memory Storage

- entity_type: "network_contact"
- tags: "career,networking,{company}"
