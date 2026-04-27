---
name: excel_builder
version: 1.0.0
description: Generate Excel files with financial models, data tables, analysis
---

# Excel Builder Skill

Создаёт Excel файлы с финансовыми моделями, таблицами данных, анализом.

## Вход

```json
{
  "template": "financial_model|data_table|competitive_analysis",
  "data": {},
  "sheets": [
    {
      "name": "Summary",
      "type": "table|chart|pivot"
    }
  ],
  "output_path": "/path/to/output.xlsx"
}
```

## Выход

```json
{
  "excel_path": "/path/to/output.xlsx",
  "sheets": 3,
  "rows": 150
}
```

## Примеры

```python
import openpyxl
from openpyxl.styles import Font, PatternFill

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Financial Model"

# Headers
ws['A1'] = 'Metric'
ws['B1'] = 'Value'
ws['A1'].font = Font(bold=True, color="FFFFFF")
ws['A1'].fill = PatternFill(start_color="667EEA", end_color="667EEA", fill_type="solid")

# Data
ws['A2'] = 'TAM'
ws['B2'] = '$10B'

wb.save("/path/to/output.xlsx")
```
