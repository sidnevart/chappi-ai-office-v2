# Skill: deep-research

## Назначение
Проведение глубокого исследования компании, продукта или темы через веб-поиск и анализ.

## Вход
```json
{
  "query": "название компании или тема",
  "depth": "quick|standard|deep",
  "focus": "products|competitors|funding|team|all"
}
```

## Выход
```json
{
  "profile": {
    "name": "...",
    "website": "...",
    "industry": "...",
    "founded": "...",
    "headquarters": "...",
    "employees": "...",
    "funding": "..."
  },
  "products": [...],
  "competitors": [...],
  "insights": [...],
  "sources": [...]
}
```

## Алгоритм
1. Web Search: 5 запросов по разным аспектам
2. Fetch контента с топ-10 результатов
3. Извлечение структурированных данных
4. Сохранение в `research/companies/{name}/`
5. Запись в Google Sheet "Company Database"

## Использование
```bash
openclaw skill run deep-research --query="OpenAI" --depth=deep --focus=all
```
