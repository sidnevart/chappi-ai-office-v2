---
name: deep-research
description: Basic web research skill. Used by all domains - edu, career, business.
---

# Deep Research Skill

Базовый skill для web research. Используется всеми доменами: edu, career, business.

## Вход

```json
{
  "query": "строка поиска",
  "depth": "quick|standard|deep",
  "sources": ["web", "news", "academic"],
  "max_results": 10,
  "filters": {
    "date_range": "last_month|last_year|any",
    "language": "en|ru|any"
  }
}
```

## Выход

```json
{
  "query": "оригинальный запрос",
  "results": [
    {
      "title": "...",
      "url": "...",
      "snippet": "...",
      "source": "web|news|academic",
      "date": "YYYY-MM-DD",
      "relevance_score": 0.0-1.0
    }
  ],
  "synthesis": {
    "summary": "сжатый пересключ",
    "key_points": ["..."],
    "gaps": ["чего не хватает"],
    "next_queries": ["следующие запросы"]
  },
  "metadata": {
    "sources_checked": 0,
    "time_spent_seconds": 0,
    "timestamp": "..."
  }
}
```

## Шаги выполнения

1. **Search**: web_search с query
2. **Fetch**: web_fetch для топ-N результатов
3. **Extract**: Извлечение ключевой информации
4. **Synthesize**: Обобщение и структурирование
5. **Validate**: Проверка полноты и точности

## Параметры depth

| Уровень | Описание | Время |
|---------|----------|-------|
| quick | 3-5 источников, краткий пересказ | 1-2 мин |
| standard | 5-10 источников, полный анализ | 3-5 мин |
| deep | 10-20 источников, глубокий анализ + cross-reference | 10-15 мин |

## Примеры использования

```python
# Quick research
result = run_deep_research(
    query="YCombinator summer 2026 batch deadline",
    depth="quick"
)

# Deep research
result = run_deep_research(
    query="Physical AI market size 2026 investments",
    depth="deep",
    sources=["web", "news"],
    filters={"date_range": "last_year", "language": "en"}
)
```
