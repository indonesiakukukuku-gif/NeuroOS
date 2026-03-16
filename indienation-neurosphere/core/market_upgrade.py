import json
import os
import sqlite3
from datetime import datetime

# @sector: 17 (Market & Production)
# @authority: INDIE-Founder

DB_PATH = os.path.expanduser("~/indienation-neurosphere/core/neuro_registry.db")
MARKET_FILE = os.path.expanduser("~/indienation-neurosphere/core/market_registry.json")

def upgrade():
    if not os.path.exists(MARKET_FILE):
        print("❌ [S17] Market Registry not found.")
        return

    with open(MARKET_FILE, 'r') as f:
        data = json.load(f)

    # Biaya upgrade statis 500 TM sesuai dashboard
    cost = 500
    current_level = data['stalls'][0]['level']
    
    # Logika upgrade
    data['stalls'][0]['level'] += 1
    data['stalls'][0]['production_rate'] += 2 # Tambah +2 LUV per hari
    
    # Simpan ke Registry
    with open(MARKET_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    
    # Catat transaksi ke Database untuk audit S25
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO tasks (command, sector_id, status, created_at) VALUES ('S17_INVEST_UPGRADE', 17, 'COMPLETED', ?)", (str(datetime.now()),))
    conn.commit()
    conn.close()

    print(f"✅ [S17] Upgrade Successful! Level: {current_level} -> {data['stalls'][0]['level']}")

if __name__ == "__main__":
    upgrade()
