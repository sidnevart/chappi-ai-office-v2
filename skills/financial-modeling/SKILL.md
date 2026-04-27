---
name: financial-modeling
description: Use when building financial projections, unit economics, or valuation models for startups
---

# Financial Modeling

## Overview

Builds financial models and produces **Google Sheets** for investors + JSON for pipeline.

## Output Formats

1. **JSON** (`/mnt/files/research-state/business/financial_models/*.json`) — for pipeline
2. **Google Sheets** — human-readable financial model with formulas
3. **S3 URL** — public access to sheets
4. **Telegram** — notification with Google Sheets link

## What This Skill Does NOT Produce

- ❌ HTML report (financial data belongs in spreadsheets)
- ❌ PDF (Google Sheets has built-in export)

## Workflow

### Step 1: Build Model in JSON

```json
{
  "assumptions": {
    "customers_year_1": 50,
    "arpu_monthly": 100,
    "cac": 200,
    "churn_monthly": 0.05
  },
  "projections": [...],
  "unit_economics": {
    "ltv": 2160,
    "cac": 200,
    "ltv_cac_ratio": 10.8
  }
}
```

### Step 2: Create Google Sheets

```python
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Create spreadsheet
service = build('sheets', 'v4', credentials=creds)
spreadsheet = {
    'properties': {'title': 'TeamMemory AI — Financial Model'}
}
result = service.spreadsheets().create(body=spreadsheet).execute()
spreadsheet_id = result['spreadsheetId']

# Add data
requests = [
    # Unit Economics
    {
        'updateCells': {
            'rows': [
                {'values': [
                    {'userEnteredValue': {'stringValue': 'Metric'}},
                    {'userEnteredValue': {'stringValue': 'Value'}},
                    {'userEnteredValue': {'stringValue': 'Notes'}}
                ]},
                {'values': [
                    {'userEnteredValue': {'stringValue': 'CAC'}},
                    {'userEnteredValue': {'numberValue': 200}},
                    {'userEnteredValue': {'stringValue': 'Organic + Performance'}}
                ]},
                # ... more rows
            ],
            'fields': 'userEnteredValue',
            'start': {'sheetId': 0, 'rowIndex': 0, 'columnIndex': 0}
        }
    }
]

body = {'requests': requests}
service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()

# Make public
permissions = {'type': 'anyone', 'role': 'reader'}
service_drive = build('drive', 'v3', credentials=creds)
service_drive.permissions().create(fileId=spreadsheet_id, body=permissions).execute()

sheet_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit"
```

### Step 3: Save References

```json
{
  "google_sheets_url": "https://docs.google.com/spreadsheets/d/.../edit",
  "spreadsheet_id": "...",
  "local_json": "/mnt/files/research-state/business/financial_models/...json"
}
```

### Step 4: Send to Telegram

```
💰 Financial Model: https://docs.google.com/spreadsheets/d/.../edit
```

## Google Sheets Structure

| Sheet | Content |
|-------|---------|
| Unit Economics | CAC, LTV, Payback, Churn |
| 5-Year Projections | Revenue, Customers, Team, EBITDA |
| Pricing | Tiers, ARPU, Packages |
| Funding | Stages, Amounts, Valuations |
| Assumptions | All model inputs |

## Best Practices

- ✅ Use Google Sheets formulas (not just values)
- ✅ Add charts in sheets
- ✅ Make read-only public link
- ✅ Include sensitivity analysis
- ❌ Don't duplicate data in HTML

## Commands

```bash
# Generate model
python3 skills/financial-modeling/build.py --idea=team-memory-ai

# Upload to Google Sheets
python3 skills/google-sheets-writer/upload.py --file=model.json --title="TeamMemory AI"

# Send to Telegram
python3 skills/telegram-reporter/send.py --message="💰 Financial Model" --url=$SHEET_URL
```
