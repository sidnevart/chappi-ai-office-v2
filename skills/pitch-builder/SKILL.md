---
name: pitch-builder
description: Use when creating investor pitch decks with evidence-based claims and proofs
---

# Pitch Builder

## Overview

**Vector DB Integration:**
- Check /mnt/files/research-state/db/knowledge.db before research
- Save findings with embeddings
- Search related facts for context

Generates investor pitch decks as **HTML** (primary) with:
- Every claim backed by evidence
- Source citations in speaker notes
- Market data with calculations
- Competitive analysis with proof
- Risk mitigation with data

## Output

1. **HTML** (`business/pitches/[idea].html`) — PRIMARY
2. **PDF** — converted from HTML for printing
3. **S3 Upload** → public URL
4. **Telegram** — notification with link

## Evidence Rules

Every slide MUST have:
- **Speaker notes** with evidence URLs
- **Data sources** for every number
- **Calculation methods** shown
- **Counter-arguments** addressed

## Workflow

### 1. Evidence Collection

For each pitch claim:
1. Find source
2. Verify number
3. Check date
4. Document method

### 2. Self-Challenge

For each slide:
- "What would investor ask?"
- "What's the counter-argument?"
- "What if this number is wrong?"
- "Why us and not them?"

### 3. Generate Pitch

HTML with:
- Professional styling
- Evidence in speaker notes
- Source citations
- Counter-arguments addressed

### 4. Convert to PDF

Use ReportLab with DejaVu fonts for Cyrillic.

## Best Practices

- ✅ Every number has source
- ✅ Speaker notes with evidence
- ✅ Counter-arguments addressed
- ✅ Professional design
- ❌ No unsupported claims
- ❌ No "we believe" statements
- ❌ No numbers without calculation


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
