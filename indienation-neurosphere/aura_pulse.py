import os
import re
from datetime import date

cert_dir = "certificates"
today = str(date.today())

def pulse_aura():
    for filename in os.listdir(cert_dir):
        if filename.endswith(".txt"):
            path = os.path.join(cert_dir, filename)
            with open(path, "r") as f:
                content = f.read()
            
            # Guard: Cek apakah sudah dipulse hari ini
            if f"LAST-UPDATE: {today}" in content:
                continue
                
            # Update Aura Level
            current_level = float(re.search(r"AURA-LEVEL: ([\d.]+)", content).group(1))
            new_level = round(current_level + 0.01, 2)
            
            # Update atau Tambahkan Timestamp
            if "LAST-UPDATE:" in content:
                new_content = re.sub(r"LAST-UPDATE: .*", f"LAST-UPDATE: {today}", content)
            else:
                new_content = content + f"\nLAST-UPDATE: {today}"
            
            new_content = re.sub(r"AURA-LEVEL: [\d.]+", f"AURA-LEVEL: {new_level}", new_content)
            
            with open(path, "w") as f:
                f.write(new_content)

if __name__ == "__main__":
    pulse_aura()
    print(f"Pulse Synced for {today}")
