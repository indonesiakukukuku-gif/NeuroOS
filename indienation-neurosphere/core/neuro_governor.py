import sqlite3
import json
import os
import time
import subprocess

# @authority: IID-021+ (INDIE-Founder)
# @sector: 00 (Autonomous Core)

DB_PATH = os.path.expanduser("~/indienation-neurosphere/core/neuro_registry.db")
MARKET_FILE = os.path.expanduser("~/indienation-neurosphere/core/market_registry.json")

def get_state():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM tasks WHERE command LIKE 'S03_%' AND status='COMPLETED'")
    days = c.fetchone()[0]
    
    c.execute("SELECT COUNT(*) FROM tasks WHERE command='S17_INVEST_UPGRADE'")
    upgrades = c.fetchone()[0]
    conn.close()
    
    with open(MARKET_FILE, 'r') as f:
        market = json.load(f)
    
    balance = 1000 + (days-1)*270 - (upgrades*500) if days > 0 else 0
    return {"days": days, "balance": balance, "market": market}

def decide_next_action(state):
    # LOGIKA ADAPTIF (Hybrid Scoring)
    # 1. Prioritas Distribusi Harian
    if state["days"] < 364:
        return "EXECUTE_DAY"
    
    # 2. Prioritas Re-investasi (Jika saldo > 1500 dan level masih rendah)
    if state["balance"] > 1500 and state["market"]["stalls"][0]["level"] < 10:
        return "AUTO_UPGRADE"
    
    return "IDLE"

def run_cycle():
    print("🤖 [INDIE-AI] Analyzing State...")
    state = get_state()
    action = decide_next_action(state)
    
    if action == "EXECUTE_DAY":
        next_day = state["days"] + 1
        print(f"🚀 [S03] Autonomously Executing Day {next_day}")
        subprocess.run(["sqlite3", DB_PATH, f"INSERT INTO tasks (command, sector_id, status, created_at) VALUES ('S03_RELAY_DAY_{next_day}', 3, 'PENDING', '{time.ctime()}');"])
        subprocess.run(["python3", os.path.expanduser("~/indienation-neurosphere/core/argi_worker.py")])
        
    elif action == "AUTO_UPGRADE":
        print("📈 [S17] Balance High. Executing Autonomous Upgrade.")
        subprocess.run(["python3", os.path.expanduser("~/indienation-neurosphere/core/market_upgrade.py")])

if __name__ == "__main__":
    while True:
        run_cycle()
        print("💤 [INDIE-AI] Sleeping for 60s (Autonomous Loop Active)...")
        time.sleep(60)
