---
name: pitch-builder-agent
description: Agent that creates pitch decks. MUST output HTML pitch.
---

# Pitch Builder Agent

## Input
- Business idea
- Financial model
- Market analysis
- Strategy document

## Output (ALWAYS)
1. **Pitch HTML** → `/mnt/files/research-state/business/pitches/[idea].html`
2. **Upload to S3** → public URL
3. **Trigger next agent** → TechSpecWriter

## Pitch MUST include:
- Problem with evidence
- Solution description
- Market size with sources
- Competition with feature matrix
- Unit economics
- Team background
- Ask amount
- Evidence in speaker notes


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
