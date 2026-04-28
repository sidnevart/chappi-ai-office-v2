---
name: eval-runner
description: Use when running comprehensive eval tests on skills and reporting results
---

# Eval Runner

## Overview

Runs comprehensive eval tests for all skills and produces HTML report with results.

## Capabilities

1. **Parse eval YAML** — reads eval definitions
2. **Test skills** — checks skill markdown against eval criteria
3. **Generate report** — HTML report with pass/fail/status
4. **Identify gaps** — finds missing skills, tests, coverage

## Test Categories

### 1. Evidence Quality (weight 40%)
- Source URL present
- Calculation method shown
- Confidence levels
- Counter-evidence
- Source dates

### 2. Output Format (weight 25%)
- HTML generated (not JSON for humans)
- Proper structure (headings, tables)
- Professional styling
- Source citations

### 3. Language (weight 20%)
- Report in Russian
- Only proper nouns in English
- No English paragraphs
- Metrics in original language

### 4. Completeness (weight 15%)
- All required sections present
- All artifacts generated
- S3 upload confirmed
- Telegram notification sent

## Running Tests

```bash
# Run all evals
python3 /opt/openclaw-stack/workspace/skills/eval-runner/run_evals.py

# Run specific skill
python3 run_evals.py --skill trend-monitor

# Run with verbose output
python3 run_evals.py --verbose
```

## Report Format

```html
<h1>Eval Results — 2026-04-28</h1>
<div class="summary">
  <p>Total Skills: 25</p>
  <p>Total Tests: 500</p>
  <p>Passed: 480 (96%)</p>
  <p>Failed: 15 (3%)</p>
  <p>Skipped: 5 (1%)</p>
</div>

<div class="skill-result">
  <h2>trend-monitor</h2>
  <p>Tests: 18 | Passed: 18 | Failed: 0 | Score: 100%</p>
  
  <div class="test-details">
    <div class="test-pass">✅ evidence-source-url</div>
    <div class="test-pass">✅ evidence-calculation</div>
    ...
  </div>
</div>
```

## Continuous Testing

Run daily via cron:
```
0 3 * * * python3 /opt/openclaw-stack/workspace/skills/eval-runner/run_evals.py --report
```

Send results to Telegram if failures > 0.
