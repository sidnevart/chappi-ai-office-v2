---
name: agent-event-bus
description: |
  Event bus for agent-to-agent communication.
  Use when: (1) Agent needs to send message to another agent,
  (2) Broadcasting events, (3) Triggering workflows,
  (4) Sharing research results between agents.
  
  Storage: SQLite database
  Location: /home/user/research-system/shared/state/event_bus.db
  Hashtags: #shared #event-bus #коммуникация #agents
---

# AgentEventBus Skill

## Usage

```python
from agent_event_bus import event_bus

# Send event to specific agent
event_bus.emit(
    event_type="deal_found",
    sender="DealFlowTracker",
    target="CompanyAnalyst",
    payload={"company": "OpenAI", "amount": "$122B"}
)

# Broadcast to all agents
event_bus.broadcast(
    event_type="trend_detected",
    sender="TrendMonitor",
    payload={"trend": "Physical AI", "strength": "strong"}
)

# Receive events
events = event_bus.receive("CompanyAnalyst", limit=5)
for event in events:
    print(f"{event['type']}: {event['payload']}")
```

## Event Types

| Type | Description | Sender → Target |
|------|-------------|----------------|
| `deal_found` | New deal discovered | DealFlowTracker → CompanyAnalyst |
| `trend_detected` | New trend identified | TrendMonitor → IdeaGenerator |
| `company_analyzed` | Company deep-dive complete | CompanyAnalyst → CompetitiveStrategist |
| `idea_generated` | New idea created | IdeaGenerator → CompetitiveStrategist |
| `strategy_ready` | Strategy complete | CompetitiveStrategist → FundingScout |
| `digest_ready` | Digest generated | Any → TelegramDispatcher |

## Workflow Example

```
DealFlowTracker → deal_found → CompanyAnalyst
CompanyAnalyst → company_analyzed → CompetitiveStrategist
CompetitiveStrategist → strategy_ready → FundingScout
FundingScout → funding_found → PitchBuilder
PitchBuilder → pitch_ready → TelegramDispatcher
```

## Memory Storage

- entity_type: "event"
- tags: "shared,events,{event_type}"
