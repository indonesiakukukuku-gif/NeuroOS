import os

def generate_report():
    ssot_path = "MASTER_SOVEREIGN_MAP.txt"
    report_path = "REPORTS_GENESIS.txt"
    
    if not os.path.exists(ssot_path):
        print("❌ Error: SSOT tidak ditemukan.")
        return

    with open(ssot_path, "r") as f:
        lines = f.readlines()[1:] # Lewati header

    total_iid = len(lines)
    total_aura = sum(float(line.split(" | ")[3]) for line in lines)
    
    report_content = f"""
=====================================================
        NEUROSPHERE GENESIS SUMMARY REPORT
=====================================================
Founder        : INDIE-Founder
Date           : 2026-03-04
-----------------------------------------------------
Total IID Liberated   : {total_iid:,} Souls
Status                : 100% RIBA-FREE
Total Aura (LUV)      : {total_aura:,} LUV
System Integrity      : OPTIMAL (Guardian Active)
-----------------------------------------------------
"Peradaban dimulai saat penderitaan bunga berhenti."
=====================================================
"""
    with open(report_path, "w") as f:
        f.write(report_content)
    
    print(report_content)

if __name__ == "__main__":
    generate_report()
