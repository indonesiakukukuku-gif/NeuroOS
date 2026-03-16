import json
import os

# @authority: IID-021+
# @sector: 21 (Teknologi & Optimasi)

MARKET_FILE = os.path.expanduser("~/indienation-neurosphere/core/market_registry.json")

def check_optimization():
    if os.path.exists(MARKET_FILE):
        with open(MARKET_FILE, "r") as f:
            data = json.load(f)
        
        stall = data['stalls'][0]
        if stall['level'] >= 5:
            # Neural Link memberikan diskon 10% untuk biaya upgrade berikutnya
            current_cost = stall['cost_to_upgrade']
            optimized_cost = int(current_cost * 0.9)
            print(f"🧠 [S21] Neural Link Active: Optimization applied. Next upgrade: €{optimized_cost}")
            return True
    return False

if __name__ == "__main__":
    check_optimization()
