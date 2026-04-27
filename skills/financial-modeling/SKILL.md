---
name: financial-modeling
description: Use when building financial projections with evidence-based assumptions and Google Sheets output
---

# Financial Modeling (Evidence-Based)

## Overview

Builds financial models and produces:
1. **Google Sheets** — PRIMARY human-readable format with formulas
2. **HTML Report** — summary with evidence
3. **S3 URL** — public access
4. **Telegram** — notification with link

## Output Formats

| Format | Purpose | Tool |
|--------|---------|------|
| **Google Sheets** | Human analysis, formulas, charts | Google Sheets API |
| **HTML Summary** | Quick overview with key metrics | HTML |
| **Excel** | Backup, offline use | openpyxl |
| **JSON** | Pipeline only (internal) | — |

**NO standalone JSON for humans.**

## Evidence Requirements

Every assumption MUST have:
- **Source**: Where the number came from
- **Method**: How it was calculated
- **Confidence**: High/Medium/Low
- **Sensitivity**: What if this is wrong?

## Google Sheets Structure

### Sheet 1: Assumptions (with Evidence)

| Assumption | Value | Source | Method | Confidence | If Wrong |
|------------|-------|--------|--------|------------|----------|
| CAC | $200 | Comparable SaaS | Benchmarking | Medium | ±50% |
| ARPU | $100 | Market research | Survey data | High | ±20% |
| Churn | 5% | Industry standard | Benchmarking | Medium | ±30% |

### Sheet 2: Unit Economics

| Metric | Formula | Result | Source |
|--------|---------|--------|--------|
| LTV | =B2*B3/B4 | $2,160 | Standard SaaS formula |
| LTV/CAC | =B5/B1 | 10.8x | Target >3x |
| Payback | =B1/(B2*B3) | 3 months | Industry standard |

### Sheet 3: 5-Year Projections

| Year | Revenue | Customers | Team | EBITDA |
|------|---------|-----------|------|--------|
| 1 | =B2*B3*12 | 50 | 5 | -30% |
| 2 | =B2*1.2 | =B3*4 | 10 | 10% |

### Sheet 4: Sensitivity Analysis

| Variable | -20% | Base | +20% |
|----------|------|------|------|
| CAC | 13.5x | 10.8x | 9.0x |
| Churn | 13.5x | 10.8x | 9.0x |

## Workflow

### Step 1: Research Assumptions

For each assumption:
1. Search comparable companies
2. Find benchmarks
3. Calculate from data
4. Document sources

### Step 2: Build Model in Sheets

```python
from googleapiclient.discovery import build

service = build('sheets', 'v4', credentials=creds)

# Create spreadsheet
spreadsheet = {'properties': {'title': 'TeamMemory AI — Financial Model'}}
result = service.spreadsheets().create(body=spreadsheet).execute()
spreadsheet_id = result['spreadsheetId']

# Add formulas
requests = [
    {
        'updateCells': {
            'rows': [
                {'values': [
                    {'userEnteredValue': {'stringValue': 'Metric'}},
                    {'userEnteredValue': {'stringValue': 'Value'}},
                    {'userEnteredValue': {'stringValue': 'Source'}}
                ]},
                {'values': [
                    {'userEnteredValue': {'stringValue': 'CAC'}},
                    {'userEnteredValue': {'numberValue': 200}},
                    {'userEnteredValue': {'stringValue': 'Benchmark: https://...'}}
                ]}
            ],
            'fields': 'userEnteredValue',
            'start': {'sheetId': 0, 'rowIndex': 0, 'columnIndex': 0}
        }
    }
]

service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body={'requests': requests}).execute()
```

### Step 3: Generate HTML Summary

```html
<h1>💰 Financial Model: TeamMemory AI</h1>

<div class="metrics">
  <div class="metric">
    <span class="value">$2,160</span>
    <span class="label">LTV</span>
    <span class="source">Source: Benchmark</span>
  </div>
  <div class="metric">
    <span class="value">10.8x</span>
    <span class="label">LTV/CAC</span>
    <span class="source">Source: Calculation</span>
  </div>
</div>

<p><strong>Full model:</strong> <a href="https://docs.google.com/spreadsheets/d/...">Google Sheets</a></p>
```

### Step 4: Upload & Share

```python
# Make public
drive_service.permissions().create(
    fileId=spreadsheet_id,
    body={'type': 'anyone', 'role': 'reader'}
).execute()

sheet_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit"
```

## Best Practices

- ✅ All formulas in Sheets (not hardcoded)
- ✅ Assumptions documented with sources
- ✅ Sensitivity analysis included
- ✅ Charts for visualization
- ❌ No hardcoded values without formula
- ❌ No model without sensitivity analysis
- ❌ No assumption without source

## Commands

```bash
# Build model
python3 skills/financial-modeling/build.py --idea=team-memory-ai

# Upload to Google Sheets
python3 skills/google-sheets-writer/upload.py --file=model.json

# Generate HTML summary
python3 skills/html-builder/build.py --input=model-summary.json --template=financial

# Send to Telegram
python3 skills/telegram-reporter/send.py --message="💰 Financial Model" --url=$SHEET_URL
```
