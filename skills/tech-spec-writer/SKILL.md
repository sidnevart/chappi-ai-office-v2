---
name: tech-spec-writer
description: Use when writing technical specifications and system architecture documents
---

# Tech Spec Writer

## Overview

Writes technical specifications. Output: **Markdown** (primary) + optional HTML for web viewing.

## Output Formats

1. **Markdown** (`/mnt/files/research-state/tech-specs/*.md`) — primary, human-readable
2. **HTML** (optional) — if web viewing needed
3. **S3 URL** — for sharing
4. **Telegram** — notification with link

## What This Skill Does NOT Produce

- ❌ JSON (tech specs are narrative documents)
- ❌ Excel (irrelevant for technical documentation)
- ❌ Google Sheets (irrelevant)

## Workflow

### Step 1: Write Markdown Spec

```markdown
# Technical Specification: TeamMemory AI

## 1. Overview
AI-платформа для командной памяти...

## 2. Architecture
```mermaid
[Diagram]
```

## 3. API Design
```http
POST /api/v1/ingest/message
```

## 4. Data Models
```json
{
  "Message": {
    "id": "uuid",
    "source": "telegram|meet|file"
  }
}
```

## 5. Security
- Auth: JWT + OAuth2
- Data: AES-256 at rest
- Transport: TLS 1.3

## 6. Tech Stack
| Component | Technology |
|-----------|------------|
| Backend | Python 3.12 + FastAPI |
| Vector DB | Qdrant |
| LLM | Ollama + LangChain |

## 7. Deployment
```yaml
# docker-compose.yml
```
```

### Step 2: Convert to HTML (optional)

```bash
# Using pandoc or similar
pandoc spec.md -o spec.html --css=style.css
```

### Step 3: Upload to S3

```python
import boto3
s3 = boto3.client('s3', endpoint_url='http://127.0.0.1:9000', ...)
s3.put_object(Bucket='ai-office', Key='tech-specs/team-memory-ai.md', Body=md_content, ContentType='text/markdown')
```

### Step 4: Send to Telegram

```
📝 Tech Spec: https://80.74.25.43:9000/ai-office/tech-specs/team-memory-ai.md
```

## Best Practices

- ✅ Write in Markdown (GitHub-friendly)
- ✅ Include diagrams (Mermaid)
- ✅ Code examples for API
- ✅ Security section mandatory
- ❌ Don't create JSON version
- ❌ Don't create Excel

## Commands

```bash
# Write spec
python3 skills/tech-spec-writer/write.py --idea=team-memory-ai

# Upload to S3
python3 skills/s3-uploader/upload.py --file=tech-specs/team-memory-ai.md

# Send to Telegram
python3 skills/telegram-reporter/send.py --message="📝 Tech Spec" --url=$URL
```
