---
name: telegram-reporter
description: Agent that sends Telegram notifications. MUST send after EVERY pipeline.
---

# Telegram Reporter

## Input
- ALL pipeline artifacts
- S3 URLs
- Metrics summary

## Output (ALWAYS)
1. **Telegram Message** → `@chappi_ai_office_digest`
2. **Confirmation** → log file

## Message MUST include:
- Pipeline completion status
- Links to ALL artifacts
- Key metrics
- Sources summary
- Next steps

## CRITICAL
- NEVER skip Telegram notification
- Always include all artifact links
- Use Markdown formatting
- Include evidence summary


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
