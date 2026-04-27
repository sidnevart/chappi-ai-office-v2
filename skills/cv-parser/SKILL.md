---
name: cv-parser
description: Parse and analyze CV from PDF. Extract structured data for matching with programs and jobs.
---

# CV Parser Skill

Парсинг и анализ CV из PDF. Извлекает структурированные данные для matching с программами/вакансиями.

## Вход

```json
{
  "cv_source": "local|googledrive",
  "cv_path": "путь к файлу или ID",
  "output_format": "json|markdown|structured"
}
```

## Выход

```json
{
  "profile": {
    "name": "...",
    "title": "...",
    "email": "...",
    "links": {
      "telegram": "...",
      "linkedin": "...",
      "github": "...",
      "habr": "...",
      "twitter": "..."
    }
  },
  "summary": "краткое описание",
  "experience": [
    {
      "company": "...",
      "role": "...",
      "period": "...",
      "achievements": ["..."],
      "technologies": ["..."],
      "metrics": ["..."]
    }
  ],
  "skills": {
    "technical": ["..."],
    "soft": ["..."],
    "languages": ["..."]
  },
  "education": [
    {
      "institution": "...",
      "degree": "...",
      "field": "...",
      "period": "..."
    }
  ],
  "projects": [
    {
      "name": "...",
      "description": "...",
      "technologies": ["..."],
      "link": "..."
    }
  ],
  "achievements": ["..."],
  "metrics": {
    "years_experience": 0,
    "companies_count": 0,
    "projects_count": 0,
    "key_metrics": ["$600K+ business impact", "30M transactions/day"]
  }
}
```

## Шаги выполнения

1. **Extract**: Извлечь текст из PDF (smart_file_extract)
2. **Parse**: Разобрать на секции (Summary, Experience, Skills, Education, Projects)
3. **Extract entities**: Названия компаний, технологии, метрики, даты
4. **Normalize**: Привести к единому формату
5. **Score**: Оценить уровень (junior/mid/senior)
6. **Export**: Сохранить в structured формате

## Примеры использования

```python
# Parse local CV
result = parse_cv(
    cv_source="local",
    cv_path="/home/user/cv/sidnev_en_swe.pdf"
)

# Parse from Google Drive
result = parse_cv(
    cv_source="googledrive",
    cv_path="1zNEdmJjUl-gX90aDSEC3zCifW8DVcu-9"
)
```

## Технологии извлечения

- `smart_file_extract` для PDF парсинга
- Regex patterns для секций
- LLM для entity extraction
- Manual review для критичных данных
