---
name: s3-uploader
description: Use when uploading files to S3-compatible storage and generating public URLs
---

# S3 Uploader

## Overview

Uploads files to MinIO S3 and returns public URLs. Used by other skills for sharing artifacts.

## When to Use

- After generating HTML reports
- After creating Excel models
- After writing Markdown specs
- When user asks for "share" or "public link"

**When NOT to use:**
- Local file operations → use bash/write tools
- Before generating content → generate first, then upload

## Configuration

```yaml
# ~/.openclaw/skills/s3-uploader/config.yaml
s3:
  endpoint: "http://127.0.0.1:9000"
  region: "us-east-1"
  bucket: "ai-office"
  access_key: "minio"
  secret_key: "${MINIO_ROOT_PASSWORD}"
```

## Workflow

### 1. Upload File

```python
import boto3
from botocore.config import Config

s3 = boto3.client('s3',
    endpoint_url='http://127.0.0.1:9000',
    aws_access_key_id='minio',
    aws_secret_access_key='${MINIO_ROOT_PASSWORD}',
    config=Config(signature_version='s3v4'),
    region_name='us-east-1'
)

# Upload with correct content type
s3.put_object(
    Bucket='ai-office',
    Key='reports/report.html',
    Body=open('/path/to/report.html', 'rb'),
    ContentType='text/html'
)

# Generate URL
url = f"http://80.74.25.43:9000/ai-office/reports/report.html"
```

### 2. Content Types

| File | Content-Type |
|------|-------------|
| HTML | text/html |
| JSON | application/json |
| PDF | application/pdf |
| Excel | application/vnd.openxmlformats-officedocument.spreadsheetml.sheet |
| Markdown | text/markdown |
| Images | image/png, image/jpeg |

### 3. Batch Upload

```python
files = [
    ('reports/report.html', 'text/html'),
    ('reports/model.xlsx', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
    ('tech-specs/spec.md', 'text/markdown'),
]

for local_path, content_type in files:
    s3.put_object(
        Bucket='ai-office',
        Key=local_path,
        Body=open(f'/mnt/files/research-state/{local_path}', 'rb'),
        ContentType=content_type
    )
```

## Output

```json
{
  "uploaded": true,
  "url": "http://80.74.25.43:9000/ai-office/reports/report.html",
  "key": "reports/report.html",
  "size": 4575,
  "content_type": "text/html"
}
```

## Best Practices

- ✅ Always set correct Content-Type
- ✅ Use consistent key structure: `{type}/{project}-{date}.{ext}`
- ✅ Verify upload succeeded (check response)
- ❌ Don't upload without content type
- ❌ Don't use inconsistent naming

## Commands

```bash
# Upload single file
python3 skills/s3-uploader/upload.py --file=report.html --key=reports/report.html

# Batch upload
python3 skills/s3-uploader/upload.py --batch=upload-list.json

# Verify
python3 skills/s3-uploader/verify.py --key=reports/report.html
```
