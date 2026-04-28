---
name: funding-scout
description: Use when searching for investors with evidence-based matching and track record analysis
---

# Funding Scout

## Overview

Finds investors and produces **HTML evidence report** with:
- Investor track record with data
- Portfolio analysis with sources
- Check size verification
- Contact information with attribution
- Success probability scoring

## Output

1. **HTML Report** (`reports/html/funding-[idea].html`) — PRIMARY
2. **S3 Upload** → public URL
3. **Telegram** → link to HTML

## Evidence Rules

Every investor MUST have:
- **Track record**: Portfolio companies, exits
- **Check size**: Verified from Crunchbase/PitchBook
- **Sector focus**: From official website
- **Geography**: Where they invest
- **Stage**: Seed/Series A/etc.
- **Warm intro path**: LinkedIn mutual connections

## Workflow

### 1. Investor Database Search

Search:
- Crunchbase (https://crunchbase.com)
- PitchBook (if available)
- Investor websites
- Portfolio company websites
- News articles about investments

### 2. Track Record Verification

For each investor:
1. List portfolio companies (from Crunchbase)
2. Check exits (IPO, acquisition)
3. Calculate returns (if public)
4. Verify check sizes
5. Check recent activity

### 3. Fit Scoring

Score each investor:
| Criterion | Weight | Evidence |
|-----------|--------|----------|
| Sector fit | 30% | Portfolio analysis |
| Stage fit | 25% | Recent investments |
| Geography | 20% | Investment locations |
| Check size | 15% | Verified amounts |
| Track record | 10% | Exits, returns |

### 4. Warm Intro Research

Find paths:
1. LinkedIn mutual connections
2. Portfolio founder intros
3. Accelerator networks
4. Industry events

### 5. Generate HTML Evidence Report

HTML with:
- Investor cards with track record
- Check size verification
- Fit scoring with evidence
- Warm intro paths
- Recommended approach

## Best Practices

- ✅ Verify every check size
- ✅ Verify every exit
- ✅ Find warm intro path
- ✅ Score with evidence
- ❌ No investor without track record
- ❌ No claimed check size without proof
- ❌ No recommendation without fit score


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
