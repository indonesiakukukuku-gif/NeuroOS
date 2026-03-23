import json
import os
from datetime import datetime

def register_citizen(iid_name):
    mem_path = os.path.expanduser("~/indienation-neurosphere/core/kernel_memory.json")
    
    # Data awal untuk IID baru
    new_citizen = {
        "iid": iid_name,
        "signup_date": datetime.now().strftime("%Y-%m-%d"),
        "balances": {
            "IND-EUR": 1000, # Hari pertama kick-off
            "LUV_ESTIMATE": 1000000 # Reserved reward
        },
        "relay_day": 1,
        "status": "ACTIVE_AURA"
    }
    
    # Update total distribusi di kernel memory
    try:
        with open(mem_path, 'r+') as f:
            data = json.load(f)
            data['total_distribution_eur'] = data.get('total_distribution_eur', 0) + 1000
            data['active_citizens'] = data.get('active_citizens', 0) + 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
    except:
        pass

    return new_citizen

if __name__ == "__main__":
    import sys
    name = sys.argv[1] if len(sys.argv) > 1 else "IID-GUEST"
    print(json.dumps(register_citizen(name), indent=4))
