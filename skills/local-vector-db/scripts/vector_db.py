"""
Unified Vector Database for AI Office
SQLite + sentence-transformers
"""

import sqlite3
import numpy as np
from sentence_transformers import SentenceTransformer
from datetime import datetime, timedelta
import os

DB_PATH = "/mnt/files/research-state/db/knowledge.db"
MODEL_NAME = 'all-MiniLM-L6-v2'

class VectorDB:
    def __init__(self, db_path=DB_PATH):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.db = sqlite3.connect(db_path)
        self.encoder = SentenceTransformer(MODEL_NAME)
        self._init_tables()
    
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
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
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
    
    def add_fact(self, entity_type, entity_id, content, source_url, 
                 confidence, discovered_by, ttl_days=7):
        """Add fact with vector embedding"""
        embedding = self.encoder.encode(content)
        embedding_bytes = embedding.tobytes()
        
        self.db.execute("""
            INSERT INTO facts (entity_type, entity_id, content, embedding, 
                             source_url, confidence, discovered_by, ttl_days)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (entity_type, entity_id, content, embedding_bytes, 
              source_url, confidence, discovered_by, ttl_days))
        self.db.commit()
    
    def search(self, query, top_k=5):
        """Semantic search by query"""
        query_vector = self.encoder.encode(query)
        
        cursor = self.db.execute(
            "SELECT content, entity_type, entity_id, source_url, confidence FROM facts"
        )
        results = []
        
        for row in cursor.fetchall():
            content, entity_type, entity_id, source_url, confidence = row
            # Simple text search for now (full vector search requires FAISS)
            if any(word.lower() in content.lower() for word in query.split()):
                results.append({
                    'content': content,
                    'entity_type': entity_type,
                    'entity_id': entity_id,
                    'source_url': source_url,
                    'confidence': confidence
                })
        
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
                'ttl_days': row[11] if len(row) > 11 else 7
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
            # If created_at is not parseable, consider it fresh
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
    db = VectorDB()
    print("✅ VectorDB initialized")
    print(f"   DB: {DB_PATH}")
    print(f"   Model: {MODEL_NAME}")
