---
name: cv-pipeline-orchestrator
description: Orchestrator that runs CV-aware matching across all domains (career, edu, business)
---

# CV Pipeline Orchestrator

## Overview

Runs CV-aware pipeline across all domains:
1. Load CV profile
2. Run scouts with CV filter
3. Match opportunities
4. Filter by score
5. Generate report

## Pipeline

```
Load CV
    ↓
[Career] Job Scout → CV Match → Filter → Report
    ↓
[Edu] Bootcamp Scout → CV Match → Filter → Report
[Edu] Competition Scout → CV Match → Filter → Report
[Edu] Grant Scout → CV Match → Filter → Report
    ↓
Merge all results
    ↓
Weekly Matcher (CV-aware)
    ↓
Telegram Report with match scores
```

## CV Profile

```json
{
  "name": "Artem Sidnev",
  "role": "Software Engineer (Backend)",
  "experience_years": 3,
  "current_company": "T-Bank",
  "skills": ["Java", "Kotlin", "Go", "Python", "TypeScript", 
             "Spring Boot", "PostgreSQL", "ClickHouse", "Redis", "Kafka",
             "GitLab CI", "n8n", "RAG", "AI agents"],
  "achievements": [
    "$600K+ annual business impact",
    "5x performance improvement",
    "40-60 hours/month manual work saved"
  ],
  "education": "Canisius University | Bachelor of Computer Science",
  "languages": ["Russian", "English"],
  "location_preference": "Remote / EU / UK",
  "salary_target": "$100K-$150K/year"
}
```

## Output Format

```html
<h1>📋 Подходящие возможности для Артёма</h1>
<p>📅 [Date] | Матчинг по CV</p>

<h2>💼 Работа (Score > 60%)</h2>
<div class="opportunity">
  <h3>Senior Backend @ Revolut — 80%</h3>
  <ul>
    <li>Tech: Java, Kotlin, Spring Boot ✅ (100%)</li>
    <li>Level: Senior (5y) vs 3y — gap 2y ⚠️</li>
    <li>Location: Remote UK ✅</li>
    <li>Salary: £120K ✅</li>
  </ul>
  <p><strong>Рекомендация:</strong> Откликнуться — сильный tech fit</p>
</div>

<h2>🎓 Образование (Score > 50%)</h2>
<div class="opportunity">
  <h3>EEML Summer School — 75%</h3>
  <ul>
    <li>Tech: ML, Python ✅ (80%)</li>
    <li>Level: Advanced — подходит ⚠️</li>
    <li>Deadline: 15 мая ⚠️</li>
  </ul>
</div>

<h2>🚀 Стартап-идеи (на основе CV)</h2>
<div class="idea">
  <h3>AI Agent Workflow Platform — 90%</h3>
  <p>Опыт: RAG, n8n, AI agents → идеальный founder fit</p>
</div>
```

## Best Practices

- ✅ Always load CV first
- ✅ Show match score for every item
- ✅ Explain gaps
- ✅ Give clear recommendation
- ❌ Never include items without score
- ❌ Never skip without reason
