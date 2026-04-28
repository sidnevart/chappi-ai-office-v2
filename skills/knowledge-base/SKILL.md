---
name: knowledge-base
description: Shared knowledge base where agents learn from each other and accumulate research
---

# Knowledge Base

## Overview

Central knowledge repository where all agents store and share findings.
Prevents duplicate research and enables cross-domain insights.

## Location

`/mnt/files/research-state/db/knowledge.json`

## Schema

```json
{
  "version": "1.0",
  "last_updated": "2026-04-28T02:35:00Z",
  "facts": {
    "company:otter.ai": {
      "type": "company",
      "name": "Otter.ai",
      "users": "25M",
      "arr": "$100M",
      "funding": "$63M",
      "weaknesses": ["No Telegram", "No Russian"],
      "sources": ["https://otter.ai/blog", "https://pitchbook.com/..."],
      "discovered_by": "company-deep-dive",
      "confidence": "High",
      "updated_at": "2026-04-28T02:00:00Z"
    },
    "market:ai-meeting": {
      "type": "market",
      "size_2025": "$3.47B",
      "cagr": "25.8%",
      "sources": ["https://grandviewresearch.com/..."],
      "discovered_by": "trend-monitor",
      "used_by": ["idea-generator", "competitive-analysis"],
      "confidence": "High",
      "updated_at": "2026-04-28T02:00:00Z"
    },
    "tech:telegram-bot-api": {
      "type": "technology",
      "description": "Bot API for Telegram integration",
      "docs": "https://core.telegram.org/bots/api",
      "used_in": ["team-memory-ai"],
      "discovered_by": "tech-spec-writer",
      "confidence": "High",
      "updated_at": "2026-04-28T02:00:00Z"
    }
  },
  "relationships": {
    "company:otter.ai": ["market:ai-meeting", "tech:voice-transcription"],
    "market:ai-meeting": ["company:otter.ai", "company:fireflies.ai", "company:read.ai"]
  },
  "queries": {
    "ai meeting market size 2026": {
      "last_answer": "market:ai-meeting",
      "asked_by": ["trend-monitor", "idea-generator"],
      "timestamp": "2026-04-28T02:00:00Z"
    }
  }
}
```

## Rules

### 1. Store Every Finding

Every agent MUST store findings:

```python
def store_fact(entity_type, entity_id, data, discovered_by):
    kb = load_kb()
    
    key = f"{entity_type}:{entity_id}"
    kb['facts'][key] = {
        "type": entity_type,
        **data,
        "discovered_by": discovered_by,
        "confidence": data.get('confidence', 'Medium'),
        "updated_at": now()
    }
    
    save_kb(kb)
```

### 2. Check Before Research

```python
def check_kb(query):
    kb = load_kb()
    
    # Check if we already know this
    for key, fact in kb['facts'].items():
        if query.lower() in key.lower() or query.lower() in str(fact).lower():
            return fact
    
    # Check relationships
    for entity, related in kb['relationships'].items():
        if query in related:
            return kb['facts'].get(entity)
    
    return None
```

### 3. Cross-Domain Learning

When TrendMonitor finds a trend → IdeaGenerator uses it:

```python
# In idea-generator
def generate_idea(trend):
    kb = load_kb()
    
    # Check if we know about this trend
    trend_data = check_kb(trend)
    if trend_data:
        # Use existing knowledge
        market_size = trend_data['market_size']
        competitors = trend_data.get('competitors', [])
    else:
        # Research
        trend_data = research(trend)
        store_fact('market', trend, trend_data, 'trend-monitor')
    
    return generate_idea_with_data(trend_data)
```

### 4. Incremental Updates

Don't replace, update:

```python
def update_fact(key, new_data, updated_by):
    kb = load_kb()
    fact = kb['facts'].get(key, {})
    
    for field, value in new_data.items():
        if value != fact.get(field):
            fact[field] = value
            fact['updated_at'] = now()
    
    fact['updated_by'] = updated_by
    kb['facts'][key] = fact
    save_kb(kb)
```

## API

```python
class KnowledgeBase:
    def __init__(self, path='/mnt/files/research-state/db/knowledge.json'):
        self.path = path
        self.data = self.load()
    
    def load(self):
        if os.path.exists(self.path):
            with open(self.path) as f:
                return json.load(f)
        return {"version": "1.0", "facts": {}, "relationships": {}, "queries": {}}
    
    def save(self):
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
    
    def get(self, key):
        return self.data['facts'].get(key)
    
    def set(self, key, value):
        self.data['facts'][key] = value
        self.save()
    
    def query(self, text):
        results = []
        for key, fact in self.data['facts'].items():
            if text.lower() in key.lower() or text.lower() in str(fact).lower():
                results.append(fact)
        return results
    
    def related(self, key):
        related_keys = self.data['relationships'].get(key, [])
        return [self.data['facts'].get(k) for k in related_keys]
```

## Integration

Every agent MUST:
1. Check KB before research
2. Store findings in KB
3. Use KB data when available

```python
# In company-deep-dive
def analyze_company(company_name):
    kb = KnowledgeBase()
    
    # Check if we already know this company
    cached = kb.get(f"company:{company_name}")
    if cached and is_fresh(cached):
        return cached
    
    # Research
    data = research_company(company_name)
    
    # Store
    kb.set(f"company:{company_name}", {
        **data,
        "discovered_by": "company-deep-dive",
        "updated_at": now()
    })
    
    return data
```

## Best Practices

- ✅ Always check KB first
- ✅ Store every finding
- ✅ Link related entities
- ✅ Incremental updates
- ❌ Never duplicate research
- ❌ Never skip KB update
- ❌ Never lose data on crash
