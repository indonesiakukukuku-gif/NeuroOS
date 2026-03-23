import json
import os

def check_debt_integrity():
    mem_path = os.path.expanduser("~/indienation-neurosphere/core/kernel_memory.json")
    try:
        with open(mem_path, 'r') as f:
            data = json.load(f)
            
        # Logika Inti: Memastikan variabel 'debt' selalu 0
        current_debt = data.get('system_debt', 0)
        total_distributed = data.get('total_distribution_eur', 0)
        
        # Anchor Value Dasar: €100.000 per orang
        anchor_value = 100000 
        
        if current_debt > 0:
            # Protokol Otomatis Penghapusan Utang (Self-Liquidating)
            data['system_debt'] = 0
            status = "DEBT_DETECTED_AND_ERASED"
        else:
            status = "STABLE_ABUNDANCE"
            
        return {
            "status": status,
            "anchor_per_capita": anchor_value,
            "total_system_value": total_distributed,
            "debt_relevance": "0% (Zero-Debt Policy Active)"
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    result = check_debt_integrity()
    print(json.dumps(result, indent=4))
