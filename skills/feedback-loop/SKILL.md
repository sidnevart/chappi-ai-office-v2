---
name: feedback-loop
description: Use when processing user feedback and adapting agent behavior
---

# Feedback Loop

## Overview

Processes user feedback (👍/👎, comments, reactions) and adapts agent behavior.

## Storage

`/mnt/files/research-state/db/feedback.json`

## Schema

```json
{
  "version": "1.0",
  "feedback": [
    {
      "timestamp": "2026-04-28T02:40:00Z",
      "skill": "trend-monitor",
      "report": "trends-2026-04-28.html",
      "type": "reaction",
      "value": "👍",
      "comment": "Отличный анализ, но нужно больше источников"
    },
    {
      "timestamp": "2026-04-28T02:45:00Z",
      "skill": "idea-generator",
      "report": "ideas-2026-04-28.html",
      "type": "comment",
      "value": "Слишком общие идеи, нужно конкретнее",
      "adjustment": {
        "min_sources": 3,
        "require_market_size": true
      }
    }
  ],
  "preferences": {
    "trend-monitor": {
      "min_sources": 3,
      "depth": "detailed",
      "focus": "technical"
    },
    "idea-generator": {
      "min_sources": 4,
      "require_validation": true,
      "focus": "b2b"
    }
  },
  "blacklist": {
    "companies": ["CompanyX"],
    "topics": ["crypto"],
    "skills": []
  }
}
```

## Feedback Types

### 1. Telegram Reactions

| Reaction | Meaning | Action |
|----------|---------|--------|
| 👍 | Good | Increase weight, use similar approach |
| 👎 | Bad | Decrease weight, try different approach |
| ❤️ | Excellent | Save as template |
| 🤔 | Confusing | Add explanation next time |
| 🗑️ | Irrelevant | Add to blacklist |

### 2. Comments

Parse comments for adjustments:

```python
def parse_feedback(comment):
    adjustments = {}
    
    if "мало источников" in comment or "need more sources" in comment:
        adjustments['min_sources'] = current + 1
    
    if "слишком общие" in comment or "too general" in comment:
        adjustments['depth'] = 'detailed'
    
    if "не интересно" in comment or "not interested" in comment:
        adjustments['blacklist_topic'] = extract_topic()
    
    if "хорошо" in comment or "good" in comment:
        adjustments['weight'] = current * 1.2
    
    return adjustments
```

## Adaptation Rules

### 1. Source Count

| Feedback | Action |
|----------|--------|
| "Мало источников" | min_sources += 1 |
| "Слишком много" | min_sources -= 1 |
| "Источники не те" | Change source strategy |

### 2. Depth

| Feedback | Action |
|----------|--------|
| "Слишком поверхностно" | depth = "detailed" |
| "Слишком много деталей" | depth = "summary" |
| "Идеально" | keep current |

### 3. Focus

| Feedback | Action |
|----------|--------|
| "Нужно больше про технику" | focus = "technical" |
| "Больше про бизнес" | focus = "business" |
| "Нужны числа" | focus = "metrics" |

### 4. Blacklist

| Feedback | Action |
|----------|--------|
| "Не интересует компания X" | blacklist.company.add("X") |
| "Устал от крипто" | blacklist.topic.add("crypto") |
| "Этот скилл бесполезен" | blacklist.skill.add("skill_name") |

## Workflow

### Step 1: Capture Feedback

```python
def capture_feedback(skill, report, feedback_type, value, comment=None):
    fb = load_feedback()
    
    fb['feedback'].append({
        "timestamp": now(),
        "skill": skill,
        "report": report,
        "type": feedback_type,
        "value": value,
        "comment": comment
    })
    
    save_feedback(fb)
```

### Step 2: Parse Adjustments

```python
adjustments = parse_feedback(comment)
```

### Step 3: Update Preferences

```python
def update_preferences(skill, adjustments):
    fb = load_feedback()
    
    if skill not in fb['preferences']:
        fb['preferences'][skill] = {}
    
    for key, value in adjustments.items():
        if key == 'blacklist_topic':
            fb['blacklist']['topics'].append(value)
        elif key == 'blacklist_company':
            fb['blacklist']['companies'].append(value)
        else:
            fb['preferences'][skill][key] = value
    
    save_feedback(fb)
```

### Step 4: Apply to Next Run

```python
def get_skill_config(skill):
    fb = load_feedback()
    defaults = get_defaults(skill)
    prefs = fb['preferences'].get(skill, {})
    
    return {**defaults, **prefs}
```

## Integration

Every agent MUST load preferences before running:

```python
# In trend-monitor
def run():
    config = get_skill_config('trend-monitor')
    
    # Use preferences
    min_sources = config.get('min_sources', 2)
    depth = config.get('depth', 'standard')
    focus = config.get('focus', 'balanced')
    
    # Check blacklist
    blacklist = get_blacklist()
    trends = [t for t in trends if t not in blacklist['topics']]
    
    # Generate report with preferences
    report = generate_report(trends, min_sources=min_sources, depth=depth, focus=focus)
    
    return report
```

## Best Practices

- ✅ Capture all feedback
- ✅ Parse comments automatically
- ✅ Apply adjustments immediately
- ✅ Log all changes
- ❌ Never ignore feedback
- ❌ Never skip parsing
- ❌ Never lose preferences
