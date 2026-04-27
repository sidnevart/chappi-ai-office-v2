---
name: edu-bootcamp-scout
description: Use when searching for bootcamps and educational programs with verification
---

# Edu Bootcamp Scout (Evidence-Based)

## Overview

Finds bootcamps and produces **HTML evidence document** with:
- Program verification from official sources
- Cost comparison with evidence
- Deadline verification
- Reputation analysis
- Application requirements

## Output Formats

1. **HTML Report** (`/mnt/files/research-state/reports/html/bootcamps-*.html`) — PRIMARY
2. **S3 URL** — public access
3. **Telegram** — notification with link

## Evidence Requirements

Every program MUST have:
- **Official source** (program website)
- **Cost verification** (from official site)
- **Deadline verification** (from official site)
- **Requirements** (from official site)
- **Reputation** (reviews, outcomes)

## HTML Structure

```html
<h1>📚 Bootcamp Programs</h1>

<div class="program">
  <h2>🎓 Program: EEML Summer School</h2>
  
  <div class="verification">
    <h3>✅ Verification</h3>
    <p><strong>Official site:</strong> <a href="...">eml-school.com</a></p>
    <p><strong>Verified:</strong> Cost, dates, requirements match official site</p>
  </div>
  
  <div class="cost">
    <h3>💰 Cost Analysis</h3>
    <p><strong>Tuition:</strong> $2,000 (Source: <a href="...">Official site</a>)</p>
    <p><strong>Travel:</strong> ~$500 (Source: Skyscanner estimate)</p>
    <p><strong>Total:</strong> ~$2,500</p>
  </div>
  
  <div class="outcomes">
    <h3>📈 Outcomes</h3>
    <p><strong>Alumni:</strong> 500+ (Source: <a href="...">LinkedIn</a>)</p>
    <p><strong>Average salary increase:</strong> 30% (Source: <a href="...">Alumni survey</a>)</p>
  </div>
</div>
```

## Workflow

### Step 1: Official Source Check

For each program:
1. Visit official website
2. Verify cost, dates, requirements
3. Check application process
4. Verify accreditation

### Step 2: Outcome Verification

For each program:
1. Check LinkedIn alumni
2. Search for reviews
3. Check job placement rates
4. Verify claims

### Step 3: Generate Evidence Document

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

## Commands

```bash
# Search with verification
python3 skills/edu-bootcamp-scout/search.py --with-verification

# Verify programs
python3 skills/edu-bootcamp-scout/verify.py

# Generate HTML
python3 skills/html-builder/build.py --input=bootcamps-evidence.json --template=evidence-based
```
