import json
import random

def get_aura_pulse():
    # Simulasi pembacaan sentimen dari 10 Milyar IID di masa depan
    harmony_index = random.uniform(85.0, 99.9) # Berada di level tinggi karena Debt-Free
    
    status_map = {
        range(90, 101): "GOLDEN_AGE",
        range(75, 90): "STABLE_PROSPERITY",
        range(50, 75): "RECOVERY_PHASE"
    }
    
    status = "NEUTRAL"
    for r, s in status_map.items():
        if int(harmony_index) in r:
            status = s
            break
            
    return {
        "sector": "S09 - Sentiment Pulse",
        "global_harmony_index": f"{harmony_index:.2f}%",
        "aura_status": status,
        "luv_multiplier": f"x{1 + (harmony_index/100):.2f}",
        "insight": "Distribusi €100.000 menekan tingkat stres finansial global secara radikal."
    }

if __name__ == "__main__":
    print(json.dumps(get_aura_pulse(), indent=4))
