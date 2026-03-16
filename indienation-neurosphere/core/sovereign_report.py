import json
import os
import sqlite3
from datetime import datetime

# @sector: 33 (Sovereign Reporting & Transparency)
# @authority: INDIE-Founder

class SovereignReport:
    def __init__(self):
        self.base_dir = os.path.expanduser("~/indienation-neurosphere/core")
        self.db_path = os.path.join(self.base_dir, "neuro_registry.db")
        self.market_file = os.path.join(self.base_dir, "market_registry.json")

    def generate(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM tasks WHERE status='COMPLETED'")
        total_tasks = c.fetchone()[0]
        conn.close()

        with open(self.market_file, 'r') as f:
            market = json.load(f)

        report = {
            "timestamp": str(datetime.now()),
            "founder": "INDIE-Founder",
            "system_status": "AUTONOMOUS_INTELLIGENCE_ACTIVE",
            "metrics": {
                "total_executed_cycles": total_tasks,
                "current_production_lvl": market['stalls'][0]['level'],
                "total_luv_produced": market['total_produced_luv']
            },
            "integrity_hash": open(os.path.join(self.base_dir, "genesis_manifest.hash")).read()[:64]
        }

        report_path = os.path.join(self.base_dir, f"report_{datetime.now().strftime('%Y%m%d')}.json")
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=4)
        
        return report_path

if __name__ == "__main__":
    path = SovereignReport().generate()
    print(f"✅ [S33] Sovereign Report generated: {path}")
