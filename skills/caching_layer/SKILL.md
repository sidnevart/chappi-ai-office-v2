---
name: caching_layer
description: |
  Caching layer to prevent duplicate research.
  Use when: (1) Multiple agents request same data, (2) Need cache,
  (3) Reducing API calls, (4) Performance optimization.
  
  Storage: Redis or SQLite
  Hashtags: #shared #cache #performance #optimization
---

# CachingLayer Skill

## Features

| Feature | Description |
|---------|-------------|
| **TTL** | Time-based expiration |
| **Invalidation** | Manual cache clear |
| **Tags** | Grouped invalidation |
| **Size Limit** | Max cache size |
| **LRU** | Least Recently Used eviction |

## Configuration

```json
{
  "default_ttl": 3600,
  "max_size": 1000,
  "eviction": "lru",
  "storage": "sqlite"
}
```

## Usage

```python
from caching_layer import Cache

cache = Cache()

# Get or compute
result = cache.get_or_compute(
    key="deals_2026-04-27",
    compute=lambda: fetch_deals(),
    ttl=3600
)

# Invalidate
cache.invalidate_tag("deals")
```

## Memory Storage

- entity_type: "cache_entry"
- tags: "shared,cache,{tag}"
