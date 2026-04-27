---
name: agent-logger
description: |
  Agent activity logging system.
  Use when: (1) Agent completes task, (2) Need audit trail,
  (3) Debugging, (4) Performance monitoring.
  
  Storage: /home/user/research-system/shared/logs/research-log/YYYY-MM-DD/
  Hashtags: #shared #logging #логи #audit
---

# AgentLogger Skill

## Log Structure

```
research-log/
├── 2026-04-27/
│   ├── trend_monitor.json
│   ├── deal_flow_tracker.json
│   ├── edu_bootcamp_scout.json
│   └── job_scout.json
├── 2026-04-28/
│   └── ...
```

## Log Format

```json
{
  "agent": "DealFlowTracker",
  "timestamp": "2026-04-27T09:00:00Z",
  "duration_ms": 45000,
  "status": "success",
  "tasks": [
    {
      "task": "web_search",
      "status": "success",
      "results": 10,
      "duration_ms": 15000
    },
    {
      "task": "deep_research",
      "status": "success",
      "results": 4,
      "duration_ms": 25000
    }
  ],
  "output": {
    "deals_found": 4,
    "total_amount": "$131B+",
    "digest_path": ".../digest_business_2026-04-27.html",
    "telegram_sent": true
  },
  "errors": [],
  "warnings": ["Rate limit approaching"]
}
```

## Usage

```python
from agent_logger import AgentLogger

logger = AgentLogger()
logger.log("DealFlowTracker", {
    "status": "success",
    "deals_found": 4
})
```

## Memory Storage

- entity_type: "agent_log"
- tags: "shared,logs,{agent_name},{date}"
