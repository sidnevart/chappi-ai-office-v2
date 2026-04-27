---
name: research-digest
description: Generate research digests for AI Office. Use when: (1) Running daily cron jobs for business/edu/career research, (2) Creating HTML/Telegram digests with web search data, (3) Updating knowledge base with new findings, (4) Matching CV with opportunities, (5) Tracking trends and deals. Automatically stores data in MEM0 memory for semantic search.
---

# Research Digest Skill

## Workflow

1. **Run web search** via OpenClaw tools for current data
2. **Parse and analyze** results using deep_research skill
3. **Generate digest** in HTML + Telegram formats
4. **Store in memory** via MEM0 for semantic search
5. **Send to Telegram** if channel configured

## Categories

- **business**: deals, trends, funding, companies
- **edu**: bootcamps, competitions, grants, programs
- **career**: jobs, internships, CV matching

## Usage

```
@research-digest run category=business agent=DealFlowTracker
```

## Memory Integration

All data auto-stores in MEM0 with:
- agent_id: "ai-office-research"
- categories: ["business", "deals", "funding"]
- metadata: {date, source, type}

## Output Formats

- HTML: /home/user/research-system/output/digest_*.html
- Telegram: /home/user/research-system/output/telegram_*.txt
