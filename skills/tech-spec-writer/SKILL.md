---
name: tech-spec-writer
description: |
  Write technical specifications for developers.
  Use when: (1) User asks for tech spec, (2) Product team needs docs,
  (3) Outsourcing development, (4) Internal planning.

  Input: Product vision + Requirements
  Output: Technical specification (Markdown/HTML)
  Hashtags: #business #техническое_задание #тз #specification
---

# TechSpecWriter Skill

## Workflow

1. **Product analysis**: Features, user stories
2. **Architecture**: System design
3. **API design**: Endpoints, schemas
4. **Database**: Schema, models
5. **Frontend**: Components, flows
6. **Backend**: Services, logic
7. **Output**: Markdown/HTML spec

## Spec Structure

| Section | Content |
|---------|---------|
| Overview | Project description |
| Goals | Objectives |
| Architecture | System diagram |
| API | Endpoints, requests, responses |
| Database | Schema, migrations |
| Frontend | Components, state |
| Backend | Services, business logic |
| Testing | Test plan |
| Deployment | CI/CD, infrastructure |
| Timeline | Milestones |

## Output Format

```json
{
  "project": "AI Assistant Platform",
  "spec": {
    "overview": "Platform for AI assistants",
    "architecture": "Microservices",
    "tech_stack": ["Python", "FastAPI", "PostgreSQL", "React"],
    "api": {
      "endpoints": [
        {
          "path": "/api/v1/assistants",
          "method": "GET",
          "description": "List assistants"
        }
      ]
    },
    "database": {
      "tables": ["users", "assistants", "conversations"]
    },
    "timeline": [
      {"week": 1, "task": "Setup infrastructure"},
      {"week": 2, "task": "Build API"}
    ]
  },
  "file": "/path/to/tech-spec.md"
}
```

## Memory Storage

- entity_type: "tech_spec"
- tags: "business,tech-specs,{project}"
