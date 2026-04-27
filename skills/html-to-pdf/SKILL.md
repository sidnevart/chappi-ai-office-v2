---
name: html-to-pdf
description: Use when generating professional PDF reports from HTML or markdown content, especially for business reports, pitch decks, and technical specifications with Cyrillic support
---

# HTML-to-PDF

## Overview

Generates detailed, professional PDF documents from HTML content with full Unicode/Cyrillic support. Uses ReportLab for reliable rendering without browser dependencies.

## When to Use

- Creating investor pitch decks
- Generating business analysis reports
- Exporting technical specifications
- Creating printable research summaries

**When NOT to use:**
- Simple text export → use plain text
- Spreadsheet data → use excel-builder
- Web content → use html-builder

## Requirements

```bash
pip install reportlab --break-system-packages
# OR
pip install reportlab
```

## PDF Structure

A complete business report PDF should be **10+ pages** with:

1. **Cover page** — Title, subtitle, date, key metrics (3-5 metrics cards)
2. **Executive Summary** — 1-2 paragraphs, key findings
3. **Market Analysis** — Tables with data, charts placeholders
4. **Competitive Landscape** — Competitor comparison table
5. **Product/Strategy** — Detailed breakdown
6. **Financial Model** — 5-year projections table
7. **Go-to-Market** — Strategy, channels, timeline
8. **Team & Ask** — Funding requirements
9. **Appendix** — Sources, methodology

## Workflow

### 1. Gather Content

Read all research artifacts:
```
research-state/business/ideas/{project}.json
research-state/business/companies/*.json
research-state/business/strategies/{project}.json
research-state/business/financial_models/{project}.json
```

### 2. Generate Rich HTML

Create detailed HTML with:
- All sections (8-10 slides/pages worth of content)
- Tables, metrics, bullet points
- Professional styling

### 3. Convert to PDF

Use ReportLab with Unicode fonts:

```python
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register Cyrillic font
pdfmetrics.registerFont(TTFont('DejaVuSans', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))

# Create document
doc = SimpleDocTemplate(
    "output.pdf",
    pagesize=A4,
    rightMargin=20*mm, leftMargin=20*mm,
    topMargin=20*mm, bottomMargin=20*mm
)

# Custom styles with Cyrillic support
title_style = ParagraphStyle(
    'CustomTitle',
    fontName='DejaVuSans-Bold',
    fontSize=32,
    textColor=HexColor('#1a237e'),
    spaceAfter=30,
    alignment=TA_CENTER
)

heading_style = ParagraphStyle(
    'CustomHeading',
    fontName='DejaVuSans-Bold',
    fontSize=18,
    textColor=HexColor('#3949ab'),
    spaceAfter=12,
    spaceBefore=12
)

body_style = ParagraphStyle(
    'CustomBody',
    fontName='DejaVuSans',
    fontSize=11,
    leading=14,
    spaceAfter=8,
    alignment=TA_JUSTIFY
)
```

### 4. Content Sections

Each section should be substantial:

**Cover (1 page):**
- Large title
- Subtitle
- 3-5 metric cards in a table
- Date, version

**Executive Summary (1-2 pages):**
- 2-3 paragraphs of text
- Key findings bullet list
- Recommendation

**Market Analysis (2-3 pages):**
- Market size table
- Growth trends
- Segment breakdown
- TAM/SAM/SOM

**Competition (1-2 pages):**
- Competitor comparison table (4-6 competitors)
- Feature matrix
- Differentiation analysis

**Financials (1-2 pages):**
- 5-year projections table
- Unit economics
- Funding requirements

**Strategy (1-2 pages):**
- Go-to-market plan
- Timeline with milestones
- Risk analysis

## Output Requirements

- **Minimum pages:** 10
- **Font:** Must support Cyrillic (DejaVu, Liberation, Noto)
- **Tables:** All data in formatted tables
- **Colors:** Professional palette (no bright colors)
- **Page numbers:** Footer with page numbers
- **Header:** Document title in header

## Example

```python
story = []

# Page 1: Cover
story.append(Paragraph("TeamMemory AI", title_style))
story.append(Paragraph("AI-память команды: ничего не теряется", subtitle_style))
story.append(Spacer(1, 30))

metrics = [
    ['Метрика', 'Значение'],
    ['Рынок СНГ', '$150M'],
    ['LTV/CAC', '10.8x'],
    ['Payback', '3 мес.'],
    ['Seed', '$1M']
]
table = Table(metrics, colWidths=[80*mm, 80*mm])
table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), HexColor('#667eea')),
    ('TEXTCOLOR', (0,0), (-1,0), white),
    ('FONTNAME', (0,0), (-1,0), 'DejaVuSans-Bold'),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('GRID', (0,0), (-1,-1), 1, HexColor('#ddd')),
]))
story.append(table)
story.append(PageBreak())

# Page 2-3: Executive Summary
story.append(Paragraph("Executive Summary", heading_style))
story.append(Paragraph("Detailed analysis here...", body_style))
story.append(Spacer(1, 15))
story.append(Paragraph("Key Findings:", heading_style))
findings = [
    "• Finding 1 with details...",
    "• Finding 2 with details...",
    "• Finding 3 with details..."
]
for f in findings:
    story.append(Paragraph(f, body_style))

# Continue for 10+ pages...

doc.build(story)
```

## Common Mistakes

- **Missing Cyrillic:** Always register Unicode fonts
- **Too short:** Minimum 10 pages for business report
- **No tables:** All structured data in tables
- **Missing sections:** Must have all 8 sections
- **No page breaks:** Use PageBreak() between sections
- **Wrong font:** Default Helvetica doesn't support Cyrillic
