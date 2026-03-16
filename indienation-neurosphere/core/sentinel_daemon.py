import time, os, subprocess

PID_FILE = os.path.expanduser("~/indienation-neurosphere/core/sentinel.pid")
LOG_FILE = os.path.expanduser("~/indienation-neurosphere/core/sovereign_audit.log")
HASH_FILE = os.path.expanduser("~/indienation-neurosphere/core/genesis_manifest.hash")

with open(PID_FILE, "w") as f:
    f.write(str(os.getpid()))

def verify_integrity():
    if not os.path.exists(HASH_FILE): return "NO_MANIFEST"
    try:
        # Cek apakah hash saat ini masih sesuai dengan manifest
        result = subprocess.run(["sha256sum", "-c", HASH_FILE], capture_output=True, text=True)
        return "OK" if result.returncode == 0 else "BREACH_DETECTED"
    except:
        return "ERROR"

try:
    while True:
        status = verify_integrity()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] HEARTBEAT | S29 | INTEGRITY: {status}\n")
        time.sleep(10)
except KeyboardInterrupt:
    if os.path.exists(PID_FILE): os.remove(PID_FILE)
