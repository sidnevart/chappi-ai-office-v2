---
name: vector_index
version: 1.0.0
description: Index documents into vector database for RAG queries
---

# Vector Index Skill

Индексирует документы (PDF, HTML, MD, JSON) в векторную базу знаний.

## Вход

```json
{
  "documents": [
    {
      "path": "/path/to/doc.pdf",
      "type": "pdf|html|md|json",
      "metadata": {
        "category": "business|edu|career",
        "agent": "DealFlowTracker",
        "date": "2026-04-27",
        "tags": ["funding", "AI"]
      }
    }
  ]
}
```

## Выход

```json
{
  "indexed": 10,
  "chunks": 45,
  "vectors": 45,
  "db_path": "/home/user/research-system/vector_db/knowledge.db"
}
```

## Реализация

```python
import sqlite3
import sqlite_vec
import json

# Create vector DB
db = sqlite3.connect("/home/user/research-system/vector_db/knowledge.db")
db.enable_load_extension(True)
sqlite_vec.load(db)

# Create table
db.execute("""
  CREATE TABLE IF NOT EXISTS knowledge (
    id INTEGER PRIMARY KEY,
    text TEXT,
    embedding BLOB,
    metadata JSON,
    source TEXT,
    created_at TIMESTAMP
  )
""")
```
