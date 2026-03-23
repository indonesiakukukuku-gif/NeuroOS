import json, os, sys
core_path = os.path.expanduser("~/indienation-neurosphere/core/")
if core_path not in sys.path: sys.path.append(core_path)

try:
    from sector02_tracker import calculate_relay
    from sector08_anchor import check_debt_integrity
    from sector09_aura import get_aura_pulse
except:
    def calculate_relay(d): return {"akumulasi_saldo": "Error", "visual_progress": "[!]", "sisa_hari": 0}
    def check_debt_integrity(): return {"debt_relevance": "Error"}
    def get_aura_pulse(): return {"global_harmony_index": "0%", "aura_status": "Error"}

def generate_dashboard(day):
    r, d, a = calculate_relay(day), check_debt_integrity(), get_aura_pulse()
    return {
        "SYSTEM": "NEUROSPHERE DIGITAL CITY (IID-021+)",
        "FOUNDER": "INDIE-Founder",
        "ECONOMY": {
            "Total": r.get("akumulasi_saldo"),
            "Debt": d.get("debt_relevance"),
            "Progress": r.get("visual_progress")
        },
        "AURA": {
            "Index": a.get("global_harmony_index"),
            "Status": a.get("aura_status")
        },
        "TIMELINE": {"Day": day, "Remaining": r.get("sisa_hari")}
    }

if __name__ == "__main__":
    day_in = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    print(json.dumps(generate_dashboard(day_in), indent=4))
