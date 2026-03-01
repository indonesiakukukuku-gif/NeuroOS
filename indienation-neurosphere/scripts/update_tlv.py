import requests

DB_BASE = "https://indienation-tm-default-rtdb.asia-southeast1.firebasedatabase.app/pioneers/"
pioneers = ["IID-011", "IID-012", "IID-013", "IID-014", "IID-015", "IID-016", "IID-017", "IID-018", "IID-019", "IID-020"]

def init_tlv():
    print("💎 [ANCHOR] Mengunci Total Living Value ke €100.000,00...")
    for iid in pioneers:
        requests.patch(f"{DB_BASE}{iid}.json", json={"tlv_eur": 100000.00})
    print("✅ SELESAI.")

if __name__ == "__main__":
    init_tlv()
