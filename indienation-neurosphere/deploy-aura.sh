#!/bin/bash
# NeuroSphere Executive Deployer v2.0
echo "🛡️ [CORE] Memulai Sinkronisasi NeuroSphere..."

# Pastikan berada di root
cd "$(dirname "$0")"

if [ -d "public" ]; then
    SIZE=$(du -sm public | cut -f1)
    if [ $SIZE -gt 100 ]; then
        echo "⚠️ ALERT: Data public (${SIZE}M) melebihi batas 100M!"
        exit 1
    fi
    echo "📊 Status Storage: ${SIZE}M / 100M [SAFE]"
else
    echo "❌ ERROR: Folder 'public' tidak ditemukan!"
    exit 1
fi

echo "🎲 Menjalankan Distribusi E-KINDNESS..."
aura ./scripts/distribute_kindness.aura

echo "🧠 Mengintegrasikan Auralang Logic ke Cloud..."


./update_registry.sh

firebase deploy --only hosting

echo "✅ SUCCESS: Peradaban NeuroSphere Online & Anchored."
echo "🌐 Master Portal: https://indienation-tm.web.app/master-portal"
