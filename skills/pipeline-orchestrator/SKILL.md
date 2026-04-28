---
name: pipeline-orchestrator
description: Orchestrates the complete research pipeline with error handling, quality gate, and S3 upload. Use for ANY pipeline run.
---

# Pipeline Orchestrator

## Overview

Runs the complete research pipeline with:
- Error handling (retry, fallback)
- Quality gate (before Telegram)
- S3 upload (after each step)
- Vector DB storage (after each step)

## Pipeline

```
Input: Company/Idea Name
  ↓
CompanyAnalyst
  ↓ (on error → retry → skip → fallback)
CompetitiveStrategist
  ↓
IdeaGenerator
  ↓
RussianMarketAnalyst
  ↓
FundingScout
  ↓
FinancialModeler
  ↓
PitchBuilder
  ↓
TechSpecWriter
  ↓
QualityGate (check HTML before Telegram)
  ↓
S3 Upload (all artifacts)
  ↓
TelegramReporter
```

## Error Handling

### Per-Step Retry

```python
def run_step(step_name, skill_name, input_data, max_retries=2):
    for attempt in range(max_retries + 1):
        try:
            result = run_skill(skill_name, input_data)
            store_in_vector_db(result)
            upload_to_s3(result)
            return result
        except Exception as e:
            log_error(step_name, attempt, e)
            if attempt < max_retries:
                sleep(2 ** attempt)  # Exponential backoff
            else:
                return fallback_result(step_name)
```

### Fallback Strategy

| Step | Fallback |
|------|----------|
| CompanyAnalyst | Use cached data from VectorDB |
| CompetitiveStrategist | Generate basic strategy |
| IdeaGenerator | Use previous idea |
| RussianMarket | Skip (not critical) |
| FundingScout | Use known investors |
| FinancialModeler | Use cached model |
| PitchBuilder | Generate basic pitch |
| TechSpecWriter | Skip (not critical) |
| Telegram | Log to file, retry later |

## Quality Gate

```python
def check_quality(html_report):
    checks = {
        'min_length': len(html_report) > 500,
        'has_sources': 'http' in html_report,
        'has_russian': any(c in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' for c in html_report),
        'has_sections': html_report.count('<h2>') >= 2,
        'has_tables': '<table>' in html_report,
    }
    
    score = sum(checks.values()) / len(checks)
    
    if score >= 0.9:
        return 'PASS', score
    elif score >= 0.7:
        return 'WARNING', score
    else:
        return 'FAIL', score
```

## S3 Upload

```python
def upload_artifacts(artifacts):
    s3 = boto3.client('s3', endpoint_url='http://127.0.0.1:9000',
                      aws_access_key_id='minio',
                      aws_secret_access_key='minio123')
    
    for artifact in artifacts:
        s3.put_object(Bucket='ai-office', Key=artifact['key'],
                      Body=artifact['content'],
                      ContentType=artifact['type'])
```

## Integration

Every skill MUST use this orchestrator:

```python
from pipeline_orchestrator import run_step

result = run_step('company_analyst', 'company-analyst-agent',
                  {'company': 'OpenAI'},
                  max_retries=2)
```

## Best Practices

- ✅ Retry with exponential backoff
- ✅ Fallback to cached data
- ✅ Quality gate before Telegram
- ✅ S3 upload after each step
- ✅ Vector DB storage
- ❌ Never fail the whole pipeline
- ❌ Never skip quality gate
- ❌ Never lose data
