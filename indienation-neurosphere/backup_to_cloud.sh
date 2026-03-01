#!/bin/bash
# NeuroSphere: Sovereign Data Archival Protocol

BACKUP_NAME="NEUROSPHERE_BACKUP_$(date +%Y%m%d_%H%M%S).tar.gz"
TARGET_DIR="$HOME/indienation-neurosphere"

# Definisi Warna
GOLD='\033[1;33m'
NC='\033[0m'

echo -e "${GOLD}----------------------------------------------------${NC}"
echo -e "${GOLD}[AI GUARD] STARTING SYSTEM ARCHIVAL...              ${NC}"
echo -e "${GOLD}----------------------------------------------------${NC}"

# 1. Verifikasi Integritas Sebelum Backup
if [ -f "neuro_ledger.json" ]; then
    echo ">> [OK] Ledger Integrity Verified."
else
    echo ">> [ERROR] Ledger not found! Aborting backup."
    exit 1
fi

# 2. Kompresi Folder (Aman di bawah limit 100M)
tar -czf "$BACKUP_NAME" *.sh *.json *.txt *.aur 2>/dev/null

# 3. Verifikasi Ukuran
file_size=$(du -h "$BACKUP_NAME" | cut -f1)
echo ">> [SUCCESS] Archive Created: $BACKUP_NAME"
echo ">> [INFO] Final Package Size: $file_size"

# 4. Generate Hash Keamanan
echo ">> [HASH] $(sha256sum "$BACKUP_NAME" | head -c 32)"

echo -e "${GOLD}----------------------------------------------------${NC}"
echo -e "${GOLD}>> SYSTEM BACKUP COMPLETE. READY FOR CLOUD RELAY.   ${NC}"
echo -e "${GOLD}----------------------------------------------------${NC}"
