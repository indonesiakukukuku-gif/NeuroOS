#!/bin/bash
# Konfigurasi
BASE_URL="https://indienation-tm-default-rtdb.asia-southeast1.firebasedatabase.app"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="$HOME/indienation-neurosphere/backups/$TIMESTAMP"

echo "🛡️ Memulai Backup Data NeuroSphere ke Lokal..."
mkdir -p $BACKUP_DIR

# Tarik data Pioneers & Ledger
curl -s "$BASE_URL/pioneers.json" -o "$BACKUP_DIR/pioneers_backup.json"
curl -s "$BASE_URL/ledger.json" -o "$BACKUP_DIR/ledger_backup.json"

echo "✅ Backup selesai di: $BACKUP_DIR"
echo "📊 Ukuran Data: $(du -sh $BACKUP_DIR | cut -f1)"
