---
name: tech-spec-writer-agent
description: Agent that writes technical specs. MUST output Markdown spec.
---

# Tech Spec Writer Agent

## Input
- Business idea
- Strategy document
- Pitch deck

## Output (ALWAYS)
1. **Tech Spec MD** → `/mnt/files/research-state/tech-specs/[idea].md`
2. **Upload to S3** → public URL
3. **Trigger next agent** → TelegramReporter

## Spec MUST include:
- Architecture diagram
- Technology choices with justification
- Security analysis
- Performance requirements
- Deployment instructions
