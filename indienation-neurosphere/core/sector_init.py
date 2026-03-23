import json
import os

CORE_DIR = os.path.expanduser("~/indienation-neurosphere/core")
MEM_FILE = os.path.join(CORE_DIR, "kernel_memory.json")

sectors = [
    "Investment", "Music", "CSR / Key of Kindness", "Seni & Budaya", "Pendidikan",
    "Pariwisata", "Lingkungan Hidup", "Hukum", "Agrobisnis", "Perikanan",
    "Trading Bursa", "Entertainment", "Dunia Anak", "Dunia Wanita", "Pekerjaan",
    "Fashion & Lifestyle", "UMKM & Ekspor", "Sport", "Recycling", "Lelang E-Legacy",
    "Teknologi & Inovasi", "Kesehatan & Kecantikan", "Automotif & Transportasi",
    "Real Estate & Properti", "Keuangan & Perbankan", "Telekomunikasi & Internet",
    "Kreatif & Desain", "Makanan & Minuman", "Keamanan & Proteksi", "Pengembangan SDM",
    "Quantum Computing", "Space Exploration", "Decentralized Identity"
]

def update_kernel():
    data = {
        "version": "0.7-C",
        "founder": "INDIE-Founder",
        "iid": "TM-0001-0001-0001",
        "sectors_count": len(sectors),
        "sectors_map": {i+1: name for i, name in enumerate(sectors)},
        "argi_status": "ACTIVE",
        "relay_logic": "365-DAYS-LOCKED"
    }
    with open(MEM_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    print("✅ Kernel Memory Synced with 33 Sovereign Sectors.")

if __name__ == "__main__":
    update_kernel()
