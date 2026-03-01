#!/bin/bash
# NeuroSphere Path Fixer & Environment Alignment
# Author: INDIE-Founder

echo "🛠️ Memulai Perbaikan Jalur NeuroSphere..."

# 1. Membuat file aura_sync.sh jika belum ada
if [ ! -f "aura_sync.sh" ]; then
    echo "Creating aura_sync.sh executor..."
    echo "#!/bin/bash" > aura_sync.sh
    echo "echo '🧠 Auralang Interpreter Active'" >> aura_sync.sh
    chmod +x aura_sync.sh
fi

# 2. Sinkronisasi direktori scripts
mkdir -p scripts logs identities

# 3. Verifikasi Izin Eksekusi
chmod +x deploy-aura.sh save_proof.sh audit_report.sh aura_sync.sh

echo "✅ SUCCESS: Semua jalur (path) telah diselaraskan."
echo "🌐 NeuroSphere siap untuk sinkronisasi cloud."
