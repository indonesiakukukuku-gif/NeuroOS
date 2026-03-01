import requests

DB_BASE = "https://indienation-tm-default-rtdb.asia-southeast1.firebasedatabase.app/pioneers/"

# Daftar Nama Resmi berdasarkan dokumen yang diunggah
pioneer_identities = {
    "IID-011": "PURWANTORO",
    "IID-012": "MARSELUS HASAN",
    "IID-013": "KIKI KESTURI",
    "IID-014": "DIAVATCHE BOGUI EUGÈNE",
    "IID-015": "Miftahudin",
    "IID-016": "Kastim",
    "IID-017": "Meiriska",
    "IID-018": "Rasheed Abiodun O. Gbaiye",
    "IID-019": "Lugard Jumbo",
    "IID-020": "Heri Heryanto"
}

def sync_identities():
    print("👤 [IDENTITY] Sinkronisasi Nama Pioneer ke Firebase...")
    for iid, name in pioneer_identities.items():
        response = requests.patch(f"{DB_BASE}{iid}.json", json={"name": name})
        if response.ok:
            print(f"✅ {iid} terverifikasi sebagai: {name}")
    print("🛡️ DATABASE IDENTITAS TELAH DIPERBARUI.")

if __name__ == "__main__":
    sync_identities()
