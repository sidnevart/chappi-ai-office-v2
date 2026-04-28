---
name: job-scout
description: Use when searching for job opportunities with market analysis and salary verification
---

# Job Scout

## Overview

**Vector DB Integration:**
- Check /mnt/files/research-state/db/knowledge.db before research
- Save findings with embeddings
- Search related facts for context

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

### 0. Load CV Profile
- Load `/mnt/files/research-state/cv_profile.json`
- Extract: skills, experience, location pref, salary target

### 1. Multi-Source Search

Search:
- LinkedIn Jobs
- Indeed
- Glassdoor
- Company career pages
- AngelList (for startups)

### 2. CV Match Filter

For each job found:
1. **Tech Match**: Required skills vs CV skills (40%)
2. **Level Match**: Required level vs CV experience (30%)  
3. **Location Match**: Required vs preferred (15%)
4. **Salary Match**: Offered vs target (15%)

**Skip jobs with score < 50%** (explain why in log)

### 3. Salary Verification

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
