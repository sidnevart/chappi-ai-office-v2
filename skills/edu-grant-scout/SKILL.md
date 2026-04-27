---
name: edu-grant-scout
description: Use when searching for grants and scholarships with verification and deadline tracking
---

# Edu Grant Scout

## Overview

Finds grants and produces **HTML evidence report** with:
- Official verification from grant providers
- Eligibility requirements with proofs
- Deadline verification
- Application process documentation
- Success rate analysis

## Output

1. **HTML Report** (`reports/html/grants-YYYY-MM-DD.html`) — PRIMARY
2. **S3 Upload** → public URL
3. **Telegram** — notification with link

## Evidence Rules

Every grant MUST have:
- **Official source** (grant website)
- **Amount verification** (from official announcement)
- **Deadline confirmation** (from official site)
- **Eligibility requirements** (from official rules)
- **Application process** (from official guide)
- **Success rate** (if available)

## Workflow

### 1. Official Source Check

For each grant:
1. Visit official website
2. Verify amount, deadline, requirements
3. Check application process
4. Verify eligibility

### 2. Success Rate Analysis

For each grant:
1. Search for previous winners
2. Check acceptance rates
3. Find average funding amounts
4. Check time to decision

### 3. Generate HTML Evidence Report

HTML with:
- Grant cards with verification
- Amount breakdown
- Eligibility requirements
- Success rate data
- Application checklist

## Best Practices

- ✅ Verify from official site
- ✅ Check success rates
- ✅ Verify eligibility
- ❌ No grant without official source
- ❌ No amount without verification
