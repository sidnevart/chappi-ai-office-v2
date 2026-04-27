---
name: pitch_builder
version: 1.0.0
description: Generate HTML pitch decks with data from research
---

# Pitch Builder Skill

Создаёт HTML pitch deck презентации на основе данных из research.

## Вход

```json
{
  "company": "Company Name",
  "slides": [
    "cover",
    "problem",
    "solution",
    "market",
    "traction",
    "team",
    "financials",
    "ask"
  ],
  "data": {
    "market_size": "$10B",
    "problem": "...",
    "solution": "..."
  },
  "output_path": "/path/to/pitch.html"
}
```

## Выход

```json
{
  "html_path": "/path/to/pitch.html",
  "slides": 8,
  "preview_url": "http://localhost:5180/..."
}
```

## Шаблон

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    .slide { width: 100%; height: 100vh; display: flex; align-items: center; justify-content: center; }
    .cover { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
  </style>
</head>
<body>
  <div class="slide cover">
    <h1>{{company}}</h1>
    <p>{{tagline}}</p>
  </div>
  <!-- more slides -->
</body>
</html>
```
