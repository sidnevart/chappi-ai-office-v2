---
name: edu-grant-scout
description: Use when searching for grants and scholarships with verification and deadline tracking
---

# Edu Grant Scout (Evidence-Based)

## Overview

Finds grants and produces **HTML evidence document** with:
- Official verification from grant providers
- Eligibility requirements with proofs
- Deadline verification
- Application process documentation
- Success rate analysis

## Output Formats

1. **HTML Report** (`/mnt/files/research-state/reports/html/grants-*.html`) — PRIMARY
2. **S3 URL** — public access
3. **Telegram** — notification with link

## Evidence Requirements

Every grant MUST have:
- **Official source** (grant website)
- **Amount verification** (from official announcement)
- **Deadline confirmation** (from official site)
- **Eligibility requirements** (from official rules)
- **Application process** (from official guide)
- **Success rate** (if available)

## HTML Structure

```html
<h1>🎓 Grants & Scholarships</h1>

<div class="grant">
  <h2>Grant: Сколково</h2>
  
  <div class="verification">
    <h3>✅ Verification</h3>
    <p><strong>Official site:</strong> <a href="https://sk.ru/...">sk.ru</a></p>
    <p><strong>Verified:</strong> Amount, deadline, requirements</p>
  </div>
  
  <div class="amount">
    <h3>💰 Amount Verification</h3>
    <p><strong>Total:</strong> Up to 25M ₽</p>
    <p><strong>Breakdown:</strong></p>
    <ul>
      <li>R&D: 70% (Source: <a href="...">Official rules</a>)</li>
      <li>Equipment: 20%</li>
      <li>Travel: 10%</li>
    </ul>
  </div>
  
  <div class="eligibility">
    <h3>📋 Eligibility</h3>
    <p><strong>Required:</strong></p>
    <ul>
      <li>Russian legal entity (Source: <a href="...">Law 127-ФЗ</a>)</li>
      <li>Skolkovo resident status</li>
      <li>Project duration: 1-3 years</li>
    </ul>
  </div>
  
  <div class="success-rate">
    <h3>📈 Success Rate</h3>
    <p><strong>2025 data:</strong> 15% acceptance (Source: <a href="...">Skolkovo report</a>)</p>
    <p><strong>Average funding:</strong> 18M ₽</p>
  </div>
</div>
```

## Workflow

### Step 1: Official Source Check

For each grant:
1. Visit official website
2. Verify amount, deadline, requirements
3. Check application process
4. Verify eligibility

### Step 2: Success Rate Analysis

For each grant:
1. Search for previous winners
2. Check acceptance rates
3. Find average funding amounts
4. Check time to decision

### Step 3: Generate Evidence Document

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

## Commands

```bash
# Search with verification
python3 skills/edu-grant-scout/search.py --with-verification

# Verify grants
python3 skills/edu-grant-scout/verify.py

# Generate HTML
python3 skills/html-builder/build.py --input=grants-evidence.json --template=evidence-based
```
