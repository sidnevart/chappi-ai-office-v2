---
name: local-vector-db
description: |
  Local vector database for semantic search using SQLite + sentence-transformers.
  Use when: (1) Need to store embeddings for semantic search, (2) Memory retrieval by meaning,
  (3) Fast local search without external APIs, (4) Indexing digests, entities, research data.
  
  Replaces: MEM0, Supabase vector storage
  Location: /home/user/research-system/vector_db/
---

# Local Vector Database Skill

## Architecture

```
vector_db/
├── knowledge.db          # SQLite database
│   ├── entities          # Companies, programs, jobs
│   ├── digests           # Generated digests
│   ├── sessions          # Chat sessions
│   └── vectors           # Vector embeddings (FAISS or numpy)
└── embeddings/           # Cached sentence embeddings
```

## Implementation

```python
import sqlite3
import numpy as np
from sentence_transformers import SentenceTransformer

class LocalVectorDB:
    def __init__(self, db_path="/home/user/research-system/vector_db/knowledge.db"):
        self.db = sqlite3.connect(db_path)
        self.encoder = SentenceTransformer('all-MiniLM-L6-v2')
        self._init_tables()
    
    def _init_tables(self):
        """Create tables if not exist"""
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS vectors (
                id INTEGER PRIMARY KEY,
                text TEXT,
                embedding BLOB,
                entity_type TEXT,
                entity_id TEXT,
                metadata TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS entities (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE,
                type TEXT,
                data TEXT,
                tags TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.db.commit()
    
    def add(self, text: str, entity_type: str, entity_id: str, metadata: dict = None):
        """Add text with vector embedding"""
        embedding = self.encoder.encode(text)
        embedding_bytes = embedding.tobytes()
        
        self.db.execute("""
            INSERT INTO vectors (text, embedding, entity_type, entity_id, metadata)
            VALUES (?, ?, ?, ?, ?)
        """, (text, embedding_bytes, entity_type, entity_id, str(metadata)))
        self.db.commit()
    
    def search(self, query: str, top_k: int = 5) -> list:
        """Semantic search by query"""
        query_vector = self.encoder.encode(query)
        
        cursor = self.db.execute("SELECT text, embedding, entity_type, entity_id, metadata FROM vectors")
        results = []
        
        for row in cursor.fetchall():
            text, embedding_bytes, entity_type, entity_id, metadata = row
            stored_vector = np.frombuffer(embedding_bytes, dtype=np.float32)
            
            # Cosine similarity
            similarity = np.dot(query_vector, stored_vector) / (np.linalg.norm(query_vector) * np.linalg.norm(stored_vector))
            
            results.append({
                "text": text,
                "similarity": float(similarity),
                "entity_type": entity_type,
                "entity_id": entity_id,
                "metadata": metadata
            })
        
        # Sort by similarity
        results.sort(key=lambda x: x["similarity"], reverse=True)
        return results[:top_k]
    
    def get_entity(self, name: str) -> dict:
        """Get entity by name"""
        cursor = self.db.execute("SELECT * FROM entities WHERE name = ?", (name,))
        row = cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "name": row[1],
                "type": row[2],
                "data": row[3],
                "tags": row[4]
            }
        return {}
    
    def add_entity(self, name: str, entity_type: str, data: dict, tags: str = ""):
        """Add or update entity"""
        self.db.execute("""
            INSERT OR REPLACE INTO entities (name, type, data, tags)
            VALUES (?, ?, ?, ?)
        """, (name, entity_type, str(data), tags))
        self.db.commit()
        
        # Also add to vectors for semantic search
        text = f"{name}: {data}"
        self.add(text, entity_type, name, data)
```

## Usage

```python
# Initialize
from local_vector_db import LocalVectorDB

db = LocalVectorDB()

# Add digest content
db.add(
    text="OpenAI raised $122B in funding for AI/LLM development",
    entity_type="company",
    entity_id="OpenAI",
    metadata={"amount": "$122B", "field": "AI/LLM", "date": "2026-04-27"}
)

# Semantic search
results = db.search("AI funding rounds 2026", top_k=5)
for r in results:
    print(f"{r['similarity']:.3f}: {r['text']}")
```

## Installation

```bash
pip3 install sentence-transformers numpy --break-system-packages
```

## Auto-indexing

All skills auto-index their output:
1. **DealFlowTracker** → index deals as "company" entities
2. **TrendMonitor** → index trends as "trend" entities  
3. **JobScout** → index jobs as "job" entities
4. **EduBootcampScout** → index programs as "program" entities

## Performance

- **Query time**: < 100ms for 10K vectors
- **Storage**: ~50MB per 10K vectors
- **Memory**: ~200MB for model
