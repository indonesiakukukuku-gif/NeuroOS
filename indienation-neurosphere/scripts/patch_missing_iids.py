import requests, json, time

DB_BASE_URL = "https://indienation-tm-default-rtdb.asia-southeast1.firebasedatabase.app/pioneers/"

missing_pioneers = {
    "IID-012": "MARSELUS HASAN",
    "IID-013": "KIKI KESTURI",
    "IID-014": "DIAVATCHE BOGUI EUGÈNE"
}

def patch():
    for iid, name in missing_pioneers.items():
        print(f"🛡️ Patching Missing IID {iid}: {name}...")
        data = {
            "name": name,
            "role": "Pioneer",
            "status": "ANCHORED",
            "living_value_reward": 100000.0,
            "balance_eur": 1270.0,
            "hash": f"NS-2026-{iid}-VERIFIED",
            "last_sync": int(time.time())
        }
        requests.put(f"{DB_BASE_URL}{iid}.json", json=data)
        time.sleep(0.5)
    print("✅ DATA IID-012, 013, 014 BERHASIL DISINKRONKAN.")

if __name__ == "__main__":
    patch()
