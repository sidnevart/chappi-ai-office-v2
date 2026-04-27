---
name: html-builder
description: Create HTML artifacts (presentations, reports, dashboards) for OpenClaw Office UI.
---

# HTML Artifact Builder Skill

Создание HTML-артефактов (презентации, отчёты, дашборды) для OpenClaw Office UI.

## Вход

```json
{
  "template": "pitch|report|dashboard|comparison",
  "title": "...",
  "data": {},
  "sections": ["..."],
  "output_path": "/home/user/research-system/...",
  "style": "minimal|corporate|creative"
}
```

## Выход

```json
{
  "html_path": "/path/to/file.html",
  "preview_url": "http://localhost:5180/...",
  "sections_rendered": 0,
  "charts_count": 0,
  "tables_count": 0
}
```

## Шаблоны

### pitch
- Слайды с cover, problem, solution, market, traction, team, ask
- CSS transitions, responsive
- Export to PDF via print

### report
- TOC, sections, charts, tables
- Dark/light mode toggle
- Collapsible sections

### dashboard
- Cards, metrics, charts
- Real-time updates via SSE
- Filters and date ranges

### comparison
- Side-by-side tables
- Highlight differences
- Score bars

## Примеры использования

```python
# Build pitch deck
result = build_html_artifact(
    template="pitch",
    title="CompanyX Analysis",
    data={
        "company": "CompanyX",
        "market_size": "$10B",
        "problem": "...",
        "solution": "..."
    },
    sections=["cover", "problem", "solution", "market", "competition", "financials", "ask"],
    output_path="/home/user/research-system/business/pitches/companyx.html"
)
```

## Технологии

- Pure HTML/CSS/JS (no external deps)
- Tailwind-like utility classes
- Chart.js for charts
- Markdown rendering
