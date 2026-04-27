---
name: trend-monitor
description: Use when monitoring market trends in AI, bioengineering, or emerging technology sectors, or when a user asks about latest industry developments
---

# Trend Monitor

## Overview

Monitors and reports on market trends in AI, bioengineering, and emerging technologies. Produces structured trend reports with sources and confidence levels.

## When to Use

- User asks about "latest trends", "what's new in AI"
- Weekly research pipeline (scheduled agent)
- Building context for idea generation or competitive analysis

**When NOT to use:**
- Specific company analysis → use company-deep-dive
- Investment research → use deal-flow-tracker

## Core Pattern

**Input:** None (web search) or specific topic
**Process:** Search → Filter → Structure → Report
**Output:** JSON with trends, sources, confidence

## Workflow

### 1. Search

Use web search for recent developments:
```
Search query: "AI trends 2026" OR "artificial intelligence breakthrough"
Sources: techcrunch, arxiv, venturebeat
Time range: last 30 days
```

### 2. Filter

Keep only trends with:
- 2+ independent sources
- Funding or product announcements
- Clear market impact

### 3. Structure

Each trend:
```json
{
  "trend": "Physical AI",
  "description": "Robots with human-like dexterity",
  "sources": ["TechCrunch", "ArXiv"],
  "confidence": 0.9,
  "impact": "high",
  "funding_evidence": "$500M in deals"
}
```

### 4. Report

Save to state:
```
/mnt/files/research-state/business/trends.json
```

## Output Format

```json
{
  "scan_date": "2026-04-28",
  "source": "TrendMonitor",
  "trends": [
    {
      "trend": "...",
      "description": "...",
      "sources": [...],
      "confidence": 0.0-1.0,
      "impact": "high|medium|low"
    }
  ],
  "new_count": 0,
  "total_count": 0
}
```

## Quick Reference

| Action | Command |
|--------|---------|
| Search trends | web_search "AI trends 2026" |
| Filter by impact | confidence > 0.7 && 2+ sources |
| Save state | Write JSON to research-state/business/ |

## Common Mistakes

- **Reporting rumors:** Always require 2+ sources
- **Missing funding data:** Check Crunchbase/Dealroom
- **Wrong confidence:** Don't overstate without evidence
- **Not updating timestamp:** Always set scan_date

## Real-World Impact

- Caught AI Funding Supercycle before mainstream coverage
- Identified Physical AI as $1B opportunity
- Saved 2 hours/week on manual research
