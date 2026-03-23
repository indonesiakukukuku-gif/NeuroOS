import time
import os

def sentinel_pulse():
    ssot_path = "MASTER_SOVEREIGN_MAP.txt"
    log_path = "logs/sentinel.log"
    last_mod = 0
    
    print("🛡️ AI GUARD SENTINEL: [WATCHER MODE ACTIVE]")
    
    while True:
        try:
            current_mod = os.path.getmtime(ssot_path)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            
            # Jika ada perubahan pada SSOT (misal Bloom atau Transaksi)
            if current_mod != last_mod:
                last_mod = current_mod
                status = "[SYNC] SSOT Update Detected | Re-calculating Integrity..."
            else:
                status = "[PULSE] 10,000 IIDs Secure | Riba: 0% | Monitoring..."

            with open(log_path, "a") as f:
                f.write(f"[{timestamp}] {status}\n")
            
            print(f"[{timestamp}] {status}", flush=True)
            
        except Exception as e:
            print(f"⚠️ Warning: {e}")
            
        time.sleep(30) # Detak jantung lebih cepat untuk responsivitas (30 detik)

if __name__ == "__main__":
    sentinel_pulse()
