---
name: state-persistence
description: Use when tracking research state to avoid duplicate work and enable incremental updates
---

# State Persistence

## Overview

Tracks what has been researched, when, and by whom.
Prevents duplicate work and enables incremental updates.

## Database

Location: `/mnt/files/research-state/db/state.json`

### Schema

```json
{
  "version": "1.0",
  "last_updated": "2026-04-28T02:30:00Z",
  "entities": {
    "companies": {
      "otter.ai": {
        "last_researched": "2026-04-28T02:00:00Z",
        "by_skill": "company-deep-dive",
        "data_hash": "sha256:abc123...",
        "ttl_days": 7,
        "sources_checked": [
          "https://otter.ai/blog",
          "https://pitchbook.com/..."
        ],
        "fields": {
          "users": {"value": "25M", "updated": "2026-04-28"},
          "arr": {"value": "$100M", "updated": "2026-04-28"},
          "funding": {"value": "$63M", "updated": "2026-04-28"}
        }
      }
    },
    "trends": {
      "ai-meeting-assistants": {
        "last_researched": "2026-04-28T02:00:00Z",
        "by_skill": "trend-monitor",
        "ttl_days": 3,
        "market_size": "$3.47B"
      }
    },
    "jobs": {
      "revolut-senior-backend": {
        "last_researched": "2026-04-28T02:00:00Z",
        "by_skill": "job-scout",
        "ttl_days": 1,
        "status": "active"
      }
    }
  }
}
```

## Rules

### 1. Before Research — Check State

```python
def should_research(entity_type, entity_id):
    state = load_state()
    entity = state.get(entity_type, {}).get(entity_id)
    
    if not entity:
        return True  # Never researched
    
    age = now() - entity['last_researched']
    ttl = timedelta(days=entity['ttl_days'])
    
    if age > ttl:
        return True  # Stale data
    
    return False  # Fresh enough
```

### 2. TTL by Entity Type

| Entity Type | TTL | Reason |
|-------------|-----|--------|
| Company | 7 days | Company data changes slowly |
| Trend | 3 days | Trends evolve fast |
| Job | 1 day | Jobs expire quickly |
| Bootcamp | 7 days | Deadlines approaching |
| Competition | 3 days | New competitions appear |
| Grant | 7 days | Funding cycles |

### 3. Incremental Updates

Don't re-research everything. Update only changed fields:

```python
def update_entity(entity_type, entity_id, new_data):
    old = state[entity_type][entity_id]
    
    for field, value in new_data.items():
        if old['fields'].get(field) != value:
            old['fields'][field] = {
                "value": value,
                "updated": now()
            }
    
    old['last_researched'] = now()
    save_state(state)
```

### 4. Force Refresh

User can force re-research:
```
"Обнови данные по Otter.ai" → ignore TTL, force refresh
```

## Workflow

### Step 1: Check Before Research
```python
if not should_research('companies', 'otter.ai'):
    # Load from state
    cached = state['entities']['companies']['otter.ai']
    return cached['fields']
```

### Step 2: Research (if needed)
```python
# Do research...
new_data = web_search("otter.ai 2026")
```

### Step 3: Update State
```python
update_entity('companies', 'otter.ai', new_data)
```

### Step 4: Log Decision
```json
{
  "timestamp": "2026-04-28T02:30:00Z",
  "entity": "companies/otter.ai",
  "action": "used_cache",
  "reason": "Age 2h < TTL 7d",
  "saved_time": "~30 seconds"
}
```

## State API

```python
def load_state():
    """Load state from disk"""
    with open('/mnt/files/research-state/db/state.json') as f:
        return json.load(f)

def save_state(state):
    """Save state to disk"""
    with open('/mnt/files/research-state/db/state.json', 'w') as f:
        json.dump(state, f, indent=2, ensure_ascii=False)

def get_entity(entity_type, entity_id):
    """Get entity from state"""
    state = load_state()
    return state.get('entities', {}).get(entity_type, {}).get(entity_id)

def update_entity(entity_type, entity_id, data):
    """Update entity in state"""
    state = load_state()
    state.setdefault('entities', {}).setdefault(entity_type, {})[entity_id] = data
    save_state(state)
```

## Integration with Agents

Every agent MUST check state before research:

```python
# In trend-monitor
def run():
    trends = ['ai-meeting-assistants', 'physical-ai', 'vertical-saas']
    
    for trend in trends:
        if should_research('trends', trend):
            data = research(trend)
            update_state('trends', trend, data)
        else:
            data = load_from_state('trends', trend)
        
        report.add(data)
```

## Best Practices

- ✅ Always check state first
- ✅ Respect TTL
- ✅ Incremental updates
- ✅ Log decisions
- ❌ Never re-research without reason
- ❌ Never skip state update
- ❌ Never lose state on crash
