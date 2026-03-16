import sqlite3
import datetime
import os
import sys

sys.path.append(os.path.expanduser("~/indienation-neurosphere/core"))
from ghost_vault import encrypt_data
import micro_market

DB_PATH = os.path.expanduser("~/indienation-neurosphere/core/neuro_registry.db")
LOG_FILE = os.path.expanduser("~/indienation-neurosphere/core/sovereign_audit.log")

def get_relay_amount(conn):
    c = conn.cursor()
    # Hitung jumlah task 'S03_DISTRIBUTION' yang sudah COMPLETED
    c.execute("SELECT COUNT(*) FROM tasks WHERE command LIKE 'S03_%' AND status='COMPLETED'")
    count = c.fetchone()[0]
    
    if count == 0:
        return 1000, "Hari ke-1 (Kick-off)"
    elif count < 364:
        return 270, f"Hari ke-{count + 1}"
    else:
        return 990, "Hari Terakhir (Final Relay)"

def process_tasks():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, command FROM tasks WHERE status='PENDING'")
    tasks = c.fetchall()
    
    if not tasks:
        return

    for task_id, cmd in tasks:
        ts_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Penentuan Nilai Otomatis Berdasarkan Estafet
        amount, label = get_relay_amount(conn)
        
        secret_msg = f"RELAY_STATUS: {label} | AMOUNT: €{amount} | TARGET: IID-021+"
        secure_ref = encrypt_data(secret_msg)
        
        c.execute("UPDATE sectors SET last_sync=? WHERE id IN (1,3,25,33)", (ts_now,))
        c.execute("UPDATE tasks SET status='COMPLETED', completed_at=? WHERE id=?", (ts_now, task_id))
        
        with open(LOG_FILE, "a") as f:
            f.write(f"[{ts_now}] ACTION: {cmd} | S03_DIST_REF: {secure_ref} | STATUS: SUCCESS\n")
        
        print(f"✅ {label} Berhasil Diproses (€{amount}).")
        micro_market.init_market()
        luv_yield = micro_market.produce_luv()
        print(f"📦 [S17] Production: +{luv_yield} LUV accumulated.")
        generate_sovereign_report(conn)
            
    conn.commit()
    conn.close()

if __name__ == "__main__":
    process_tasks()

def generate_sovereign_report(conn):
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM tasks WHERE command LIKE 'S03_%' AND status='COMPLETED'")
    days = c.fetchone()[0]
    
    if days % 7 == 0 and days > 0:
        with open(os.path.expanduser("~/indienation-neurosphere/core/sovereign_audit.log"), "a") as f:
            f.write(f"\n[📊 WEEKLY REPORT - DAY {days}]\n")
            f.write(f"Sovereignty Progress: {days}/364 days\n")
            f.write(f"Production Efficiency: Active\n")
            f.write("------------------------------------------\n")
