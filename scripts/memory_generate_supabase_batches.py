#!/usr/bin/env python3
from __future__ import annotations

import json
import uuid
from pathlib import Path

WORKSPACE = Path('/opt/openclaw-stack/workspace')
DOCS_FILE = WORKSPACE / 'state' / 'memory-pipeline' / 'documents.ndjson'
EMB_FILE = WORKSPACE / 'state' / 'memory-pipeline' / 'embeddings.ndjson'
OUT_DIR = WORKSPACE / 'state' / 'memory-pipeline' / 'import-batches-v2'
MAX_CHARS = 18000


def q(val: str) -> str:
    return "'" + val.replace("'", "''") + "'"


def jsonb(val) -> str:
    return q(json.dumps(val, ensure_ascii=False)) + '::jsonb'


def text_array(values: list[str]) -> str:
    if not values:
        return "'{}'::text[]"
    return 'ARRAY[' + ', '.join(q(v) for v in values) + ']'


def vector_literal(values: list[float]) -> str:
    return q('[' + ','.join(f'{x:.8f}' for x in values) + ']')


def doc_upsert_sql(doc_id: str, doc: dict) -> str:
    return (
        'insert into public.memory_documents '
        '(id, source_path, source_type, title, project, topic, tags, content_hash, sensitivity, status, metadata, last_indexed_at) values '
        f'({q(doc_id)}, {q(doc["source_path"])}, {q(doc["source_type"])}, {q(doc["title"])}, '
        f'{"null" if not doc.get("project") else q(doc["project"])}, '
        f'{"null" if not doc.get("topic") else q(doc["topic"])}, '
        f'{text_array(doc.get("tags", []))}, {q(doc["content_hash"])}, {q(doc["sensitivity"])}, {q(doc["status"])}, '
        f'{jsonb(doc.get("metadata", {}))}, now()) '
        'on conflict (source_path) do update set '
        'source_type = excluded.source_type, title = excluded.title, project = excluded.project, topic = excluded.topic, '
        'tags = excluded.tags, content_hash = excluded.content_hash, sensitivity = excluded.sensitivity, status = excluded.status, '
        'metadata = excluded.metadata, last_indexed_at = now();'
    )


def chunk_insert_sql(doc_id: str, doc: dict, row: dict) -> str:
    chunk_id = str(uuid.uuid5(uuid.NAMESPACE_URL, f'openclaw-chunk:{doc["source_path"]}:{row["chunk_index"]}:{doc["content_hash"][:12]}'))
    return (
        'insert into public.memory_chunks '
        '(id, document_id, chunk_index, chunk_text, token_count, embedding_model, embedding, metadata) values '
        f'({q(chunk_id)}, {q(doc_id)}, {row["chunk_index"]}, {q(row["chunk_text"])}, '
        f'{int(row.get("token_count") or 0)}, {q("nomic-embed-text")}, {vector_literal(row["embedding"])}::vector, {jsonb(row.get("metadata", {}))});'
    )


def flush(batch_lines: list[str], idx: int) -> None:
    p = OUT_DIR / f'batch_{idx:02d}.sql'
    p.write_text('begin;\n' + '\n'.join(batch_lines) + '\ncommit;\n', encoding='utf-8')


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for p in OUT_DIR.glob('batch_*.sql'):
        p.unlink()
    docs = [json.loads(line) for line in DOCS_FILE.read_text(encoding='utf-8').splitlines() if line.strip()]
    chunks = [json.loads(line) for line in EMB_FILE.read_text(encoding='utf-8').splitlines() if line.strip()]
    by_path: dict[str, list[dict]] = {}
    for row in chunks:
        by_path.setdefault(row['source_path'], []).append(row)
    batch_lines=[]
    batch_len=0
    batch_idx=1
    for doc in docs:
        path = doc['source_path']
        doc_id = str(uuid.uuid5(uuid.NAMESPACE_URL, f'openclaw-doc:{path}'))
        prelude = [doc_upsert_sql(doc_id, doc), f'delete from public.memory_chunks where document_id = {q(doc_id)};']
        prelude_len = sum(len(x)+1 for x in prelude)
        # ensure new batch for doc prelude if needed
        if batch_lines and batch_len + prelude_len > MAX_CHARS:
            flush(batch_lines, batch_idx)
            batch_idx += 1
            batch_lines=[]
            batch_len=0
        batch_lines.extend(prelude)
        batch_len += prelude_len
        for row in sorted(by_path.get(path, []), key=lambda r: r['chunk_index']):
            stmt = chunk_insert_sql(doc_id, doc, row)
            stmt_len = len(stmt)+1
            if batch_lines and batch_len + stmt_len > MAX_CHARS:
                flush(batch_lines, batch_idx)
                batch_idx += 1
                # continue current doc without deleting again
                batch_lines=[doc_upsert_sql(doc_id, doc)]
                batch_len=len(batch_lines[0])+1
            batch_lines.append(stmt)
            batch_len += stmt_len
    if batch_lines:
        flush(batch_lines, batch_idx)
    print('batches', len(list(OUT_DIR.glob('batch_*.sql'))))
    for p in sorted(OUT_DIR.glob('batch_*.sql')):
        print(p.name, p.stat().st_size)

if __name__ == '__main__':
    main()
