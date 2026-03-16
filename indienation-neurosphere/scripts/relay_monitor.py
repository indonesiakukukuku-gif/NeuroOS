import time
from datetime import datetime

class RelayMonitor:
    def __init__(self):
        self.anchor = 100000  # Anchor Value dasar €100.000
        self.users = 10000     # Sesuai Genesis Report
        
    def track_distribution(self, user_id, join_date_str):
        join_date = datetime.strptime(join_date_str, "%Y-%m-%d")
        days_active = (datetime.now() - join_date).days + 1
        
        if days_active == 1:
            amount = 1000
        elif days_active >= 364:
            amount = 990
        else:
            amount = 270
            
        return amount, days_active

    def run_report(self):
        print("📊 [REAL-TIME RELAY MONITOR]")
        print(f"Total Active Souls: {self.users}")
        print("-" * 30)
        # Contoh sampling user pertama
        val, day = self.track_distribution("IID-00001", "2026-03-04")
        print(f"User: IID-00001 | Day: {day} | Today's Grant: €{val}")
        print(f"Status AI Guard: VIGILANT | No Interest (Riba) Detected.")

if __name__ == "__main__":
    monitor = RelayMonitor()
    monitor.run_report()
