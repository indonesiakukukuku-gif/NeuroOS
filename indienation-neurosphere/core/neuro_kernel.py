import time
import json
import os
import sqlite3
import traceback
import subprocess
from datetime import datetime

class SovereignArbiter:
    def __init__(self):
        self.base_dir = os.path.expanduser("~/indienation-neurosphere/core")
        self.paths = {
            "db": os.path.join(self.base_dir, "neuro_registry.db"),
            "market": os.path.join(self.base_dir, "market_registry.json"),
            "memory": os.path.join(self.base_dir, "kernel_memory.json"),
            "manifest": os.path.join(self.base_dir, "baseline_manifest.hash"),
            "log": os.path.join(self.base_dir, "kernel_error.log"),
            "pid": os.path.join(self.base_dir, "kernel.pid")
        }
        self.min_safety_reserve = 2500
        self.load_memory()
        self.save_pid()

    def save_pid(self):
        """Menyimpan PID untuk shutdown deterministik."""
        with open(self.paths["pid"], "w") as f:
            f.write(str(os.getpid()))

    def load_memory(self):
        default = {"fails": 0, "budget_count": 0, "last_reset_day": 0}
        if os.path.exists(self.paths["memory"]):
            try:
                with open(self.paths["memory"], 'r') as f:
                    self.memory = json.load(f)
            except: self.memory = default
        else: self.memory = default

    def safe_save_json(self, data, path):
        temp_path = path + ".tmp"
        with open(temp_path, 'w') as f:
            json.dump(data, f, indent=4)
        os.replace(temp_path, path)

    def check_integrity(self):
        """True Integrity: Verifikasi terhadap baseline (sha256sum -c)."""
        if not os.path.exists(self.paths["manifest"]):
            return True # Inisialisasi awal
        
        try:
            # Memeriksa integritas file di folder core
            result = subprocess.run(
                ["sha256sum", "-c", "--status", self.paths["manifest"]],
                cwd=self.base_dir,
                capture_output=True
            )
            return result.returncode == 0
        except:
            return False

    def sense_state(self):
        try:
            conn = sqlite3.connect(self.paths["db"])
            c = conn.cursor()
            c.execute("SELECT COUNT(*) FROM tasks WHERE command LIKE 'S03_RELAY_DAY_%' AND status='COMPLETED'")
            days_done = c.fetchone()[0]
            c.execute("SELECT COUNT(*) FROM tasks WHERE command='S17_INVEST_UPGRADE'")
            upgrades = c.fetchone()[0]
            conn.close()
            with open(self.paths["market"], 'r') as f:
                market = json.load(f)
            balance = 1000 + (days_done-1)*270 - (upgrades*500) if days_done > 0 else 0
            return {"days": days_done, "balance": balance, "market": market}
        except: return None

    def pulse(self):
        while True:
            try:
                # 1. INTEGRITY CHECK (GATEKEEPER)
                if not self.check_integrity():
                    print(f"🚨 [BREACH] {datetime.now()} | Integrity Failure. Lockdown Engaged.", flush=True)
                    # Hapus PID agar tidak dianggap aktif
                    if os.path.exists(self.paths["pid"]): os.remove(self.paths["pid"])
                    break

                state = self.sense_state()
                if not state: 
                    time.sleep(10); continue

                # 2. ARBITRATION
                days_left = 364 - state["days"]
                roi = (days_left * 2) / 500
                
                if state["balance"] < self.min_safety_reserve:
                    decision = "SECTOR_03_PRIORITY"
                elif roi > 1.5 and self.memory.get("budget_count", 0) < 3:
                    decision = "SECTOR_17_PRIORITY"
                else:
                    decision = "SECTOR_03_PRIORITY"

                print(f"💓 Arbiter OK | Day {state['days']} | Bal €{state['balance']} | Priority: {decision}", flush=True)

                # 3. MODULAR EXECUTION
                if decision == "SECTOR_17_PRIORITY":
                    os.system("python3 ~/indienation-neurosphere/core/market_upgrade.py")
                    self.memory["budget_count"] = self.memory.get("budget_count", 0) + 1
                else:
                    os.system("python3 ~/indienation-neurosphere/core/argi_worker.py")

                self.safe_save_json(self.memory, self.paths["memory"])
                os.system(f"python3 {self.base_dir}/sovereign_report.py")
                
            except Exception as e:
                with open(self.paths["log"], "a") as f:
                    f.write(f"[{datetime.now()}] {traceback.format_exc()}\n")
            
            time.sleep(60)

if __name__ == "__main__":
    SovereignArbiter().pulse()
