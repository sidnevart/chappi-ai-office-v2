---
name: company-analyst-agent
description: Agent that orchestrates company analysis pipeline. MUST trigger all downstream agents.
---

# Company Analyst Agent

## Overview

Orchestrates the complete research pipeline for a company/idea.
Runs 9 agents in sequence, producing all artifacts.
Ensures Telegram notification is ALWAYS sent.

## Vector DB Integration

Before running pipeline:
1. Check `/mnt/files/research-state/db/knowledge.db`
2. Search for existing facts about target company
3. Skip research if data is fresh (TTL not expired)
4. Store new findings after each agent completes

```python
from skills.local-vector-db import VectorDB

db = VectorDB()

# Before pipeline
if db.is_fresh('company', target):
    company_data = db.get_fact('company', target)
else:
    company_data = None

# After each agent
if company_data:
    db.add_fact('company', target, json.dumps(company_data), 
                source_url='https://...', confidence='High', 
                discovered_by='company-analyst-agent')
```

## Trigger

When user requests company analysis OR when DealFlowTracker finds a deal.

## Pipeline (MUST complete all steps)

```
CompanyAnalyst → CompetitiveStrategist → IdeaGenerator → RussianMarketAnalyst
     ↓                ↓                      ↓                ↓
  [company]      [strategy]           [idea]         [russian_market]
     ↓                ↓                      ↓                ↓
     └──────→ FundingScout → FinancialModeler → PitchBuilder → TechSpecWriter
                 ↓                  ↓                ↓              ↓
              [funding]        [financial]      [pitch]        [tech_spec]
                 └────────────────────────────────────────────────┘
                                          ↓
                                   TelegramReporter
                                          ↓
                                    [notification]
```

## Steps

### Step 1: Company Deep Dive
- Run `company-deep-dive` skill
- Output: `/mnt/files/research-state/business/companies/[company].json`

### Step 2: Competitive Strategy
- Run `competitive-analysis` skill with company data
- Output: `/mnt/files/research-state/business/strategies/[company].json`
- **CRITICAL**: Must include strategy document with evidence

### Step 3: Idea Generation
- Run `idea-generator` skill with company + strategy
- Output: `/mnt/files/research-state/business/ideas/[company].json`
- **CRITICAL**: Must include full idea with market evidence

### Step 4: Russian Market Analysis
- Run `russian-market-analysis` skill with idea
- Output: `/mnt/files/research-state/business/russian_market/[company].json`
- **CRITICAL**: Must include regulatory requirements

### Step 5: Funding Search
- Run `funding-scout` skill with idea
- Output: `/mnt/files/research-state/business/funding/[company].json`
- **CRITICAL**: Must include investor list with track record

### Step 6: Financial Model
- Run `financial-modeling` skill with idea
- Output: `/mnt/files/research-state/business/financial_models/[company].json`
- **CRITICAL**: Must include unit economics, projections, sensitivity
- Also generate: Google Sheets with formulas

### Step 7: Pitch Deck
- Run `pitch-builder` skill with all data
- Output: `/mnt/files/research-state/business/pitches/[company].html`
- **CRITICAL**: Must be HTML with metrics, sources, self-challenge

### Step 8: Tech Spec
- Run `tech-spec-writer` skill with idea
- Output: `/mnt/files/research-state/tech-specs/[company].md`
- **CRITICAL**: Must include architecture, security, deployment

### Step 9: Upload to S3
- Upload ALL artifacts to MinIO:
  - company.json → S3
  - strategy.json → S3
  - idea.json → S3
  - russian_market.json → S3
  - funding.json → S3
  - financial.json → S3
  - pitch.html → S3
  - tech_spec.md → S3
  - evidence_report.html → S3

### Step 10: Send Telegram
- **ALWAYS** send notification to Telegram
- Include: links to ALL artifacts
- Format: Markdown with metrics

## Output Checklist

After pipeline completes, verify:
- [ ] Company deep dive (JSON + HTML)
- [ ] Competitive strategy (JSON)
- [ ] Business idea (JSON + HTML)
- [ ] Russian market analysis (JSON + HTML)
- [ ] Funding prospects (JSON)
- [ ] Financial model (JSON + Google Sheets)
- [ ] Pitch deck (HTML)
- [ ] Tech spec (Markdown)
- [ ] Evidence report (HTML)
- [ ] All uploaded to S3
- [ ] Telegram notification sent

## Error Handling

If ANY step fails:
1. Log error to `/mnt/files/research-state/logs/agent-errors.json`
2. Continue with remaining steps
3. Include partial results in Telegram
4. Do NOT skip Telegram notification


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
