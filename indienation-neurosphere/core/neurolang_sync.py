import json
import random
import os
from datetime import datetime

def generate_sync_data():
    # Simulasi pembacaan dari 1.242 node
    nodes_count = 1242
    # Frekuensi emosi kolektif (0.0 - 10.0)
    harmony_index = round(random.uniform(7.5, 9.8), 2) 
    
    emotions = {
        "Hope": random.randint(80, 95),
        "Gratitude": random.randint(85, 99),
        "Focus": random.randint(70, 90),
        "Anxiety": random.randint(1, 5) # Sangat rendah karena sistem Abundance
    }
    
    sync_state = {
        "timestamp": str(datetime.now()),
        "active_nodes": nodes_count,
        "global_harmony": harmony_index,
        "sentiment_profile": emotions,
        "status": "SAPPHIRE_SYNC" if harmony_index > 8.0 else "GOLD_EVOLVE"
    }
    
    path = os.path.expanduser("~/indienation-neurosphere/core/sync_state.json")
    with open(path, 'w') as f:
        json.dump(sync_state, f, indent=4)

if __name__ == "__main__":
    generate_sync_data()
