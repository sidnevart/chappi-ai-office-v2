"""
Vector Database for AI Office
SQLite + FAISS + sentence-transformers

CRITICAL: NO SINGLETON. Each session creates its own connection.
SQLite handles concurrency. FAISS index loaded from disk.
"""

import sqlite3
import numpy as np
import faiss
import os
import logging
from sentence_transformers import SentenceTransformer
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('vector_db')

DB_PATH = os.environ.get('VECTOR_DB_PATH', "/mnt/files/research-state/db/knowledge.db")
MODEL_NAME = 'all-MiniLM-L6-v2'
EMBEDDING_DIM = 384
FAISS_INDEX_PATH = "/mnt/files/research-state/db/faiss.index"

# Lazy model cache (per-process, not singleton)
_model = None

def get_model():
    """Get model (lazy load, cached per process)"""
    global _model
    if _model is None:
        logger.info(f"Loading model: {MODEL_NAME}")
        kwargs = {}
        if os.environ.get('HF_TOKEN'):
            kwargs['use_auth_token'] = os.environ['HF_TOKEN']
        _model = SentenceTransformer(MODEL_NAME, **kwargs)
        logger.info("Model loaded")
    return _model

class VectorDB:
    """Vector database - create new instance per session"""
    
    def __init__(self, db_path=DB_PATH):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.db = sqlite3.connect(db_path, check_same_thread=False)
        self.db_path = db_path
        self._init_tables()
        self._load_faiss()
    
    def _init_tables(self):
        """Create tables if not exist"""
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS facts (
                id INTEGER PRIMARY KEY,
                entity_type TEXT,
                entity_id TEXT,
                content TEXT,
                embedding BLOB,
                source_url TEXT,
                confidence TEXT,
                discovered_by TEXT,
                used_by TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                ttl_days INTEGER DEFAULT 7
            )
        """)
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY,
                skill_name TEXT,
                report_path TEXT,
                reaction TEXT,
                comment TEXT,
                adjustments TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS preferences (
                skill_name TEXT PRIMARY KEY,
                min_sources INTEGER DEFAULT 2,
                depth TEXT DEFAULT 'standard',
                focus TEXT DEFAULT 'balanced',
                blacklist TEXT
            )
        """)
        self.db.commit()
    
    def _load_faiss(self):
        """Load or create FAISS index"""
        if os.path.exists(FAISS_INDEX_PATH):
            self.index = faiss.read_index(FAISS_INDEX_PATH)
            logger.info(f"FAISS loaded: {self.index.ntotal} vectors")
        else:
            self.index = faiss.IndexFlatIP(EMBEDDING_DIM)
            logger.info("New FAISS index created")
    
    def _save_faiss(self):
        """Save FAISS index to disk"""
        if self.index:
            faiss.write_index(self.index, FAISS_INDEX_PATH)
    
    def add_fact(self, entity_type, entity_id, content, source_url, 
                 confidence, discovered_by, ttl_days=7):
        """Add fact with vector embedding"""
        model = get_model()
        embedding = model.encode(content, normalize_embeddings=True)
        embedding_bytes = embedding.astype(np.float32).tobytes()
        
        cursor = self.db.execute("""
            INSERT INTO facts (entity_type, entity_id, content, embedding, 
                             source_url, confidence, discovered_by, ttl_days)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (entity_type, entity_id, content, embedding_bytes, 
              source_url, confidence, discovered_by, ttl_days))
        self.db.commit()
        
        # Add to FAISS
        self.index.add(embedding.reshape(1, -1).astype(np.float32))
        self._save_faiss()
        
        logger.info(f"Added: {entity_type}/{entity_id}")
        return cursor.lastrowid
    
    def search(self, query, top_k=5):
        """Semantic search with FAISS"""
        model = get_model()
        query_vector = model.encode(query, normalize_embeddings=True)
        query_vector = query_vector.reshape(1, -1).astype(np.float32)
        
        if self.index.ntotal == 0:
            return self._keyword_search(query, top_k)
        
        D, I = self.index.search(query_vector, min(top_k, self.index.ntotal))
        
        results = []
        for i in range(len(I[0])):
            if I[0][i] < 0:
                continue
            cursor = self.db.execute(
                "SELECT content, entity_type, entity_id, source_url, confidence FROM facts ORDER BY id LIMIT 1 OFFSET ?",
                (int(I[0][i]),)
            )
            row = cursor.fetchone()
            if row:
                results.append({
                    'content': row[0],
                    'entity_type': row[1],
                    'entity_id': row[2],
                    'source_url': row[3],
                    'confidence': row[4],
                    'score': float(D[0][i])
                })
        
        return results
    
    def _keyword_search(self, query, top_k=5):
        """Fallback keyword search"""
        keywords = query.lower().split()
        cursor = self.db.execute(
            "SELECT content, entity_type, entity_id, source_url, confidence FROM facts"
        )
        results = []
        for row in cursor.fetchall():
            content = row[0].lower()
            score = sum(1 for kw in keywords if kw in content) / len(keywords)
            if score > 0:
                results.append({
                    'content': row[0],
                    'entity_type': row[1],
                    'entity_id': row[2],
                    'source_url': row[3],
                    'confidence': row[4],
                    'score': score
                })
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:top_k]
    
    def get_fact(self, entity_type, entity_id):
        """Get fact by entity"""
        cursor = self.db.execute(
            "SELECT * FROM facts WHERE entity_type = ? AND entity_id = ? ORDER BY created_at DESC LIMIT 1",
            (entity_type, entity_id)
        )
        row = cursor.fetchone()
        if row:
            return {
                'id': row[0],
                'entity_type': row[1],
                'entity_id': row[2],
                'content': row[3],
                'source_url': row[5],
                'confidence': row[6],
                'discovered_by': row[7],
                'created_at': row[9],
                'ttl_days': row[10] if len(row) > 10 else 7
            }
        return None
    
    def is_fresh(self, entity_type, entity_id):
        """Check if fact is fresh"""
        fact = self.get_fact(entity_type, entity_id)
        if not fact:
            return False
        try:
            age = datetime.now() - datetime.fromisoformat(fact['created_at'].replace('Z', '+00:00'))
            return age.days < fact['ttl_days']
        except:
            return True
    
    def add_feedback(self, skill_name, report_path, reaction, comment=None):
        """Add user feedback"""
        self.db.execute("""
            INSERT INTO feedback (skill_name, report_path, reaction, comment)
            VALUES (?, ?, ?, ?)
        """, (skill_name, report_path, reaction, comment))
        self.db.commit()
    
    def get_preferences(self, skill_name):
        """Get user preferences"""
        cursor = self.db.execute(
            "SELECT * FROM preferences WHERE skill_name = ?", (skill_name,)
        )
        row = cursor.fetchone()
        if row:
            return {'min_sources': row[1], 'depth': row[2], 'focus': row[3], 'blacklist': row[4]}
        return {'min_sources': 2, 'depth': 'standard', 'focus': 'balanced'}

if __name__ == '__main__':
    db = VectorDB()
    print(f"VectorDB: {db.index.ntotal} vectors")
