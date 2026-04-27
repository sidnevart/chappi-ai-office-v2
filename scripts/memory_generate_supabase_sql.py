#!/usr/bin/env python3
from __future__ import annotations

import json
import uuid
from pathlib import Path

WORKSPACE = Path('/opt/openclaw-stack/workspace')
DOCS_FILE = WORKSPACE / 'state' / 'memory-pipeline' / 'documents.ndjson'
EMB_FILE = WORKSPACE / 'state' / 'memory-pipeline' / 'embeddings.ndjson'
OUT_SQL = WORKSPACE / 'state' / 'memory-pipeline' / 'supabase_import.sql'
OUT_SUMMARY = WORKSPACE / 'state' / 'memory-pipeline' / 'supabase_import_summary.json'


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


def main() -> None:
    docs = [json.loads(line) for line in DOCS_FILE.read_text(encoding='utf-8').splitlines() if line.strip()]
    chunks = [json.loads(line) for line in EMB_FILE.read_text(encoding='utf-8').splitlines() if line.strip()]
    docs_by_path = {d['source_path']: d for d in docs}
    by_path: dict[str, list[dict]] = {}
    for row in chunks:
        by_path.setdefault(row['source_path'], []).append(row)

    lines = ['begin;']
    docs_written = 0
    chunks_written = 0
    for path, doc in docs_by_path.items():
        doc_id = str(uuid.uuid5(uuid.NAMESPACE_URL, f'openclaw-doc:{path}'))
        lines.append(
            'insert into public.memory_documents '
            '(id, source_path, source_type, title, project, topic, tags, content_hash, sensitivity, status, metadata, last_indexed_at) values '
            f'({q(doc_id)}, {q(path)}, {q(doc["source_type"])}, {q(doc["title"])}, '
            f'{"null" if not doc.get("project") else q(doc["project"])}, '
            f'{"null" if not doc.get("topic") else q(doc["topic"])}, '
            f'{text_array(doc.get("tags", []))}, {q(doc["content_hash"])}, {q(doc["sensitivity"])}, {q(doc["status"])}, '
            f'{jsonb(doc.get("metadata", {}))}, now()) '
            'on conflict (source_path) do update set '
            'source_type = excluded.source_type, title = excluded.title, project = excluded.project, topic = excluded.topic, '
            'tags = excluded.tags, content_hash = excluded.content_hash, sensitivity = excluded.sensitivity, status = excluded.status, '
            'metadata = excluded.metadata, last_indexed_at = now();'
        )
        lines.append(f'delete from public.memory_chunks where document_id = {q(doc_id)};')
        doc_chunks = sorted(by_path.get(path, []), key=lambda r: r['chunk_index'])
        for row in doc_chunks:
            chunk_id = str(uuid.uuid5(uuid.NAMESPACE_URL, f'openclaw-chunk:{path}:{row["chunk_index"]}:{doc["content_hash"][:12]}'))
            lines.append(
                'insert into public.memory_chunks '
                '(id, document_id, chunk_index, chunk_text, token_count, embedding_model, embedding, metadata) values '
                f'({q(chunk_id)}, {q(doc_id)}, {row["chunk_index"]}, {q(row["chunk_text"])}, '
                f'{int(row.get("token_count") or 0)}, {q("nomic-embed-text")}, {vector_literal(row["embedding"])}::vector, {jsonb(row.get("metadata", {}))});'
            )
            chunks_written += 1
        docs_written += 1
    lines.append('commit;')
    OUT_SQL.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    OUT_SUMMARY.write_text(json.dumps({'documents': docs_written, 'chunks': chunks_written, 'sql_file': str(OUT_SQL)}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'documents': docs_written, 'chunks': chunks_written}, ensure_ascii=False))


if __name__ == '__main__':
    main()
