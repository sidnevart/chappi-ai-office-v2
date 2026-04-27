---
name: russian-market-analysis
description: Use when analyzing Russian/CIS market entry with regulatory evidence and compliance proofs
---

# Russian Market Analysis

## Overview

Analyzes Russian market and produces **HTML evidence report** with:
- Regulatory requirements with official sources
- Competitor analysis with local data
- Compliance checklists with citations
- Market size calculations with methodology
- Risk assessment with mitigation

## Output

1. **HTML Report** (`reports/html/russian-market-[idea].html`) — PRIMARY
2. **S3 Upload** → public URL
3. **Telegram** → link to HTML

No JSON for humans.

## Evidence Rules

Every regulation claim MUST have:
- **Official source** (law text, government site)
- **Article/paragraph number**
- **Enforcement date**
- **Penalty for non-compliance**
- **Compliance cost estimate**

## Workflow

### 1. Regulatory Research

Check official sources:
1. **Consultant.ru** — all Russian laws
2. **RKN.gov.ru** — data protection regulator
3. **Government decrees** — official requirements
4. **Tax code** — relevant articles

### 2. Market Size Calculation

Bottom-up calculation:
```
Total workers in Russia: 72M (Source: Rosstat)
Knowledge workers: 15M (Source: Habr survey)
Teams of 5-50: 500K (Source: calculation)
Target penetration (Year 1): 0.5% = 2,500 teams
ARPU: $8/month = $96/year
Revenue: 2,500 × $96 = $240K (Year 1)
```

### 3. Self-Challenge

- "Is 152-ФЗ really enforced?" → Check RKN fines list
- "Do teams really need this?" → Survey data
- "Can we comply affordably?" → Yandex Cloud pricing

### 4. Generate HTML Evidence Report

```html
<h1>🇷🇺 Russian Market Analysis</h1>

<div class="regulations">
  <h2>⚖️ Regulatory Requirements</h2>
  
  <div class="regulation">
    <h3>152-ФЗ: Personal Data Protection</h3>
    <p><strong>Source:</strong> <a href="http://www.consultant.ru/document/cons_doc_LAW_61801/">Federal Law 152-ФЗ</a> (Russian)</p>
    <p><strong>Article 18:</strong> Personal data of Russian citizens must be stored in Russia</p>
    <p><strong>Penalty:</strong> Up to 500K ₽ for first violation, up to 3M ₽ for repeat</p>
    <p><strong>Evidence:</strong> RKN enforcement cases (Source: <a href="https://rkn.gov.ru/...">RKN</a>)</p>
    <p><strong>Compliance cost:</strong> $5-10K/year (self-hosted) or $2-5K/year (Yandex Cloud)</p>
    <p><strong>Method:</strong> Cost estimate from Yandex Cloud pricing (Source: <a href="https://cloud.yandex.com/pricing">Yandex</a>)</p>
  </div>
  
  <div class="regulation">
    <h3>Localization Requirements</h3>
    <p><strong>Source:</strong> <a href="...">Government Decree No. 1236</a></p>
    <p><strong>Requirements:</strong></p>
    <ul>
      <li>Russian language interface</li>
      <li>Russian payment methods (SBP, Mir)</li>
      <li>Local customer support</li>
    </ul>
  </div>
</div>

<div class="market-size">
  <h2>📊 Market Size Calculation</h2>
  <pre>
TAM = 50M Russian workers × $10/month = $6B/year
Method: Based on Russia's working population (Source: Rosstat https://rosstat.gov.ru/...)

SAM = 5M knowledge workers × $10/month = $600M/year
Method: Filtered to office workers (Source: <a href="...">Habr survey</a>)

SOM = 500K teams × $8/month = $48M/year (Year 1)
Method: Conservative 0.5% penetration
Confidence: Medium (based on comparable SaaS adoption)
  </pre>
</div>

<div class="competitors">
  <h2>🏢 Local Competitors</h2>
  <table>
    <tr><th>Company</th><th>Product</th><th>Strengths</th><th>Weaknesses</th><th>Source</th></tr>
    <tr><td>Яндекс Трекер</td><td>Task management</td><td>Yandex ecosystem</td><td>No AI features</td><td><a href="...">Yandex</a></td></tr>
  </table>
</div>

<div class="self-challenge">
  <h2>🤔 Self-Challenge</h2>
  <p><strong>Q:</strong> Is Russian market big enough?</p>
  <p><strong>A:</strong> $48M SOM is comparable to early-stage SaaS markets. Zoom entered with $50M TAM.</p>
  <p><strong>Evidence:</strong> Zoom IPO prospectus showed $43M initial market (Source: <a href="...">SEC filing</a>)</p>
</div>

<div class="sources">
  <h2>📚 Sources</h2>
  <ol>
    <li><a href="...">[Title]</a> — [What it proves]</li>
  </ol>
</div>
```

## Best Practices

- ✅ Official law sources only
- ✅ Calculation methods shown
- ✅ RKN enforcement checked
- ✅ Local pricing verified
- ❌ No hearsay about regulations
- ❌ No market size without calculation
- ❌ No competitors without verification
