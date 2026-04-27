---
name: tech-spec-writer
description: Use when writing technical specifications with architecture decisions and security analysis
---

# Tech Spec Writer

## Overview

Writes technical specifications as **Markdown** (primary) with:
- Architecture decisions with justification
- Technology choices with comparison
- Security analysis with threats
- Performance benchmarks
- Deployment instructions

## Output

1. **Markdown** (`tech-specs/[idea].md`) — PRIMARY
2. **HTML** (optional) — for web viewing
3. **S3 Upload** → public URL
4. **Telegram** — notification with link

## Evidence Rules

Every decision MUST have:
- **Options considered**: At least 2 alternatives
- **Why chosen**: Specific reasons
- **Trade-offs**: Pros and cons
- **Performance data**: Benchmarks if applicable
- **Security analysis**: Threat model

## Workflow

### 1. Research Options

For each technology choice:
1. List 2+ alternatives
2. Find benchmarks
3. Check pricing
4. Review security

### 2. Decision Justification

For each decision:
- Why this option?
- Why not alternatives?
- What's the trade-off?
- What if we're wrong?

### 3. Security Analysis

```
Threat: Data breach
Likelihood: Medium (based on industry stats)
Impact: High (GDPR fines up to 4% revenue)
Mitigation: AES-256 + TLS 1.3
Source: GDPR Article 83
```

### 4. Generate Spec

Markdown with:
- Decision records
- Technology comparison tables
- Security threat model
- Performance benchmarks
- Deployment guide

## Best Practices

- ✅ Every decision justified
- ✅ 2+ alternatives considered
- ✅ Security threat model
- ✅ Performance benchmarks
- ❌ No decisions without justification
- ❌ No "best practice" without source
- ❌ No security without threat model
