---
name: job-scout
description: Use when searching for job opportunities with market analysis and salary verification
---

# Job Scout

## Overview

Finds jobs and produces **HTML evidence report** with:
- Salary verification from multiple sources
- Market demand analysis
- Skill requirements with evidence
- Company research
- Application recommendations

## Output

1. **HTML Report** (`reports/html/jobs-YYYY-MM-DD.html`) — PRIMARY
2. **S3 Upload** → public URL
3. **Telegram** — notification with link

## Evidence Rules

Every job MUST have:
- **Salary range** from 2+ sources (LinkedIn, Glassdoor, job posting)
- **Company verification** (exists, legitimate)
- **Requirements** from official posting
- **Market demand** (number of similar openings)

## Workflow

### 1. Multi-Source Search

Search:
- LinkedIn Jobs
- Indeed
- Glassdoor
- Company career pages
- AngelList (for startups)

### 2. Salary Verification

For each job:
1. Check posted range
2. Verify on Glassdoor
3. Check Levels.fyi (for tech)
4. Compare with market data

### 3. Company Research

For each company:
1. Check Crunchbase (funding, founded)
2. Check Glassdoor (rating, reviews)
3. Check LinkedIn (size, growth)
4. Check news (recent developments)

### 4. Generate HTML Evidence Report

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
