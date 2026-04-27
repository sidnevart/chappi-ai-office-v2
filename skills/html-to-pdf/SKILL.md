---
name: html_to_pdf
version: 1.0.0
description: Convert HTML to PDF using wkhtmltopdf or pandoc
---

# HTML to PDF Skill

Конвертирует HTML файлы в PDF для отправки в Telegram.

## Вход

```json
{
  "html_path": "/path/to/file.html",
  "output_path": "/path/to/output.pdf",
  "options": {
    "page_size": "A4",
    "margin": "20mm",
    "header": "AI Office Digest",
    "footer": "Page {page} of {total}"
  }
}
```

## Выход

```json
{
  "pdf_path": "/path/to/output.pdf",
  "pages": 10,
  "size_mb": 2.5
}
```

## Команды

```bash
# Using wkhtmltopdf
wkhtmltopdf --page-size A4 --margin-top 20mm --margin-bottom 20mm \
  --header-html header.html --footer-html footer.html \
  input.html output.pdf

# Using pandoc
pandoc input.html -o output.pdf --pdf-engine=wkhtmltopdf \
  -V geometry:margin=20mm
```
