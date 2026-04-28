---
name: edu-competition-scout
description: Use when searching for competitions and hackathons with verification
---

# Edu Competition Scout

## Overview

Finds competitions and produces **HTML evidence report** with:
- Official verification
- Prize verification
- Deadline confirmation
- Requirements check
- Reputation analysis

## Output

1. **HTML Report** (`reports/html/competitions-YYYY-MM-DD.html`) — PRIMARY
2. **S3 Upload** → public URL
3. **Telegram** — notification with link

## Evidence Rules

Every competition MUST have:
- **Official source** (website)
- **Prize verification** (from official rules)
- **Deadline confirmation** (from official site)
- **Requirements** (from official rules)
- **Previous winners** (if available)

## Workflow

### 1. Official Source Check

For each competition:
1. Visit official website
2. Verify prizes, dates, requirements
3. Check rules document
4. Verify organizer legitimacy

### 2. Prize Verification

For each competition:
1. Check prize pool from official rules
2. Verify payment method
3. Check tax implications
4. Verify previous payouts

### 3. Generate HTML Evidence Report

HTML with:
- Competition cards with verification
- Prize details with sources
- Previous edition data
- Application checklist

## Best Practices

- ✅ Verify from official site
- ✅ Verify prizes
- ✅ Check previous editions
- ❌ No competition without official source
- ❌ No prize without verification


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
