---
name: edu_program_scout
version: 1.0.0
domains: [edu]
dependencies: [deep_research, cv_parser]
author: AI Office
---

# Edu Program Scout Skill

Поиск образовательных программ: буткемпы, летние школы, гранты, соревнования.

## Вход

```json
{
  "query": "AI engineering summer school Europe 2026",
  "filters": {
    "type": "bootcamp|summer_school|grant|competition",
    "field": "AI|SWE|Data Science|Product",
    "level": "undergrad|grad|professional",
    "location": "Europe|USA|Asia|Remote",
    "duration": "1week|1month|3months|6months",
    "cost": "free|paid|funded",
    "deadline_after": "2026-05-01"
  },
  "depth": "quick|standard|deep",
  "max_results": 10
}
```

## Выход

```json
{
  "programs": [
    {
      "name": "EEML Summer School",
      "type": "summer_school",
      "field": "AI",
      "location": "Europe",
      "dates": "2026-07-15 to 2026-07-30",
      "deadline": "2026-05-01",
      "cost": "free",
      "funding": "accommodation + travel",
      "url": "https://www.eeml.eu/home",
      "description": "...",
      "requirements": ["CV", "motivation letter", "recommendation"],
      "relevance_score": 0.95,
      "cv_match_score": 0.87
    }
  ],
  "metadata": {
    "total_found": 0,
    "filtered": 0,
    "search_time_seconds": 0
  }
}
```

## Шаги выполнения

1. **Search**: web_search с query + фильтры
2. **Filter**: Оставить только matching по датам/локации/уровню
3. **Enrich**: web_fetch для каждой программы (детали, дедлайны, требования)
4. **Score**: Сопоставить с CV (cv_parser skill)
5. **Rank**: Отсортировать по relevance_score + cv_match_score
6. **Export**: Сохранить в `research-state/edu/programs.json`

## Примеры

```python
# Search bootcamps
result = run_skill("edu_program_scout", {
    "query": "AI engineering bootcamp summer 2026",
    "filters": {"type": "bootcamp", "field": "AI", "location": "Europe"},
    "depth": "standard"
})

# Search grants
result = run_skill("edu_program_scout", {
    "query": "student grant AI project 2026",
    "filters": {"type": "grant", "cost": "free"},
    "depth": "deep"
})
```
