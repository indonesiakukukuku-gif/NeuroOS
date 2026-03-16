import json
import os

# @authority: IID-021+
# @sector: 17 (UMKM & Ekspor)

MARKET_FILE = os.path.expanduser("~/indienation-neurosphere/core/market_registry.json")

def init_market():
    if not os.path.exists(MARKET_FILE):
        data = {
            "stalls": [
                {"id": 1, "name": "Digital Souvenir S06", "level": 1, "cost_to_upgrade": 500, "production_rate": 2}
            ],
            "total_produced_luv": 0
        }
        with open(MARKET_FILE, "w") as f:
            json.dump(data, f, indent=4)

def produce_luv():
    if os.path.exists(MARKET_FILE):
        with open(MARKET_FILE, "r") as f:
            data = json.load(f)
        
        # Hitung produksi berdasarkan level stall
        daily_yield = sum(stall['production_rate'] * stall['level'] for stall in data['stalls'])
        data['total_produced_luv'] += daily_yield
        
        with open(MARKET_FILE, "w") as f:
            json.dump(data, f, indent=4)
        return daily_yield
    return 0

if __name__ == "__main__":
    init_market()
    yield_amount = produce_luv()
    print(f"📦 [S17] Market Cycle: Produced {yield_amount} LUV from your Digital Stalls.")
