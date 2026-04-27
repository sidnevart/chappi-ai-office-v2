---
name: idea-generator
description: Use when generating business ideas from trends, competitive weaknesses, or market gaps, especially for startup ideation or innovation research
---

# Idea Generator

## Overview

Generates business ideas by analyzing market trends and competitive weaknesses. Scores ideas by market size, feasibility, and differentiation.

## When to Use

- User asks for "business ideas" or "startup ideas"
- Pipeline trigger: trends + weaknesses → ideas
- Innovation workshops

**When NOT to use:**
- Market analysis → use trend-monitor
- Competitive strategy → use competitive-analysis
- Financial modeling → use financial-modeling

## Core Pattern

**Input:** Trends + Company weaknesses
**Process:** Analyze gaps → Generate ideas → Score → Rank
**Output:** JSON with scored ideas

## Workflow

### 1. Analyze Gaps

Read from state:
```
/mnt/files/research-state/business/trends.json
/mnt/files/research-state/business/companies/*.json
```

### 2. Generate Ideas

For each trend + weakness pair:
- What product solves this?
- Who pays for it?
- What's the unique angle?

### 3. Score

```json
{
  "name": "...",
  "description": "...",
  "score": 0.0,
  "market_size": "...",
  "feasibility": "high|medium|low",
  "differentiation": "...",
  "status": "new|analyzed"
}
```

### 4. Report

Save to:
```
/mnt/files/research-state/business/ideas.json
```

## Scoring Criteria

| Factor | Weight | How to Measure |
|--------|--------|----------------|
| Market size | 30% | $B, growth rate |
| Feasibility | 25% | Technical complexity |
| Differentiation | 25% | Unique angle |
| Timing | 20% | Trend alignment |

## Quick Reference

| Action | Method |
|--------|--------|
| Read trends | Read JSON from research-state |
| Score idea | Market + feasibility + differentiation |
| Save | Write to ideas.json |

## Common Mistakes

- **Copycat ideas:** Require differentiation
- **Ignoring timing:** Check trend maturity
- **Vague descriptions:** Must be specific enough to build MVP
- **Not saving sources:** Link to trend/weakness that triggered idea
