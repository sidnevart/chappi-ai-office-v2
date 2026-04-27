---
name: deal-flow-tracker
description: Use when tracking startup funding, acquisitions, or investment deals in the technology sector, or when building a deal pipeline for analysis
---

# Deal Flow Tracker

## Overview

Tracks and records startup funding rounds, acquisitions, and major investment deals. Produces structured deal flow reports with company details, amounts, and investors.

## When to Use

- User asks about "recent investments", "who raised funding"
- Weekly deal monitoring (scheduled agent)
- Building pipeline for company analysis or competitive research

**When NOT to use:**
- Specific company financials → use company-deep-dive
- Market trends → use trend-monitor
- Investment thesis → use funding-scout

## Core Pattern

**Input:** None (web search) or specific sector
**Process:** Search → Verify → Structure → Report
**Output:** JSON with deals, amounts, investors

## Workflow

### 1. Search

```
Query: "startup funding 2026" OR "Series A AI" OR "acquisition tech"
Sources: Crunchbase, PitchBook, TechCrunch
Time range: last 7-14 days
```

### 2. Verify

Cross-reference 2+ sources for each deal:
- Company name
- Round type (Seed, Series A, etc.)
- Amount
- Lead investor

### 3. Structure

```json
{
  "company": "...",
  "round": "Series A",
  "amount": "$10M",
  "valuation": "$50M",
  "lead_investor": "...",
  "co_investors": [...],
  "sector": "AI",
  "date": "2026-04-28",
  "source_url": "...",
  "verified": true
}
```

### 4. Report

Save to state:
```
/mnt/files/research-state/business/deals.json
```

## Output Format

```json
{
  "scan_date": "2026-04-28",
  "source": "DealFlowTracker",
  "deals": [...],
  "new_count": 0,
  "total_count": 0,
  "total_value": "$0M"
}
```

## Quick Reference

| Action | Method |
|--------|--------|
| Search deals | web_search "Series A AI 2026" |
| Verify amount | Cross-check 2+ sources |
| Categorize | By sector, round type, geography |

## Common Mistakes

- **Reporting unverified deals:** Always 2+ sources
- **Wrong amounts:** Be precise ("$5-10M" if unclear)
- **Missing lead investor:** Always identify lead
- **Not tracking pre-money:** Record valuation if available
