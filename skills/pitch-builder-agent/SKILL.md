---
name: pitch-builder-agent
description: Agent skill for PitchBuilder. Creates HTML presentations for investors and stakeholders.
---

# PitchBuilder Agent

## Purpose

Presentation agent that creates professional HTML pitch decks for investors.

## Trigger

- Request from any business agent
- User request: "Создай питч"

## Input

- `/mnt/files/research-state/business/strategies/{idea}.json`
- Financial model data
- Company analysis

## Output

HTML file in `/mnt/files/research-state/business/pitches/{idea}.html`

## Process

1. Read all input data
2. Build pitch structure:
   - Problem
   - Solution
   - Market
   - Product
   - Traction
   - Business model
   - Competition
   - Team
   - Financials
   - Ask
3. Generate HTML with modern design
4. Save file

## Output Format

HTML file with:
- Responsive design
- Charts (via Chart.js)
- Professional styling
- Export to PDF ready

## Commands

When triggered, run:
1. Read input data
2. Generate HTML pitch
3. Save to pitches directory
4. Provide URL/path
