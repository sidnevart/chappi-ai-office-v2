#!/usr/bin/env python3
from __future__ import annotations

import json
import urllib.request
from pathlib import Path

WORKSPACE = Path('/opt/openclaw-stack/workspace')
IN_FILE = WORKSPACE / 'state' / 'memory-pipeline' / 'chunks.ndjson'
OUT_FILE = WORKSPACE / 'state' / 'memory-pipeline' / 'embeddings.ndjson'
MANIFEST = WORKSPACE / 'state' / 'memory-pipeline' / 'embedding-manifest.json'
OLLAMA_URL = 'http://127.0.0.1:11434/api/embed'
MODEL = 'nomic-embed-text'
BATCH = 16


def post_embed(texts: list[str]) -> list[list[float]]:
    payload = json.dumps({'model': MODEL, 'input': texts}).encode('utf-8')
    req = urllib.request.Request(OLLAMA_URL, data=payload, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    embeddings = data.get('embeddings') or []
    if len(embeddings) != len(texts):
        raise RuntimeError(f'Expected {len(texts)} embeddings, got {len(embeddings)}')
    return embeddings


def main() -> None:
    rows = [json.loads(line) for line in IN_FILE.read_text(encoding='utf-8').splitlines() if line.strip()]
    total = 0
    dim = None
    with OUT_FILE.open('w', encoding='utf-8') as out:
        for i in range(0, len(rows), BATCH):
            batch = rows[i:i+BATCH]
            embeddings = post_embed([r['chunk_text'] for r in batch])
            for row, emb in zip(batch, embeddings):
                dim = dim or len(emb)
                row['embedding'] = emb
                out.write(json.dumps(row, ensure_ascii=False) + '\n')
                total += 1
    MANIFEST.write_text(json.dumps({'model': MODEL, 'rows': total, 'dimensions': dim}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'rows': total, 'dimensions': dim}, ensure_ascii=False))


if __name__ == '__main__':
    main()
