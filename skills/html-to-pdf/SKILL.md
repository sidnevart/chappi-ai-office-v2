# HTML-to-PDF

## Purpose

Генерирует профессиональные PDF из HTML шаблонов. Используется для создания отчётов, pitch decks, business plans в формате PDF.

## When to Use

- Конвертация HTML отчётов в PDF
- Создание pitch decks для инвесторов
- Генерация business plan PDF
- Формирование printable reports

## Dependencies

```bash
pip install playwright
playwright install chromium
```

## Workflow

1. **Получить HTML:**
   - Загрузить HTML файл
   - Или сгенерировать HTML из markdown

2. **Применить стили:**
   - Добавить CSS для print media
   - Настроить header/footer
   - Добавить page breaks

3. **Конвертировать:**
   - Использовать playwright для рендеринга
   - Установить формат A4/Letter
   - Добавить margins
   - Экспортировать в PDF

4. **Опубликовать:**
   - Сохранить PDF в state
   - Загрузить в S3
   - Вернуть URL

## HTML Template Structure

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    @page { size: A4; margin: 20mm; }
    @page :first { margin-top: 0; }
    body { font-family: 'Segoe UI', sans-serif; line-height: 1.6; }
    h1 { page-break-before: always; }
    h1:first-of-type { page-break-before: auto; }
    table { page-break-inside: avoid; width: 100%; border-collapse: collapse; }
    .no-break { page-break-inside: avoid; }
    .cover { height: 100vh; display: flex; align-items: center; justify-content: center; background: linear-gradient(135deg, #667eea, #764ba2); color: white; }
    .metric { display: inline-block; padding: 15px 25px; background: linear-gradient(135deg, #667eea, #764ba2); color: white; border-radius: 8px; margin: 5px; text-align: center; }
    .metric-value { font-size: 28px; font-weight: bold; }
    .section { margin: 30px 0; }
    .highlight { background: #e8f5e9; padding: 15px; border-radius: 8px; }
  </style>
</head>
<body>
  <div class="cover">
    <h1>TeamMemory AI</h1>
    <p>AI-память команды</p>
  </div>
  
  <div class="section">
    <h2>Executive Summary</h2>
    <div class="metric">
      <span class="metric-value">$150M</span><br>Рынок СНГ
    </div>
    <div class="metric">
      <span class="metric-value">10.8x</span><br>LTV/CAC
    </div>
  </div>
  
  <div class="section">
    <h2>Market Analysis</h2>
    <table border="1">
      <tr><th>Сегмент</th><th>Размер</th><th>Рост</th></tr>
      <tr><td>Knowledge Management</td><td>$26.4B</td><td>47% CAGR</td></tr>
    </table>
  </div>
</body>
</html>
```

## Conversion Command

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.set_content(html_content)
    page.pdf(
        path="output.pdf",
        format="A4",
        margin={"top": "20mm", "right": "20mm", "bottom": "20mm", "left": "20mm"},
        print_background=True,
        display_header_footer=True,
        header_template='<div style="font-size:9px; margin-left:20mm; width:100%;">TeamMemory AI | Confidential</div>',
        footer_template='<div style="font-size:9px; margin-left:20mm; width:100%;"><span class="pageNumber"></span> / <span class="totalPages"></span></div>'
    )
    browser.close()
```

## Report Types

| Type | Template | CSS | Output |
|------|----------|-----|--------|
| Business Report | Professional | Minimal | A4 PDF |
| Pitch Deck | Investor-grade | Gradient cover | A4 landscape |
| Tech Spec | Engineering | Monospace code | A4 |
| Financial Model | Spreadsheet-like | Tables | A4 |

## Best Practices

- **Шрифты:** Использовать веб-безопасные (Segoe UI, Arial, Georgia)
- **Цвета:** Не использовать слишком яркие (печать)
- **Изображения:** Inline base64 или внешние URL
- **Page breaks:** Использовать `page-break-before/after/inside`
- **Header/Footer:** Добавлять номера страниц, дату, логотип
- **Accessibility:** Добавлять alt text, семантические теги

## Output Location

```
/mnt/files/research-state/reports/pdf/
├── team-memory-ai-report.pdf
├── team-memory-ai-pitch.pdf
├── vertical-ai-healthcare-tech-spec.pdf
└── ...
```
