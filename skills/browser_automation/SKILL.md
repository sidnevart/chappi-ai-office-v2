---
name: browser_automation
description: |
  Automate browser actions: scrolling, dynamic content, rate limit management.
  Use when: (1) Scraping dynamic sites, (2) Need JavaScript rendering,
  (3) Complex navigation, (4) Rate-limited sites.
  
  Input: URL + Actions
  Output: Extracted content
  Hashtags: #shared #browser #автоматизация #скрапинг
---

# BrowserAutomation Skill

## Workflow

1. **Browser launch**: Headless or visible
2. **Navigation**: Go to URL
3. **Actions**: Click, scroll, type
4. **Wait**: For dynamic content
5. **Extract**: Content extraction
6. **Close**: Clean up

## Supported Actions

| Action | Description |
|--------|-------------|
| Navigate | Go to URL |
| Click | Click element |
| Type | Input text |
| Scroll | Page scroll |
| Wait | Wait for element |
| Screenshot | Capture screen |
| Extract | Get text/HTML |

## Rate Limit Management

| Strategy | Description |
|----------|-------------|
| Delays | Random delays between requests |
| Proxy rotation | Multiple IPs |
| User agents | Rotate UA strings |
| CAPTCHA solving | Handle challenges |

## Output Format

```json
{
  "url": "https://example.com",
  "actions": [
    {"type": "navigate", "url": "https://example.com"},
    {"type": "click", "selector": "#load-more"},
    {"type": "scroll", "amount": 1000},
    {"type": "wait", "selector": ".content"},
    {"type": "extract", "selector": ".article"}
  ],
  "result": {
    "content": "[extracted text]",
    "screenshots": ["screenshot1.png"],
    "success": true
  }
}
```

## Memory Storage

- entity_type: "browser_session"
- tags: "shared,browser,{url}"
