---
name: office-dashboard
description: |
  Dashboard UI for OpenClaw Office. Shows active agents, progress, artifacts.
  Use when: (1) User opens /office/, (2) Need to monitor system status,
  (3) Viewing research results, (4) Managing agents.
  
  Output: HTML dashboard
  Location: /office/
  Hashtags: #shared #dashboard #ui #office #мониторинг
---

# OfficeDashboard Skill

## Dashboard Components

| Widget | Description |
|--------|-------------|
| **Active Agents** | Currently running agents |
| **Cron Schedule** | Upcoming tasks |
| **Latest Digests** | Recent research results |
| **Knowledge Base** | Indexed entities count |
| **System Health** | Metrics, status |
| **Agent Logs** | Recent activity |

## Dashboard Layout

```
┌─────────────────────────────────────────┐
│  🤖 AI OFFICE DASHBOARD                 │
├─────────────────┬───────────────────────┤
│ ACTIVE AGENTS   │ CRON SCHEDULE         │
│ • DealFlowTrack │ 08:00 TrendMonitor      │
│ • TrendMonitor  │ 09:00 DealFlowTracker   │
│                 │ 09:30 EduBootcampScout  │
├─────────────────┼───────────────────────┤
│ LATEST DIGESTS  │ KNOWLEDGE BASE          │
│ • Business      │ 33 entities             │
│ • Education     │ 5 companies             │
│ • Career        │ 4 trends                │
├─────────────────┴───────────────────────┤
│ SYSTEM HEALTH                             │
│ CPU: 45%  RAM: 60%  Disk: 30%         │
│ Tokens: 243M  Cost: $87.60              │
└─────────────────────────────────────────┘
```

## Usage

```bash
# View dashboard
curl http://localhost:5180/office/
```

## Memory Storage

- entity_type: "dashboard_config"
- tags: "shared,dashboard,ui"
