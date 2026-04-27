---
name: job-scout
description: Use when searching for job opportunities with market analysis and salary verification
---

# Job Scout (Evidence-Based)

## Overview

Finds jobs and produces **HTML evidence document** with:
- Salary verification from multiple sources
- Market demand analysis
- Skill requirements with evidence
- Company research
- Application recommendations

## Output Formats

1. **HTML Report** (`/mnt/files/research-state/reports/html/jobs-*.html`) — PRIMARY
2. **S3 URL** — public access
3. **Telegram** — notification with link

## Evidence Requirements

Every job MUST have:
- **Salary range** from 2+ sources (LinkedIn, Glassdoor, job posting)
- **Company verification** (exists, legitimate)
- **Requirements** from official posting
- **Market demand** (number of similar openings)

## HTML Structure

```html
<h1>💼 Job Market Analysis</h1>

<div class="market-overview">
  <h2>📊 Market Overview</h2>
  <p><strong>Role:</strong> AI Developer</p>
  <p><strong>Location:</strong> London</p>
  <p><strong>Openings found:</strong> 1,133</p>
  <p><strong>Source:</strong> LinkedIn, Indeed, Glassdoor</p>
</div>

<div class="job">
  <h2>🏢 Job: Senior AI Engineer at Company</h2>
  
  <div class="salary-verification">
    <h3>💰 Salary Verification</h3>
    <p><strong>Posted:</strong> $120K-$150K</p>
    <p><strong>Verified:</strong></p>
    <ul>
      <li>Glassdoor: $130K avg (Source: <a href="...">Link</a>)</li>
      <li>Levels.fyi: $140K median (Source: <a href="...">Link</a>)</li>
      <li>LinkedIn: $125K-$155K range (Source: <a href="...">Link</a>)</li>
    </ul>
    <p><strong>Confidence:</strong> High (3 sources agree)</p>
  </div>
  
  <div class="company-research">
    <h3>🏢 Company Research</h3>
    <p><strong>Founded:</strong> 2019 (Source: <a href="...">Crunchbase</a>)</p>
    <p><strong>Funding:</strong> $50M Series B (Source: <a href="...">TechCrunch</a>)</p>
    <p><strong>Glassdoor rating:</strong> 4.2/5 (Source: <a href="...">Glassdoor</a>)</p>
    <p><strong>Employee count:</strong> 200+ (Source: <a href="...">LinkedIn</a>)</p>
  </div>
  
  <div class="requirements">
    <h3>📋 Requirements Analysis</h3>
    <p><strong>Required:</strong> Python, PyTorch, 5+ years</p>
    <p><strong>Match with CV:</strong> 85%</p>
    <p><strong>Evidence:</strong> CV analysis shows...</p>
  </div>
</div>
```

## Workflow

### Step 1: Multi-Source Search

Search:
- LinkedIn Jobs
- Indeed
- Glassdoor
- Company career pages
- AngelList (for startups)

### Step 2: Salary Verification

For each job:
1. Check posted range
2. Verify on Glassdoor
3. Check Levels.fyi (for tech)
4. Compare with market data

### Step 3: Company Research

For each company:
1. Check Crunchbase (funding, founded)
2. Check Glassdoor (rating, reviews)
3. Check LinkedIn (size, growth)
4. Check news (recent developments)

### Step 4: Generate Evidence Document

HTML with:
- Market overview
- Job cards with salary verification
- Company research
- Requirements analysis
- Application recommendations

## Best Practices

- ✅ Verify salaries from 2+ sources
- ✅ Research every company
- ✅ Match requirements to CV
- ❌ No job without salary verification
- ❌ No company without research

## Commands

```bash
# Search with evidence
python3 skills/job-scout/search.py --role="AI Developer" --with-evification

# Verify salaries
python3 skills/job-scout/verify-salaries.py

# Generate HTML
python3 skills/html-builder/build.py --input=jobs-evidence.json --template=evidence-based
```
