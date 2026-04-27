---
name: s3-uploader
description: Use when uploading files to S3-compatible storage and generating public URLs for reports, pitches, and artifacts
---

# S3 Uploader

## Overview

Uploads files to S3-compatible storage (MinIO, AWS S3, Yandex Cloud) and returns public URLs. Used for publishing research artifacts.

## When to Use

- After generating HTML reports, pitches, or tech specs
- When user asks for "share this" or "public link"
- Pipeline final step: upload artifacts → get URLs

**When NOT to use:**
- Local file operations → use bash/write tools
- HTML generation → use html-builder or pitch-builder
- PDF conversion → use html-to-pdf

## Core Pattern

**Input:** Local file path
**Process:** Read config → Upload file → Generate URL → Update index
**Output:** JSON with URL, key, size

## Workflow

### 1. Configuration

```yaml
# ~/.openclaw/skills/s3-uploader/config.yaml
s3:
  endpoint: "https://s3.yandexcloud.net"
  region: "ru-central1"
  bucket: "chappi-ai-office"
  access_key: "${S3_ACCESS_KEY}"
  secret_key: "${S3_SECRET_KEY}"
```

### 2. Upload

```python
import boto3

s3 = boto3.client('s3', 
    endpoint_url='https://s3.yandexcloud.net',
    aws_access_key_id='...',
    aws_secret_access_key='...'
)

s3.upload_file(
    '/mnt/files/research-state/business/pitches/team-memory-ai.html',
    'chappi-ai-office',
    'pitches/team-memory-ai.html'
)

url = f"https://chappi-ai-office.s3.yandexcloud.net/pitches/team-memory-ai.html"
```

### 3. Update Index

```json
{
  "artifacts": [
    {
      "name": "team-memory-ai-pitch.html",
      "s3_url": "https://...",
      "local_path": "/mnt/files/...",
      "type": "pitch",
      "project": "team-memory-ai",
      "created": "2026-04-28T00:00:00Z"
    }
  ]
}
```

## Output Format

```json
{
  "uploaded": true,
  "url": "https://chappi-ai-office.s3.yandexcloud.net/pitches/team-memory-ai.html",
  "key": "pitches/team-memory-ai.html",
  "size": 4575,
  "content_type": "text/html"
}
```

## Quick Reference

| Action | Method |
|--------|--------|
| Upload file | boto3 upload_file |
| Generate URL | f-string with bucket + key |
| List artifacts | Read index JSON |

## Common Mistakes

- **Wrong endpoint:** Check region-specific endpoints
- **Missing permissions:** Verify bucket policy
- **No public access:** Enable public-read ACL
- **Not updating index:** Always record uploaded artifacts
