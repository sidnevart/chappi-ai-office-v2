---
name: quality-gate
description: Use when validating HTML reports before Telegram delivery. Blocks bad reports.
---

# Quality Gate

## Overview

Validates HTML reports before Telegram delivery.
**Blocks** reports that don't meet quality standards.

## Input
- HTML report path
- Skill name (who generated it)

## Output
- ✅ PASS — send to Telegram
- ❌ FAIL — block, log reason, notify admin

## CRITICAL: Never Skip

Every report MUST pass quality gate before Telegram.
No exceptions. No bypass.

## Validation Rules

### 1. Content Check (weight: 30%)

| Check | Min | Fail If |
|-------|-----|---------|
| Characters | 500 | < 500 chars |
| Sections | 3 | < 3 h2/h3 sections |
| Sources | 2 | < 2 URLs |
| Tables | 1 | No data tables |

### 2. Language Check (weight: 25%)

| Check | Rule | Fail If |
|-------|------|---------|
| Russian | 80%+ text in Russian | < 80% Russian |
| Proper nouns | Only metrics/companies in English | English paragraphs > 20% |
| Examples | Examples match rules | Wrong examples |

### 3. Evidence Check (weight: 25%)

| Check | Rule | Fail If |
|-------|------|---------|
| URLs valid | All URLs start with http | Invalid URLs |
| Sources cited | Every claim has source | Claims without source |
| Confidence | Confidence levels present | No confidence |
| Counter-evidence | Counter arguments exist | No counter-evidence |

### 4. Structure Check (weight: 20%)

| Check | Rule | Fail If |
|-------|------|---------|
| HTML valid | Has DOCTYPE, html, head, body | Broken HTML |
| CSS present | Has style or inline CSS | No styling |
| Responsive | Has viewport meta | No viewport |
| Encoding | UTF-8 specified | Wrong encoding |

## Scoring

```
Score = Content(30%) + Language(25%) + Evidence(25%) + Structure(20%)
```

| Score | Action |
|-------|--------|
| 90-100% | ✅ PASS — Send to Telegram |
| 70-89% | ⚠️ WARNING — Send with note "черновик" |
| 50-69% | ❌ FAIL — Block, return for revision |
| < 50% | ❌ FAIL — Block, log error |

## Workflow

### Step 1: Load Report
```python
html = load_report(report_path)
```

### Step 2: Run Checks
```python
checks = {
    'content': check_content(html),
    'language': check_language(html),
    'evidence': check_evidence(html),
    'structure': check_structure(html)
}
```

### Step 3: Calculate Score
```python
score = (
    checks['content'] * 0.30 +
    checks['language'] * 0.25 +
    checks['evidence'] * 0.25 +
    checks['structure'] * 0.20
)
```

### Step 4: Decide
```python
if score >= 90:
    return 'PASS', score
elif score >= 70:
    return 'WARNING', score
else:
    return 'FAIL', score
```

### Step 5: Log Result
```json
{
  "timestamp": "2026-04-28T02:30:00Z",
  "skill": "trend-monitor",
  "report": "trends-2026-04-28.html",
  "score": 85,
  "status": "WARNING",
  "failures": ["Only 1 source (min 2)"],
  "action": "Sent with 'черновик' note"
}
```

## Failure Examples

### FAIL: Empty Report
```
Score: 15%
Reason: 200 chars, 0 sources, no tables
Action: Blocked, logged
```

### FAIL: English Report
```
Score: 40%
Reason: 60% English text (should be < 20%)
Action: Blocked, returned for translation
```

### FAIL: No Evidence
```
Score: 35%
Reason: 0 URLs, no sources cited
Action: Blocked, returned for research
```

### WARNING: Draft Quality
```
Score: 75%
Reason: Only 2 sources (should be 3+)
Action: Sent with ⚠️ note
```

## Integration

Every agent MUST call quality-gate before Telegram:

```python
# In telegram-reporter
score, status = quality_gate.check(report_path)

if status == 'PASS':
    send_to_telegram(report)
elif status == 'WARNING':
    send_to_telegram(report + "\n⚠️ Черновик — требует доработки")
else:
    log_error(f"Report blocked: {failures}")
    # Don't send
```

## Best Practices

- ✅ Never bypass quality gate
- ✅ Log every check result
- ✅ Include specific failures in log
- ✅ Send warnings, block failures
- ❌ Never send FAIL reports
- ❌ Never skip quality gate
- ❌ Never hide failures
