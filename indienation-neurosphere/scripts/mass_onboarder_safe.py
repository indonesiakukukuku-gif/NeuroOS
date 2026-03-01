import requests, json, time

DB_BASE_URL = "https://indienation-tm-default-rtdb.asia-southeast1.firebasedatabase.app/pioneers/"

pioneers = {
    "IID-015": "Miftahudin",
    "IID-016": "Kastim",
    "IID-017": "Meiriska",
    "IID-018": "Rasheed Abiodun O. Gbaiye",
    "IID-019": "Lugard Jumbo",
    "IID-020": "Heri Heryanto"
}

def onboard():
    for iid, name in pioneers.items():
        print(f"🛡️ Onboarding {iid}: {name}...")
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
    print("✅ SEMUA PIONEER TELAH TERDAFTAR DI SSOT.")

if __name__ == "__main__":
    onboard()
