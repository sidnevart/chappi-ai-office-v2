---
name: google-sheets-writer
description: Use when creating financial models or data tables in Google Sheets for collaborative editing
---

# Google Sheets Writer

## Overview

Creates financial models and data tables in Google Sheets. Used primarily by **Financial Modeling** skill.

## When to Use

- Financial projections
- Unit economics calculations
- Pricing tables
- Investor metrics
- Any data requiring formulas

**When NOT to use:**
- Simple reports → use HTML
- Technical specs → use Markdown
- Pitch decks → use HTML
- One-time data → use HTML

## Authentication

```python
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Load credentials from token file
creds = Credentials.from_authorized_user_file(
    '/mnt/files/.google/sheets-token.json',
    ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
)

service = build('sheets', 'v4', credentials=creds)
drive_service = build('drive', 'v3', credentials=creds)
```

## Workflow

### 1. Create Spreadsheet

```python
spreadsheet = {
    'properties': {
        'title': 'TeamMemory AI — Financial Model',
        'locale': 'ru_RU'
    },
    'sheets': [
        {'properties': {'title': 'Unit Economics'}},
        {'properties': {'title': '5-Year Projections'}},
        {'properties': {'title': 'Pricing'}},
        {'properties': {'title': 'Funding'}},
    ]
}

result = service.spreadsheets().create(body=spreadsheet).execute()
spreadsheet_id = result['spreadsheetId']
```

### 2. Add Data with Formulas

```python
# Unit Economics sheet
unit_economics_data = [
    ['Metric', 'Value', 'Formula', 'Notes'],
    ['CAC', 200, '', 'Organic + Performance'],
    ['LTV', 2160, '=B3*B4/B5', '18 months × ARPU'],
    ['LTV/CAC', 10.8, '=B3/B2', 'Target > 3x'],
    ['Payback (months)', 3, '=B2/(B3/18)', 'CAC / monthly profit'],
    ['Gross Margin', 0.8, '', 'SaaS standard'],
    ['Monthly Churn', 0.05, '', 'Conservative'],
]

body = {
    'values': unit_economics_data
}

service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id,
    range='Unit Economics!A1:D6',
    valueInputOption='USER_ENTERED',
    body=body
).execute()
```

### 3. Format Cells

```python
requests = [
    # Header formatting
    {
        'repeatCell': {
            'range': {'sheetId': 0, 'startRowIndex': 0, 'endRowIndex': 1},
            'cell': {
                'userEnteredFormat': {
                    'backgroundColor': {'red': 0.4, 'green': 0.49, 'blue': 0.92},
                    'textFormat': {'bold': True, 'foregroundColor': {'red': 1, 'green': 1, 'blue': 1}}
                }
            },
            'fields': 'userEnteredFormat(backgroundColor,textFormat)'
        }
    },
    # Currency formatting
    {
        'repeatCell': {
            'range': {'sheetId': 0, 'startRowIndex': 1, 'endRowIndex': 6, 'startColumnIndex': 1, 'endColumnIndex': 2},
            'cell': {
                'userEnteredFormat': {
                    'numberFormat': {'type': 'CURRENCY', 'pattern': '$#,##0'}
                }
            },
            'fields': 'userEnteredFormat.numberFormat'
        }
    }
]

service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body={'requests': requests}
).execute()
```

### 4. Add Charts

```python
chart_request = {
    'addChart': {
        'chart': {
            'spec': {
                'title': '5-Year Revenue Projection',
                'basicChart': {
                    'chartType': 'LINE',
                    'domains': [{'domain': {'sourceRange': {'sources': [{'sheetId': 1, 'startRowIndex': 1, 'endRowIndex': 6, 'startColumnIndex': 0, 'endColumnIndex': 1}]}}}],
                    'series': [{'series': {'sourceRange': {'sources': [{'sheetId': 1, 'startRowIndex': 1, 'endRowIndex': 6, 'startColumnIndex': 1, 'endColumnIndex': 2}]}}}]
                }
            },
            'position': {'overlayPosition': {'anchorCell': {'sheetId': 1, 'rowIndex': 8, 'columnIndex': 0}}}
        }
    }
}

service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body={'requests': [chart_request]}
).execute()
```

### 5. Make Public

```python
permissions = {
    'type': 'anyone',
    'role': 'reader',
    'allowFileDiscovery': False
}

drive_service.permissions().create(
    fileId=spreadsheet_id,
    body=permissions
).execute()

sheet_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit"
```

## Sheet Templates

### Unit Economics
| Metric | Value | Formula | Notes |
|--------|-------|---------|-------|
| CAC | $200 | - | Organic + Performance |
| LTV | $2,160 | =ARPU×LT | 18 months |
| LTV/CAC | 10.8x | =LTV/CAC | Target >3x |
| Payback | 3 mo | =CAC/Margin | Fast |

### 5-Year Projections
| Year | Revenue | Customers | Team | EBITDA |
|------|---------|-----------|------|--------|
| 1 | $86K | 50 | 5 | -30% |
| 2 | $432K | 200 | 10 | 10% |
| 3 | $1.9M | 800 | 20 | 25% |

## Best Practices

- ✅ Use formulas, not just values
- ✅ Add charts for visualization
- ✅ Format headers with colors
- ✅ Make read-only public link
- ✅ Include sensitivity analysis
- ❌ Don't hardcode all values
- ❌ Don't forget to make public

## Commands

```bash
# Create financial model
python3 skills/google-sheets-writer/create.py --template=financial-model --idea=team-memory-ai

# Update existing sheet
python3 skills/google-sheets-writer/update.py --spreadsheet-id=XXX --data=new-data.json

# Make public
python3 skills/google-sheets-writer/share.py --spreadsheet-id=XXX --visibility=public
```
