---
name: weekly-matcher
description: Use when matching CVs with opportunities using evidence-based scoring
---

# Weekly Matcher

## Overview

Matches CVs with opportunities and produces **HTML evidence report** with:
- Score breakdown with justification
- Skill gap analysis
- Recommendation with reasoning
- Market context

## Output

1. **HTML Report** (`reports/html/matches-YYYY-MM-DD.html`) — PRIMARY
2. **S3 Upload** → public URL
3. **Telegram** — notification with link

## Evidence Rules

Every match MUST have:
- **Score calculation**: How the score was derived
- **Skill mapping**: Which skills match
- **Gap analysis**: What's missing
- **Market context**: Salary, demand
- **Recommendation**: Why apply or not

## Workflow

### 1. Skill Extraction

From CV:
- Extract skills using NLP
- Categorize by level (expert/intermediate/beginner)
- Map to standard taxonomy

### 2. Job Analysis

For each job:
- Extract requirements
- Categorize (required/preferred/nice-to-have)
- Weight by importance

### 3. Score Calculation

```python
def calculate_match(cv_skills, job_requirements):
    scores = []
    for req in job_requirements:
        if req['skill'] in cv_skills:
            level_match = compare_levels(cv_skills[req['skill']], req['level'])
            scores.append(level_match * req['weight'])
        else:
            scores.append(0)
    
    return sum(scores) / sum(req['weight'] for req in job_requirements)
```

### 4. Market Context

For each match:
- Check salary ranges
- Check demand (number of openings)
- Check growth trend

### 5. Generate HTML Evidence Report

HTML with:
- Match cards with score breakdown
- Skill gap analysis
- Market context
- Recommendation with reasoning

## Best Practices

- ✅ Show score calculation
- ✅ Identify gaps
- ✅ Provide market context
- ✅ Give clear recommendation
- ❌ No score without calculation
- ❌ No recommendation without reasoning


## CRITICAL: Output Language

**ALL reports MUST be in Russian.**

- ✅ Report text, analysis, explanations — Russian
- ✅ Only proper nouns in English (company names, metrics)
- ✅ Source URLs can be in any language
- ❌ NEVER write full report in English
- ❌ NEVER send English analysis to Telegram (Russian users!)

### Examples

✅ **Correct:** "Рынок AI Meeting Assistants достиг $3.47B в 2025 году"
❌ **Wrong:** "AI Meeting Assistants market reached $3.47B in 2025"

✅ **Correct:** "LTV/CAC ratio составляет 10.8x"
❌ **Wrong:** "LTV/CAC ratio is 10.8x"

✅ **Correct:** "Источник: Grand View Research"
❌ **Wrong:** "Source: Grand View Research"
