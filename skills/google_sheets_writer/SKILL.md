---
name: google_sheets_writer
description: |
  Write data to Google Sheets.
  Use when: (1) User asks for spreadsheet, (2) Financial models,
  (3) Data export, (4) Collaborative editing.
  
  Input: Data + Sheet structure
  Output: Google Sheets file
  Hashtags: #shared #google #sheets #excel #данные
---

# GoogleSheetsWriter Skill

## Workflow

1. **Data preparation**: Clean and structure data
2. **Sheet design**: Tabs, columns, formulas
3. **Write data**: Batch insert
4. **Formatting**: Styles, conditional formatting
5. **Sharing**: Permissions, links

## Features

| Feature | Description |
|---------|-------------|
| Batch write | Multiple rows at once |
| Formulas | SUM, VLOOKUP, etc. |
| Formatting | Colors, borders, fonts |
| Charts | Visualizations |
| Sharing | Public, private, edit/view |

## Output Format

```json
{
  "spreadsheet": {
    "title": "Financial Model 2026",
    "sheets": [
      {
        "name": "Assumptions",
        "data": [
          ["Metric", "Value"],
          ["Growth Rate", "20%"],
          ["Churn Rate", "5%"]
        ]
      },
      {
        "name": "Revenue",
        "data": [
          ["Month", "Revenue"],
          ["Jan", "$100K"],
          ["Feb", "$120K"]
        ]
      }
    ],
    "url": "https://docs.google.com/spreadsheets/d/..."
  }
}
```

## Memory Storage

- entity_type: "spreadsheet"
- tags: "shared,google-sheets,{project}"
