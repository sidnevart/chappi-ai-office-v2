# Supabase memory backend

Этот каталог содержит schema и локальные artifacts для memory backend.

## Что уже готово
- `migrations/001_memory_schema.sql` — базовая schema для `memory_documents`, `memory_chunks`, `memory_facts`, `ingestion_runs`
- `state/memory-pipeline/documents.ndjson` — нормализованные документы
- `state/memory-pipeline/chunks.ndjson` — чанки корпуса
- `state/memory-pipeline/embeddings.ndjson` — чанки с embeddings
- `state/memory-pipeline/supabase_import.sql` — готовый SQL import для Supabase

## Локальный pipeline
1. `python3 scripts/memory_prepare_corpus.py`
2. `python3 scripts/memory_embed_ollama.py`
3. `python3 scripts/memory_generate_supabase_sql.py`

## Важно
Текущий подключённый Supabase project был в статусе `INACTIVE`, поэтому remote apply schema/SQL пока не выполнен.
Когда проект станет ACTIVE, можно:
- применить `migrations/001_memory_schema.sql`
- затем применить `state/memory-pipeline/supabase_import.sql`
- затем проверить retrieval запросами к `public.match_memory_chunks(...)`
