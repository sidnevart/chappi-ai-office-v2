---
name: tech-spec-writer
description: Use when writing technical specifications, architecture documents, or system design docs for software products and features
---

# Tech Spec Writer

## Overview

Generates comprehensive technical specifications from business requirements. Includes architecture, API design, data models, and security.

## When to Use

- User asks for "technical specification" or "system design"
- Pipeline: idea → pitch → tech spec
- Planning MVP or feature development

**When NOT to use:**
- Business analysis → use idea-generator
- Pitch deck → use pitch-builder
- Code implementation → use coding-agent

## Core Pattern

**Input:** Business idea + requirements
**Process:** Design architecture → Define API → Model data → Plan security → Write spec
**Output:** Markdown spec document + S3 URL

## Workflow

### 1. Requirements

Read from state:
```
research-state/business/ideas/{idea}.json
research-state/business/pitches/{idea}.json
```

### 2. Architecture

```
[User] → [Telegram Bot] → [API Gateway] → [Services] → [DB]
                                    ↓
                              [Vector DB]
                                    ↓
                              [LLM/Ollama]
```

### 3. API Design

```http
POST /api/v1/ingest/message
Authorization: Bearer {token}
Content-Type: application/json

{
  "source": "telegram",
  "text": "...",
  "timestamp": "2026-04-28T00:00:00Z"
}
```

### 4. Data Models

```json
{
  "Message": {
    "id": "uuid",
    "source": "telegram|meet|file",
    "content": "text",
    "embedding": [0.1, 0.2, ...],
    "metadata": {
      "sender": "string",
      "timestamp": "datetime"
    }
  }
}
```

### 5. Security

- Auth: JWT + OAuth2
- Data: AES-256 at rest
- Transport: TLS 1.3
- Compliance: 152-FZ (Russia)

### 6. Write Spec

```
/mnt/files/research-state/tech-specs/{idea}.md
```

## Spec Sections

| Section | Content |
|---------|---------|
| Overview | 1-paragraph summary |
| Architecture | Diagram + description |
| Data Flow | Step-by-step |
| API Design | Endpoints, request/response |
| Data Models | JSON schemas |
| Tech Stack | Component → Technology |
| Security | Threat model + mitigations |
| Scalability | Performance targets |
| Deployment | Docker/Kubernetes config |
| MVP Scope | Phase 1-3 features |

## Quick Reference

| Action | Method |
|--------|--------|
| Read requirements | Read idea JSON |
| Design API | RESTful, versioned |
| Model data | Normalize, add indexes |
| Plan security | Threat modeling |

## Common Mistakes

- **Over-engineering:** MVP first, scale later
- **Missing auth:** Always plan authentication
- **No rate limits:** Essential for public APIs
- **Ignoring compliance:** Check regional requirements
