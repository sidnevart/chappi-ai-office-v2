---
name: template-library
description: |
  HTML template library for different digest types.
  Use when: (1) Generating digest output, (2) Creating reports,
  (3) Building presentations, (4) Any HTML artifact.
  
  Templates: business, edu, career, trends, analysis, pitch
  Location: /home/user/research-system/templates/
  Hashtags: #shared #templates #html #дизайн
---

# TemplateLibrary Skill

## Available Templates

| Template | Description | File |
|----------|-------------|------|
| **Business Digest** | Deals, investments | `digest_business.html` |
| **Education Digest** | Programs, grants | `digest_edu.html` |
| **Career Digest** | Jobs, opportunities | `digest_career.html` |
| **Trend Report** | Market trends | `digest_trends.html` |
| **Company Profile** | Deep-dive analysis | `profile_company.html` |
| **Idea Card** | Generated idea | `card_idea.html` |
| **Competitive Map** | Market landscape | `map_competitive.html` |
| **Pitch Deck** | Investor presentation | `pitch_deck.html` |
| **Tech Spec** | Technical document | `doc_tech_spec.html` |
| **Salary Report** | Compensation data | `report_salary.html` |

## Template Structure

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    /* Brand colors */
    :root {
      --primary: #667eea;
      --secondary: #764ba2;
      --success: #28a745;
      --warning: #ffc107;
      --danger: #dc3545;
    }
  </style>
</head>
<body>
  <!-- Header -->
  <div class="header">
    <h1>{{title}}</h1>
    <p>{{subtitle}}</p>
  </div>
  
  <!-- Content -->
  <div class="content">
    {{content}}
  </div>
  
  <!-- Footer -->
  <div class="footer">
    <p>{{footer_text}}</p>
  </div>
</body>
</html>
```

## Usage

```python
from template_library import TemplateLibrary

templates = TemplateLibrary()
html = templates.render("digest_business", {
    "title": "Business Digest",
    "deals": [...],
    "date": "2026-04-27"
})
```

## Memory Storage

- entity_type: "template"
- tags: "shared,templates,{type}"
