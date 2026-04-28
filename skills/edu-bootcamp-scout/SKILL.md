---
name: edu-bootcamp-scout
description: Use when searching for bootcamps and educational programs with verification
---

# Edu Bootcamp Scout

## Overview

**Vector DB Integration:**
- Check /mnt/files/research-state/db/knowledge.db before research
- Save findings with embeddings
- Search related facts for context

Finds bootcamps and produces **HTML evidence report** with:
- Program verification from official sources
- Cost comparison with evidence
- Deadline verification
- Reputation analysis
- Application requirements

## Output

1. **HTML Report** (`reports/html/bootcamps-YYYY-MM-DD.html`) — PRIMARY
2. **S3 Upload** → public URL
3. **Telegram** — notification with link

## Evidence Rules

Every program MUST have:
- **Official source** (program website)
- **Cost verification** (from official site)
- **Deadline verification** (from official site)
- **Requirements** (from official site)
- **Reputation** (reviews, outcomes)

## Workflow

### 0. Load CV Profile
- Load `/mnt/files/research-state/cv_profile.json`
- Check: education level, skills, experience

### 1. Official Source Check

For each program:
1. Visit official website
2. Verify cost, dates, requirements
3. Check application process
4. Verify accreditation

### 2. Outcome Verification

For each program:
1. Check LinkedIn alumni
2. Search for reviews
3. Check job placement rates
4. Verify claims

### 3. Generate HTML Evidence Report

HTML with:
- Program cards with verification
- Cost breakdown
- Outcome data with sources
- Application checklist

## Best Practices

- ✅ Verify from official site
- ✅ Check outcomes with alumni
- ✅ Verify costs
- ❌ No program without official source
- ❌ No cost without verification


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
