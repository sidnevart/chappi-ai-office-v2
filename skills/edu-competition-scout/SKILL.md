---
name: edu-competition-scout
description: Use when searching for competitions and hackathons with verification
---

# Edu Competition Scout (Evidence-Based)

## Overview

Finds competitions and produces **HTML evidence document** with:
- Official verification
- Prize verification
- Deadline confirmation
- Requirements check
- Reputation analysis

## Output Formats

1. **HTML Report** (`/mnt/files/research-state/reports/html/competitions-*.html`) — PRIMARY
2. **S3 URL** — public access
3. **Telegram** — notification with link

## Evidence Requirements

Every competition MUST have:
- **Official source** (website)
- **Prize verification** (from official rules)
- **Deadline confirmation** (from official site)
- **Requirements** (from official rules)
- **Previous winners** (if available)

## HTML Structure

```html
<h1>🏆 Competitions & Hackathons</h1>

<div class="competition">
  <h2>Yandex Cup 2026</h2>
  
  <div class="verification">
    <h3>✅ Verification</h3>
    <p><strong>Official site:</strong> <a href="https://yandex.ru/cup/...">yandex.ru/cup</a></p>
    <p><strong>Verified:</strong> Prize pool, dates, requirements</p>
  </div>
  
  <div class="prizes">
    <h3>💰 Prize Verification</h3>
    <p><strong>Total pool:</strong> $10,000</p>
    <p><strong>1st place:</strong> $5,000 (Source: <a href="...">Official rules</a>)</p>
    <p><strong>2nd place:</strong> $3,000</p>
    <p><strong>3rd place:</strong> $2,000</p>
  </div>
  
  <div class="previous">
    <h3>📈 Previous Editions</h3>
    <p><strong>2025:</strong> 1000+ participants (Source: <a href="...">Yandex blog</a>)</p>
    <p><strong>Winners:</strong> 5 hired by Yandex</p>
  </div>
</div>
```

## Workflow

### Step 1: Official Source Check

For each competition:
1. Visit official website
2. Verify prizes, dates, requirements
3. Check rules document
4. Verify organizer legitimacy

### Step 2: Prize Verification

For each competition:
1. Check prize pool from official rules
2. Verify payment method
3. Check tax implications
4. Verify previous payouts

### Step 3: Generate Evidence Document

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

## Commands

```bash
# Search with verification
python3 skills/edu-competition-scout/search.py --with-verification

# Verify competitions
python3 skills/edu-competition-scout/verify.py

# Generate HTML
python3 skills/html-builder/build.py --input=competitions-evidence.json --template=evidence-based
```
