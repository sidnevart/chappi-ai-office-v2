---
name: competitive-analysis
description: Use when building competitive strategy, analyzing differentiation, or creating go-to-market positioning against existing market players
---

# Competitive Analysis

## Overview

Produces competitive strategies: differentiation, pricing, partnerships. Analyzes how to win against specific competitors.

## When to Use

- Company analysis completed (input)
- User asks "how to compete with X"
- Go-to-market planning

**When NOT to use:**
- Market size → use trend-monitor
- Product ideas → use idea-generator
- Pricing alone → use financial-modeling

## Core Pattern

**Input:** Company analysis JSON
**Process:** Identify gaps → Generate strategies → Score → Select best
**Output:** JSON with strategies, recommendations

## Workflow

### 1. Read Company Analysis

```
/mnt/files/research-state/business/companies/{company}.json
```

### 2. Identify Gaps

For each weakness found:
- Is it addressable?
- What's the cost?
- What's the impact?

### 3. Generate Strategies

```json
{
  "name": "...",
  "description": "...",
  "type": "differentiation|pricing|partnership|vertical",
  "target_competitor": "...",
  "investment_required": "$...",
  "timeline": "...",
  "expected_impact": "..."
}
```

### 4. Report

```
/mnt/files/research-state/business/strategies/{company}.json
```

## Strategy Types

| Type | When to Use | Example |
|------|-------------|---------|
| Differentiation | Unique feature | Better UX, new capability |
| Pricing | Cost advantage | Freemium, lower CAC |
| Partnership | Ecosystem play | Integrations, channels |
| Vertical | Niche focus | Industry-specific |

## Quick Reference

| Step | Method |
|------|--------|
| Read analysis | Read company JSON |
| Find gaps | Weaknesses → opportunities |
| Score strategy | Investment vs impact |

## Common Mistakes

- **Generic strategies:** Must be specific to competitor
- **Ignoring resources:** Match strategy to available capital
- **No timeline:** Always specify execution timeline
- **Not measurable:** Define success metrics
