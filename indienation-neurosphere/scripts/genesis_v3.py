import requests

# URL Database baru yang sudah aktif
DB_BASE = "https://indienation-tm-default-rtdb.asia-southeast1.firebasedatabase.app/pioneers/"
pioneers = ["IID-011", "IID-012", "IID-013", "IID-014", "IID-015", "IID-016", "IID-017", "IID-018", "IID-019", "IID-020"]

def init_genesis():
    print("🔋 [GENESIS] Memulai Injeksi Kedaulatan v3...")
    for iid in pioneers:
        data = {
            "balance_eur": 1270.0,
            "nonce": 0,
            "status": "ANCHORED",
            "last_sync": "2026-02-19"
        }
        # Menggunakan PUT untuk memastikan data benar-benar tercipta
        response = requests.put(f"{DB_BASE}{iid}.json", json=data)
        if response.ok:
            print(f"✅ {iid}: Initialized with €1,270.00")
        else:
            print(f"❌ {iid}: Gagal (Status: {response.status_code})")

if __name__ == "__main__":
    init_genesis()
