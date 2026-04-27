#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

WORKSPACE = Path('/opt/openclaw-stack/workspace')
OUT_DIR = WORKSPACE / 'state' / 'memory-pipeline'
DOCS_OUT = OUT_DIR / 'documents.ndjson'
CHUNKS_OUT = OUT_DIR / 'chunks.ndjson'
MANIFEST_OUT = OUT_DIR / 'manifest.json'

INCLUDE_PATHS = [
    WORKSPACE / 'MEMORY.md',
    WORKSPACE / 'USER.md',
    WORKSPACE / 'IDENTITY.md',
    WORKSPACE / 'TOOLS.md',
    WORKSPACE / 'memory',
    WORKSPACE / 'docs' / 'research',
    WORKSPACE / 'docs' / 'plans',
    WORKSPACE / 'docs' / 'decisions',
]

EXCLUDE_PARTS = {
    '.git', '.dreams', 'node_modules', 'backups', '__pycache__', '_templates',
}
EXCLUDE_SUFFIXES = {'.json', '.sqlite', '.log', '.png', '.jpg', '.jpeg', '.gif', '.webp', '.zip', '.gz'}
SECRET_LIKE = ('secret', 'token', '.env', 'openclaw.json', 'gateway.env', 'grafana.env', 'credentials')


def iter_files() -> Iterable[Path]:
    for root in INCLUDE_PATHS:
        if not root.exists():
            continue
        if root.is_file():
            yield root
            continue
        for path in root.rglob('*'):
            if not path.is_file():
                continue
            rel_parts = set(path.relative_to(WORKSPACE).parts)
            if rel_parts & EXCLUDE_PARTS:
                continue
            if path.suffix.lower() in EXCLUDE_SUFFIXES:
                continue
            lowered = str(path).lower()
            if any(flag in lowered for flag in SECRET_LIKE):
                continue
            yield path


def source_type(path: Path) -> str:
    rel = path.relative_to(WORKSPACE)
    if rel.name == 'MEMORY.md':
        return 'memory'
    if rel.parts[:1] == ('memory',):
        return 'daily_note'
    if rel.parts[:2] == ('docs', 'research'):
        return 'research'
    if rel.parts[:2] == ('docs', 'plans'):
        return 'plan'
    if rel.parts[:2] == ('docs', 'decisions'):
        return 'decision'
    if rel.name in {'USER.md', 'IDENTITY.md'}:
        return 'profile'
    if rel.name == 'TOOLS.md':
        return 'tools'
    return 'other'


def title_from_text(path: Path, text: str) -> str:
    for line in text.splitlines():
        m = re.match(r'^#\s+(.+?)\s*$', line.strip())
        if m:
            return m.group(1)
    return path.stem.replace('-', ' ').replace('_', ' ')


def guess_topic(path: Path) -> str | None:
    rel = path.relative_to(WORKSPACE)
    if len(rel.parts) >= 3 and rel.parts[0] == 'docs' and rel.parts[1] in {'research', 'decisions'}:
        return rel.parts[2] if rel.parts[2] != rel.name else None
    return None


def chunk_text(text: str, target_words: int = 220, overlap_paragraphs: int = 1) -> list[str]:
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    if not paragraphs:
        return []
    chunks: list[str] = []
    buf: list[str] = []
    words = 0
    for para in paragraphs:
        para_words = len(para.split())
        if buf and words + para_words > target_words:
            chunks.append('\n\n'.join(buf))
            tail = buf[-overlap_paragraphs:] if overlap_paragraphs else []
            buf = tail + [para]
            words = sum(len(x.split()) for x in buf)
        else:
            buf.append(para)
            words += para_words
    if buf:
        chunks.append('\n\n'.join(buf))
    return chunks


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    docs_count = 0
    chunks_count = 0
    with DOCS_OUT.open('w', encoding='utf-8') as docs_f, CHUNKS_OUT.open('w', encoding='utf-8') as chunks_f:
        for path in sorted(set(iter_files())):
            text = path.read_text(encoding='utf-8', errors='ignore').strip()
            if not text:
                continue
            rel = path.relative_to(WORKSPACE).as_posix()
            digest = hashlib.sha256(text.encode('utf-8')).hexdigest()
            doc = {
                'source_path': rel,
                'source_type': source_type(path),
                'title': title_from_text(path, text),
                'project': None,
                'topic': guess_topic(path),
                'tags': [],
                'content_hash': digest,
                'sensitivity': 'normal',
                'status': 'active',
                'metadata': {
                    'workspace': str(WORKSPACE),
                    'mtime': datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).isoformat(),
                },
            }
            docs_f.write(json.dumps(doc, ensure_ascii=False) + '\n')
            docs_count += 1
            for idx, chunk in enumerate(chunk_text(text)):
                row = {
                    'source_path': rel,
                    'chunk_index': idx,
                    'chunk_text': chunk,
                    'token_count': max(1, round(len(chunk.split()) * 1.3)),
                    'metadata': {
                        'title': doc['title'],
                        'source_type': doc['source_type'],
                        'topic': doc['topic'],
                    },
                }
                chunks_f.write(json.dumps(row, ensure_ascii=False) + '\n')
                chunks_count += 1
    MANIFEST_OUT.write_text(json.dumps({
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'documents': docs_count,
        'chunks': chunks_count,
        'documents_file': str(DOCS_OUT),
        'chunks_file': str(CHUNKS_OUT),
    }, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'documents': docs_count, 'chunks': chunks_count}, ensure_ascii=False))


if __name__ == '__main__':
    main()
