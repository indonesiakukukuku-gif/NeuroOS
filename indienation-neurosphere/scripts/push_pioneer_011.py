import requests
import json
import time

# PASTIKAN .json ADA DI PALING AKHIR SETELAH NAMA NODE
DB_URL = "https://indienation-tm-default-rtdb.asia-southeast1.firebasedatabase.app/pioneers/IID-011.json"

data_pioneer = {
    "name": "PURWANTORO",
    "role": "Pioneer",
    "status": "ANCHORED",
    "living_value_reward": 100000.00,
    "balance_eur": 1270.00,
    "balance_idr": 25275514.60,
    "enpe": 0.00,
    "lovely": 18.00,
    "hash": "NS-2026-IID-011-ANCHORED",
    "encryption": "NEUROLANG-V1",
    "interpreter": "AURALANG",
    "last_sync": int(time.time())
}

def push_to_firebase():
    print(f"🚀 Mencoba ulang dorong data IID-011...")
    try:
        # Menggunakan .put() untuk mengganti/membuat data di node IID-011
        response = requests.put(DB_URL, json=data_pioneer)
        if response.status_code == 200:
            print("✅ BERHASIL! Data Purwantoro telah mengudara di SSOT.")
        else:
            print(f"❌ MASIH GAGAL: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"⚠️ Error Koneksi: {e}")

if __name__ == "__main__":
    push_to_firebase()

