---
name: rate_limit_manager
description: |
  Rate limit management for web requests.
  Use when: (1) Multiple agents making requests, (2) Avoiding API limits,
  (3) Smart request distribution, (4) Queue management.
  
  Hashtags: #shared #rate-limit #api #queue
---

# RateLimitManager Skill

## Features

| Feature | Description |
|---------|-------------|
| **Token Bucket** | Smooth rate limiting |
| **Queue** | FIFO request queue |
| **Priority** | High/medium/low priority |
| **Backoff** | Exponential backoff on 429 |
| **Distribution** | Round-robin across keys |

## Configuration

```json
{
  "limits": {
    "openai": {"rpm": 60, "rpd": 10000},
    "google": {"rpm": 100, "rpd": 50000},
    "telegram": {"rpm": 30, "rpd": 20000}
  },
  "backoff": {
    "initial": 1,
    "multiplier": 2,
    "max": 60
  },
  "queue": {
    "max_size": 1000,
    "timeout": 300
  }
}
```

## Usage

```python
from rate_limit_manager import RateLimitManager

rlm = RateLimitManager()

# Check if can make request
if rlm.can_request("openai"):
    response = make_api_call()
else:
    wait_time = rlm.wait_time("openai")
    time.sleep(wait_time)

# Queue request
rlm.queue_request("google", priority="high", callback=process_result)
```

## Memory Storage

- entity_type: "rate_limit_config"
- tags: "shared,rate-limits,{provider}"
