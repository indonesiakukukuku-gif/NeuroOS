import time

class EmergencySystem:
    def __init__(self):
        self.pool_allocation = "15%"
        self.status = "STANDBY"

    def trigger_relief(self, location, severity):
        print(f"🚨 EMERGENCY TRIGGERED at {location}")
        print(f"📦 Allocating {self.pool_allocation} Disaster Pool for relief...")
        time.sleep(2)
        print(f"✅ Distribution Synchronized for IID affected in {location}.")
        return "SUCCESS"

if __name__ == "__main__":
    relief = EmergencySystem()
    relief.trigger_relief("Digital City Sector 7", "High")
