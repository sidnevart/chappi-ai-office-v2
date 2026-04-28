"""
Unified Vector Database for AI Office
SQLite + FAISS + sentence-transformers
"""

import sqlite3
import numpy as np
import faiss
import os
import pickle
import logging
from sentence_transformers import SentenceTransformer
from datetime import datetime, timedelta
from functools import lru_cache

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('vector_db')

# Config
DB_PATH = os.environ.get('VECTOR_DB_PATH', "/mnt/files/research-state/db/knowledge.db")
MODEL_NAME = 'all-MiniLM-L6-v2'
EMBEDDING_DIM = 384  # all-MiniLM-L6-v2 dimension
FAISS_INDEX_PATH = "/mnt/files/research-state/db/faiss.index"
HF_TOKEN = os.environ.get('HF_TOKEN')

# Singleton instance
_db_instance = None

def get_db():
    """Get singleton VectorDB instance"""
    global _db_instance
    if _db_instance is None:
        _db_instance = VectorDB()
    return _db_instance

class VectorDB:
    _model = None  # Class-level model (lazy loaded once)
    _index = None  # Class-level FAISS index
    
    def __init__(self, db_path=DB_PATH):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.db = sqlite3.connect(db_path, check_same_thread=False)
        self.db_path = db_path
        self._init_tables()
        self._load_or_create_faiss()
        logger.info(f"VectorDB initialized: {db_path}")
    
    @classmethod
    def _get_model(cls):
        """Lazy load model once"""
        if cls._model is None:
            logger.info(f"Loading model: {MODEL_NAME}")
            kwargs = {}
            if HF_TOKEN:
                kwargs['use_auth_token'] = HF_TOKEN
                logger.info("Using HF_TOKEN for authentication")
            cls._model = SentenceTransformer(MODEL_NAME, **kwargs)
            logger.info("Model loaded")
        return cls._model
    
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
    
    def _load_or_create_faiss(self):
        """Load existing FAISS index or create new"""
        if os.path.exists(FAISS_INDEX_PATH):
            try:
                self.__class__._index = faiss.read_index(FAISS_INDEX_PATH)
                logger.info(f"FAISS index loaded: {self._index.ntotal} vectors")
            except Exception as e:
                logger.warning(f"Failed to load FAISS index: {e}")
                self._create_faiss()
        else:
            self._create_faiss()
    
    def _create_faiss(self):
        """Create new FAISS index"""
        self.__class__._index = faiss.IndexFlatIP(EMBEDDING_DIM)  # Inner Product
        logger.info("New FAISS index created")
    
    def _save_faiss(self):
        """Save FAISS index to disk"""
        if self._index is not None:
            faiss.write_index(self._index, FAISS_INDEX_PATH)
    
    def add_fact(self, entity_type, entity_id, content, source_url, 
                 confidence, discovered_by, ttl_days=7):
        """Add fact with vector embedding to FAISS"""
        model = self._get_model()
        embedding = model.encode(content, normalize_embeddings=True)
        embedding_bytes = embedding.astype(np.float32).tobytes()
        
        # Add to SQLite
        cursor = self.db.execute("""
            INSERT INTO facts (entity_type, entity_id, content, embedding, 
                             source_url, confidence, discovered_by, ttl_days)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (entity_type, entity_id, content, embedding_bytes, 
              source_url, confidence, discovered_by, ttl_days))
        fact_id = cursor.lastrowid
        self.db.commit()
        
        # Add to FAISS
        if self._index is not None:
            self._index.add(embedding.reshape(1, -1).astype(np.float32))
            self._save_faiss()
        
        logger.info(f"Added fact: {entity_type}/{entity_id} (id={fact_id})")
        return fact_id
    
    def search(self, query, top_k=5):
        """Semantic search with FAISS"""
        model = self._get_model()
        query_vector = model.encode(query, normalize_embeddings=True)
        query_vector = query_vector.reshape(1, -1).astype(np.float32)
        
        if self._index is None or self._index.ntotal == 0:
            logger.warning("FAISS index empty, falling back to keyword search")
            return self._keyword_search(query, top_k)
        
        # FAISS search
        D, I = self._index.search(query_vector, min(top_k, self._index.ntotal))
        
        results = []
        for i in range(len(I[0])):
            if I[0][i] < 0:
                continue
            # Get fact by FAISS index position (SQLite ids are 1-based sequential)
            faiss_idx = int(I[0][i])
            cursor = self.db.execute(
                "SELECT content, entity_type, entity_id, source_url, confidence FROM facts ORDER BY id LIMIT 1 OFFSET ?",
                (faiss_idx,)
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
        """Check if fact is fresh (not expired)"""
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
        """Get user preferences for skill"""
        cursor = self.db.execute(
            "SELECT * FROM preferences WHERE skill_name = ?",
            (skill_name,)
        )
        row = cursor.fetchone()
        if row:
            return {
                'min_sources': row[1],
                'depth': row[2],
                'focus': row[3],
                'blacklist': row[4]
            }
        return {'min_sources': 2, 'depth': 'standard', 'focus': 'balanced'}
    
    def set_preferences(self, skill_name, **kwargs):
        """Set user preferences for skill"""
        self.db.execute("""
            INSERT OR REPLACE INTO preferences (skill_name, min_sources, depth, focus)
            VALUES (?, ?, ?, ?)
        """, (skill_name, kwargs.get('min_sources', 2), 
              kwargs.get('depth', 'standard'), kwargs.get('focus', 'balanced')))
        self.db.commit()

if __name__ == '__main__':
    db = get_db()
    print("✅ VectorDB initialized with FAISS")
    print(f"   DB: {DB_PATH}")
    print(f"   Model: {MODEL_NAME}")
    print(f"   FAISS: {FAISS_INDEX_PATH}")
    print(f"   Vectors: {db._index.ntotal if db._index else 0}")
