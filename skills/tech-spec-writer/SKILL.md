---
name: tech-spec-writer
description: Use when writing technical specifications with architecture decisions and security analysis
---

# Tech Spec Writer (Evidence-Based)

## Overview

Writes technical specifications as **Markdown** (primary) with:
- Architecture decisions with justification
- Technology choices with comparison
- Security analysis with threats
- Performance benchmarks
- Deployment instructions

## Output Formats

1. **Markdown** (`/mnt/files/research-state/tech-specs/*.md`) — PRIMARY
2. **HTML** (optional) — for web viewing
3. **S3 URL** — public access
4. **Telegram** — notification with link

## Evidence Requirements

Every decision MUST have:
- **Options considered**: At least 2 alternatives
- **Why chosen**: Specific reasons
- **Trade-offs**: Pros and cons
- **Performance data**: Benchmarks if applicable
- **Security analysis**: Threat model

## Markdown Structure

```markdown
# Technical Specification: TeamMemory AI

## 1. Architecture Decision: Vector Database

### Options Considered
| Option | Pros | Cons | Source |
|--------|------|------|--------|
| Qdrant | Rust-based, fast | Newer ecosystem | Benchmark: https://... |
| Pinecone | Managed, easy | Expensive | Pricing: https://... |
| Weaviate | GraphQL | Complex | Docs: https://... |

### Decision: Qdrant
**Why:** Best performance/price ratio for self-hosted
**Evidence:** Benchmark shows 2x faster than Weaviate (Source: https://...)
**Trade-off:** Need to manage infrastructure

### Self-Challenge
**Q:** Why not Pinecone for simplicity?
**A:** Cost analysis shows $500/month vs $50/month self-hosted (Source: pricing pages)

## 2. Security: Data Encryption

### Threat Model
| Threat | Likelihood | Impact | Mitigation | Source |
|--------|------------|--------|------------|--------|
| Data breach | Medium | High | AES-256 | NIST guidelines |
| Insider threat | Low | High | RBAC | OWASP |

### Implementation
```python
# Encryption at rest
from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher = Fernet(key)
```

## 3. Performance Targets

| Metric | Target | Evidence | Source |
|--------|--------|----------|--------|
| Search latency | <200ms | Benchmark | Internal test |
| Ingestion | 1000 msg/sec | Load test | k6 results |

## 4. Sources
1. [Qdrant Benchmark](https://...)
2. [NIST Encryption Guidelines](https://...)
3. [OWASP Security](https://...)
```

## Workflow

### Step 1: Research Options

For each technology choice:
1. List 2+ alternatives
2. Find benchmarks
3. Check pricing
4. Review security

### Step 2: Decision Justification

For each decision:
- Why this option?
- Why not alternatives?
- What's the trade-off?
- What if we're wrong?

### Step 3: Security Analysis

```
Threat: Data breach
Likelihood: Medium (based on industry stats)
Impact: High (GDPR fines up to 4% revenue)
Mitigation: AES-256 + TLS 1.3
Source: GDPR Article 83
```

### Step 4: Generate Spec

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

## Commands

```bash
# Write spec with evidence
python3 skills/tech-spec-writer/write.py --idea=team-memory-ai --with-evidence

# Generate HTML
python3 skills/html-builder/build.py --input=tech-specs/team-memory-ai.md --output=tech-spec.html

# Upload
python3 skills/s3-uploader/upload.py --file=tech-specs/team-memory-ai.md
```
