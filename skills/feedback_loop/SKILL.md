---
name: feedback_loop
description: |
  User feedback system for agent improvement.
  Use when: (1) User rates digest, (2) Agent performance review,
  (3) Continuous improvement, (4) Quality metrics.
  
  Hashtags: #shared #feedback #улучшение #quality
---

# FeedbackLoop Skill

## Features

| Feature | Description |
|---------|-------------|
| **Rating** | 1-5 star rating |
| **Comments** | Free text feedback |
| **Tags** | Categorize feedback |
| **Metrics** | Quality scores |
| **Improvement** | Auto-adjustment |

## Feedback Types

| Type | When |
|------|------|
| **Digest Rating** | After receiving digest |
| **Agent Rating** | After agent execution |
| **Skill Rating** | After using skill |
| **System Rating** | Periodic survey |

## Usage

```python
from feedback_loop import FeedbackLoop

feedback = FeedbackLoop()

# Submit feedback
feedback.submit(
    agent="DealFlowTracker",
    rating=5,
    comment="Great deals found!",
    tags=["relevance", "speed"]
)

# Get metrics
metrics = feedback.get_metrics("DealFlowTracker")
print(f"Avg rating: {metrics['avg_rating']}")
```

## Memory Storage

- entity_type: "feedback"
- tags: "shared,feedback,{agent_name}"
