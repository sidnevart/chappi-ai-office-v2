---
name: skill-evaluator
description: Use when testing skills, evaluating agent behavior against expected outputs, or validating skill quality through automated test cases
---

# Skill Evaluator

## Overview

Tests skills using evaluation cases (evals) to ensure agents produce expected behavior. Inspired by OpenAI Evals framework.

## When to Use

- After writing or editing a skill
- Before deploying a skill to production
- When agent behavior doesn't match expectations
- Periodic regression testing

**When NOT to use:**
- Testing code (not skills) → use unit tests
- Manual testing → run agent directly

## Core Pattern

**Input:** Skill name + eval cases
**Process:** Load skill → Run eval cases → Compare output → Report results
**Output:** JSON with pass/fail status for each case

## Eval Case Format

```yaml
# evals/trend-monitor-eval.yaml
eval_id: trend-monitor-basic
skill: trend-monitor
cases:
  - id: case-1
    name: "Detect AI trend"
    input:
      query: "What are latest AI trends?"
      context: "Research system"
    expected:
      - contains: "AI"
      - contains: "trend"
      - json_format: true
      - confidence_range: [0.5, 1.0]
    
  - id: case-2
    name: "Structure output"
    input:
      query: "Physical AI trends"
    expected:
      - has_fields: ["trend", "description", "sources", "confidence"]
      - sources_count: ">=2"
```

## Workflow

### 1. Create Eval Case

```yaml
# skills/trend-monitor/evals/basic.yaml
eval_id: trend-monitor-basic
skill: trend-monitor
description: "Basic functionality test"
cases:
  - id: detect-trend
    input: { query: "AI trends 2026" }
    expected:
      - contains: "trend"
      - json_output: true
```

### 2. Run Eval

```bash
openclaw skill eval trend-monitor --eval=basic
```

### 3. Check Results

```json
{
  "eval_id": "trend-monitor-basic",
  "skill": "trend-monitor",
  "passed": 5,
  "failed": 1,
  "total": 6,
  "cases": [
    {
      "id": "detect-trend",
      "status": "pass",
      "checks": [
        { "check": "contains('trend')", "status": "pass" },
        { "check": "json_output", "status": "pass" }
      ]
    }
  ]
}
```

## Check Types

| Check | Description | Example |
|-------|-------------|---------|
| `contains` | Output contains text | `contains: "AI"` |
| `has_fields` | JSON has fields | `has_fields: ["trend"]` |
| `json_format` | Valid JSON output | `json_format: true` |
| `confidence_range` | Value in range | `confidence_range: [0.5, 1.0]` |
| `sources_count` | Minimum sources | `sources_count: ">=2"` |
| `matches_regex` | Regex match | `matches_regex: ".*AI.*"` |
| `file_exists` | File created | `file_exists: "path/to/file"` |
| `file_contains` | File content | `file_contains: "text"` |

## Eval Categories

### Basic Evals
- Skill loads without errors
- Output format is correct
- Required fields present

### Functional Evals
- Business logic works
- Edge cases handled
- Error states managed

### Integration Evals
- Skill works with other skills
- Pipeline end-to-end works
- State files updated correctly

## Running Evals

```bash
# Single skill
openclaw skill eval trend-monitor

# All skills
openclaw skill eval --all

# Specific eval
openclaw skill eval trend-monitor --eval=basic

# With verbose output
openclaw skill eval trend-monitor --verbose
```

## Eval Results Location

```
/mnt/files/research-state/evals/
├── trend-monitor/
│   ├── basic-2026-04-28.json
│   └── advanced-2026-04-28.json
├── deal-flow-tracker/
│   └── basic-2026-04-28.json
└── summary.json
```

## Quick Reference

| Action | Command |
|--------|---------|
| Create eval | Write YAML to skills/{skill}/evals/ |
| Run eval | `openclaw skill eval {skill}` |
| Check results | Read JSON from research-state/evals/ |
| Fix failures | Update skill → re-run eval |

## Common Mistakes

- **No eval cases:** Every skill must have at least basic eval
- **Only happy path:** Test error cases too
- **Not updating evals:** Update when skill changes
- **Ignoring flakiness:** Mark known flaky tests
