import sqlite3
import os

DB_PATH = os.path.expanduser("~/indienation-neurosphere/core/neuro_registry.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Tabel Sektor
    c.execute('''CREATE TABLE IF NOT EXISTS sectors 
                 (id INTEGER PRIMARY KEY, name TEXT, status TEXT, 
                  last_sync TEXT, checksum TEXT, error_flag INTEGER)''')
    # Tabel Task Queue (Antrean Tugas ARGI)
    c.execute('''CREATE TABLE IF NOT EXISTS tasks 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, command TEXT, 
                  sector_id INTEGER, status TEXT, created_at TEXT, completed_at TEXT)''')
    
    sectors = [
        (1, 'Investment', 'ACTIVE', '', 'hash_v1', 0),
        (6, 'Pariwisata', 'ACTIVE', '', 'hash_v1', 0),
        (17, 'UMKM & Ekspor', 'ACTIVE', '', 'hash_v1', 0),
        (21, 'Teknologi & Inovasi', 'ACTIVE', '', 'hash_v1', 0),
        (25, 'Keuangan', 'ACTIVE', '', 'hash_v1', 0),
        (29, 'Keamanan', 'ACTIVE', '', 'hash_v1', 0),
        (33, 'Identity', 'LOCKED', '', 'hash_v1', 0)
    ]
    c.executemany('INSERT OR REPLACE INTO sectors VALUES (?,?,?,?,?,?)', sectors)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("✅ [REGISTRY] Database & Task Queue Initialized.")
