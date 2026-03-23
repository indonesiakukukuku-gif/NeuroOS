import json
import os

def get_luv_treasury():
    # Simulasi data distribusi LUV
    total_supply = 100_000_000_000_000  # 100 Triliun
    founder_allocation = total_supply * 0.20 # 20%
    disaster_pool = total_supply * 0.15 # 15%
    operational = total_supply * 0.10 # 10%
    locked_reserve = total_supply * 0.55 # 55%
    
    # 1% dari Founder (1 Triliun) untuk 1 Juta orang
    genesis_reward_pool = 1_000_000_000_000 
    
    return {
        "token": "LUV (Lovely Coin)",
        "total_supply": f"{total_supply:,}",
        "genesis_reward_per_iid": "1,000,000 LUV",
        "status": "Aura Distribution Ready (01-02-2027)",
        "allocation": {
            "Founder (Inc. 1% Reward)": "20%",
            "Disaster Pool": "15%",
            "Operational": "10%",
            "Locked (2 Years)": "55%"
        }
    }

if __name__ == "__main__":
    print(json.dumps(get_luv_treasury(), indent=4))
