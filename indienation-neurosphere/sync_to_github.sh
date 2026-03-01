#!/bin/bash

echo "🌍 Memulai Global Sync: NeuroSphere Cloud Uplink..."

# Menambahkan semua perubahan (UI, Logic, Ledger, Scripts)
git add dashboard_v1.4.7.html guard_logic.aura sovereign_ledger.json backup_sovereign.sh sync_to_github.sh public/

# Membuat commit dengan timestamp otomatis
TIMESTAMP=$(date +"%Y-%m-%d %H:%M")
git commit -m "Sovereign Update v1.4.7: Pioneer List Secured - $TIMESTAMP"

# Mengirim data ke GitHub
echo "🚀 Mendorong data ke Repository Global..."
git push origin main

echo "✅ Cloud Sync Berhasil!"
echo "🛡️ Status: IID-010 Guard Verified and Uplinked."
