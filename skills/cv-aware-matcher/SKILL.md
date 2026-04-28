---
name: cv-aware-matcher
description: Use when matching CV profile with opportunities and calculating detailed match scores
---

# CV-Aware Matcher

## Overview

Matches CV profile with opportunities and calculates detailed match score.

## Input
- CV profile JSON
- Opportunity (job/bootcamp/competition/grant)

## Output
- Match score 0-100%
- Detailed breakdown by categories
- Gap analysis (what's missing)
- Recommendation (apply / maybe / skip)

## Match Breakdown

```
Score = Tech Match (40%) + Level Match (30%) + Location (15%) + Salary (15%)
```

### Example

```
Job: "Senior Backend Engineer at Revolut"

Tech Match:
- Required: Java, Kotlin, Spring Boot, Kafka, PostgreSQL
- CV Has: Java ✅, Kotlin ✅, Spring Boot ✅, Kafka ✅, PostgreSQL ✅
- Missing: None
- Score: 100% × 40 = 40 pts

Level Match:
- Required: Senior (5+ years)
- CV: 3 years
- Gap: 2 years short
- Score: 50% × 30 = 15 pts

Location Match:
- Required: London / Remote UK
- CV Pref: Remote / EU / UK
- Match: Remote UK ✅
- Score: 80% × 15 = 12 pts

Salary Match:
- Offered: £80-120K
- Target: £100K+
- Match: Within range
- Score: 90% × 15 = 13.5 pts

Total: 80.5% → ⚠️ Partial match (level gap)

Recommendation: "Apply — strong tech fit, level gap can be addressed in interview"
```

## Best Practices

- ✅ Always show detailed breakdown
- ✅ Identify specific gaps
- ✅ Give actionable recommendation
- ✅ Include alternative roles if match is weak
- ❌ Never give score without explanation
