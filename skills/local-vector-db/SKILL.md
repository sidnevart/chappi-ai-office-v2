---
name: local-vector-db
description: |
  ЕДИНСТВЕННАЯ система хранения знаний.
  SQLite + sentence-transformers для семантического поиска.
  Хранит: entities, facts, feedback, session state.
  Replaces: MEM0, Supabase, knowledge.json, state.json, feedback.json
---

# Local Vector Database

## Overview

**ЕДИНСТВЕННАЯ** база знаний системы.
Всё хранится здесь — никаких дублирующих JSON файлов.

## Architecture

```
vector_db/
├── knowledge.db          # SQLite
│   ├── entities          # Companies, programs, jobs
│   ├── facts             # Research findings with embeddings
│   ├── feedback          # User reactions and preferences
│   ├── sessions          # Session state
│   └── vectors           # Vector embeddings (FAISS)
└── embeddings/           # Cached sentence embeddings
```

## Schema

### Table: facts (основная таблица знаний)
```sql
CREATE TABLE facts (
    id INTEGER PRIMARY KEY,
    entity_type TEXT,      -- 'company', 'trend', 'job', 'idea'
    entity_id TEXT,        -- 'otter.ai', 'ai-meeting'
    content TEXT,          -- текст с данными
    embedding BLOB,        -- векторное представление
    source_url TEXT,       -- источник
    confidence TEXT,       -- High/Medium/Low
    discovered_by TEXT,    -- какой скилл нашёл
    used_by TEXT,         -- какие скиллы использовали
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    ttl_days INTEGER       -- время жизни
);
```

### Table: feedback (обратная связь)
```sql
CREATE TABLE feedback (
    id INTEGER PRIMARY KEY,
    skill_name TEXT,
    report_path TEXT,
    reaction TEXT,         -- 👍, 👎, ❤️, 🤔, 🗑️
    comment TEXT,
    adjustments TEXT,      -- JSON с изменениями
    created_at TIMESTAMP
);
```

### Table: preferences (предпочтения пользователя)
```sql
CREATE TABLE preferences (
    skill_name TEXT PRIMARY KEY,
    min_sources INTEGER DEFAULT 2,
    depth TEXT DEFAULT 'standard',
    focus TEXT DEFAULT 'balanced',
    blacklist TEXT         -- JSON array
);
```

## API

```python
class VectorDB:
    def __init__(self, db_path="/mnt/files/research-state/db/knowledge.db"):
        self.db = sqlite3.connect(db_path)
        self.encoder = SentenceTransformer('all-MiniLM-L6-v2')
        self._init_tables()
    
    def add_fact(self, entity_type, entity_id, content, source_url, confidence, discovered_by, ttl_days=7):
        """Добавить факт с эмбеддингом"""
        embedding = self.encoder.encode(content)
        self.db.execute("""
            INSERT INTO facts (entity_type, entity_id, content, embedding, source_url, confidence, discovered_by, ttl_days)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (entity_type, entity_id, content, embedding.tobytes(), source_url, confidence, discovered_by, ttl_days))
        self.db.commit()
    
    def search(self, query, top_k=5):
        """Семантический поиск"""
        query_vector = self.encoder.encode(query)
        # ... поиск по косинусному сходству
        return results
    
    def get_fact(self, entity_type, entity_id):
        """Получить факт по ID"""
        cursor = self.db.execute(
            "SELECT * FROM facts WHERE entity_type = ? AND entity_id = ?",
            (entity_type, entity_id)
        )
        return cursor.fetchone()
    
    def is_fresh(self, entity_type, entity_id):
        """Проверить не устарел ли факт"""
        fact = self.get_fact(entity_type, entity_id)
        if not fact:
            return False
        age = (datetime.now() - fact['updated_at']).days
        return age < fact['ttl_days']
```

## Usage in Skills

### Before Research — Check Vector DB
```python
# В trend-monitor
def run():
    db = VectorDB()
    
    # Проверить, знаем ли мы уже этот тренд
    if db.is_fresh('trend', 'ai-meeting-assistants'):
        return db.search('AI meeting assistants market 2026')
    
    # Иначе — research
    data = web_search('AI meeting assistants market 2026')
    db.add_fact('trend', 'ai-meeting-assistants', data, 'https://...', 'High', 'trend-monitor')
    return data
```

### Cross-Domain Learning
```python
# В idea-generator
def generate_idea(trend):
    db = VectorDB()
    
    # Найти связанные факты
    related = db.search(f'startup ideas {trend}')
    
    # Использовать для генерации
    return generate_with_context(related)
```

### Feedback Storage
```python
# В telegram-reporter
def send_report(report, skill_name):
    # Отправить в Telegram...
    
    # Сохранить для feedback
    db = VectorDB()
    db.add_feedback(skill_name, report, reaction=None)
```

## Integration

**КАЖДЫЙ скилл ДОЛЖЕН:**
1. Проверять Vector DB перед research
2. Сохранять findings в Vector DB
3. Искать связанные факты

**НИКОГДА не использовать:**
- ❌ knowledge.json
- ❌ state.json  
- ❌ feedback.json
- ❌ Любые другие JSON для знаний

## Best Practices

- ✅ Единая точка входа — VectorDB
- ✅ Все данные с эмбеддингами
- ✅ TTL для устаревания
- ✅ Семантический поиск
- ❌ Никаких дублирующих систем
