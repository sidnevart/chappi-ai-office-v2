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
