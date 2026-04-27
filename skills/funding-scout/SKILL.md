---
name: funding-scout
description: Use when searching for investors with evidence-based matching and track record analysis
---

# Funding Scout (Evidence-Based)

## Overview

Finds investors and produces **HTML evidence document** with:
- Investor track record with data
- Portfolio analysis with sources
- Check size verification
- Contact information with attribution
- Success probability scoring

## Output Formats

1. **HTML Report** (`/mnt/files/research-state/reports/html/funding-*.html`) — PRIMARY
2. **S3 URL** — public access
3. **Telegram** — notification with link

## Evidence Requirements

Every investor MUST have:
- **Track record**: Portfolio companies, exits
- **Check size**: Verified from Crunchbase/PitchBook
- **Sector focus**: From official website
- **Geography**: Where they invest
- **Stage**: Seed/Series A/etc.
- **Warm intro path**: LinkedIn mutual connections

## HTML Structure

```html
<h1>💰 Funding Landscape Analysis</h1>

<div class="investor">
  <h2>🏦 Runa Capital</h2>
  
  <div class="track-record">
    <h3>Track Record</h3>
    <table>
      <tr><th>Company</th><th>Sector</th><th>Exit</th><th>Return</th><th>Source</th></tr>
      <tr><td>Nginx</td><td>DevTools</td><td>$670M</td><td>15x</td><td><a href="...">TechCrunch</a></td></tr>
      <tr><td>PandaDoc</td><td>SaaS</td><td>$1B</td><td>20x</td><td><a href="...">Forbes</a></td></tr>
    </table>
  </div>
  
  <div class="check-size">
    <h3>Check Size Verification</h3>
    <p><strong>Claimed:</strong> $500K-$3M Seed/Series A</p>
    <p><strong>Evidence:</strong></p>
    <ul>
      <li>Nginx: $2M Series A (Source: <a href="...">Crunchbase</a>)</li>
      <li>PandaDoc: $1M Seed (Source: <a href="...">Crunchbase</a>)</li>
    </ul>
    <p><strong>Confidence:</strong> High (verified from multiple sources)</p>
  </div>
  
  <div class="fit">
    <h3>Fit for TeamMemory AI</h3>
    <p><strong>Score:</strong> 9/10</p>
    <p><strong>Why:</strong></p>
    <ul>
      <li>✅ CIS focus (matches our market)</li>
      <li>✅ DevTools/SaaS experience (Nginx, PandaDoc)</li>
      <li>✅ Seed stage active (recent investments)</li>
      <li>✅ $1-3M check size (matches our need)</li>
    </ul>
    <p><strong>Evidence:</strong> Portfolio analysis from Crunchbase (Source: <a href="...">Crunchbase</a>)</p>
  </div>
  
  <div class="warm-intro">
    <h3>Warm Introduction Path</h3>
    <p><strong>Option 1:</strong> Via Nginx founder (mutual connection on LinkedIn)</p>
    <p><strong>Option 2:</strong> Via Сколково (partner program)</p>
    <p><strong>Source:</strong> LinkedIn network analysis</p>
  </div>
</div>
```

## Workflow

### Step 1: Investor Database Search

Search multiple sources:
- Crunchbase (https://crunchbase.com)
- PitchBook (if available)
- Investor websites
- Portfolio company websites
- News articles about investments

### Step 2: Track Record Verification

For each investor:
1. List portfolio companies (from Crunchbase)
2. Check exits (IPO, acquisition)
3. Calculate returns (if public)
4. Verify check sizes
5. Check recent activity

### Step 3: Fit Scoring

Score each investor:
| Criterion | Weight | Evidence |
|-----------|--------|----------|
| Sector fit | 30% | Portfolio analysis |
| Stage fit | 25% | Recent investments |
| Geography | 20% | Investment locations |
| Check size | 15% | Verified amounts |
| Track record | 10% | Exits, returns |

### Step 4: Warm Intro Research

Find paths:
1. LinkedIn mutual connections
2. Portfolio founder intros
3. Accelerator networks
4. Industry events

### Step 5: Generate Evidence Document

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

## Commands

```bash
# Search with evidence
python3 skills/funding-scout/search.py --with-evidence --verify-checks

# Verify track record
python3 skills/funding-scout/verify.py --investor=Runa-Capital

# Generate HTML
python3 skills/html-builder/build.py --input=funding-evidence.json --template=evidence-based
```
