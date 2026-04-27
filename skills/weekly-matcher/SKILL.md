---
name: weekly-matcher
description: Use when matching CVs with opportunities using evidence-based scoring
---

# Weekly Matcher (Evidence-Based)

## Overview

Matches CVs with opportunities and produces **HTML evidence document** with:
- Score breakdown with justification
- Skill gap analysis
- Recommendation with reasoning
- Market context

## Output Formats

1. **HTML Report** (`/mnt/files/research-state/reports/html/matches-*.html`) — PRIMARY
2. **S3 URL** — public access
3. **Telegram** — notification with link

## Evidence Requirements

Every match MUST have:
- **Score calculation**: How the score was derived
- **Skill mapping**: Which skills match
- **Gap analysis**: What's missing
- **Market context**: Salary, demand
- **Recommendation**: Why apply or not

## HTML Structure

```html
<h1>🎯 Weekly Matches</h1>

<div class="match">
  <h2>Match: AI Developer at Company</h2>
  
  <div class="score">
    <h3>Score: 92%</h3>
    <p><strong>Calculation:</strong></p>
    <ul>
      <li>Python: 100% match (CV: expert, Job: required)</li>
      <li>PyTorch: 80% match (CV: intermediate, Job: required)</li>
      <li>Experience: 100% match (CV: 3 years, Job: 2+ years)</li>
      <li>Location: 90% match (CV: remote, Job: hybrid)</li>
    </ul>
    <p><strong>Weighted average:</strong> (100 + 80 + 100 + 90) / 4 = 92.5%</p>
  </div>
  
  <div class="gaps">
    <h3>Skill Gaps</h3>
    <ul>
      <li>TensorFlow: Not in CV (Job: preferred)</li>
      <li>Kubernetes: Not in CV (Job: nice-to-have)</li>
    </ul>
  </div>
  
  <div class="market">
    <h3>Market Context</h3>
    <p><strong>Salary:</strong> $120K-$150K (Source: Glassdoor, LinkedIn)</p>
    <p><strong>Demand:</strong> High (1,133 openings in London)</p>
    <p><strong>Trend:</strong> +15% YoY growth</p>
  </div>
  
  <div class="recommendation">
    <h3>Recommendation: APPLY</h3>
    <p><strong>Why:</strong> 92% match, high salary, growing market</p>
    <p><strong>Risk:</strong> TensorFlow gap (mitigation: learn in 2 weeks)</p>
  </div>
</div>
```

## Workflow

### Step 1: Skill Extraction

From CV:
- Extract skills using NLP
- Categorize by level (expert/intermediate/beginner)
- Map to standard taxonomy

### Step 2: Job Analysis

For each job:
- Extract requirements
- Categorize (required/preferred/nice-to-have)
- Weight by importance

### Step 3: Score Calculation

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

### Step 4: Market Context

For each match:
- Check salary ranges
- Check demand (number of openings)
- Check growth trend

### Step 5: Generate Evidence Document

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

## Commands

```bash
# Match with evidence
python3 skills/weekly-matcher/match.py --with-evidence

# Generate HTML
python3 skills/html-builder/build.py --input=matches-evidence.json --template=evidence-based

# Upload
python3 skills/s3-uploader/upload.py --file=reports/html/matches.html
```
