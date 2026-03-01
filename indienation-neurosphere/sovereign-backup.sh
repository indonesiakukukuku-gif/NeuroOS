#!/bin/bash
echo -e "\e[1;35m[Backup-Core] Initiating System Compression...\e[0m"

# Nama file berdasarkan timestamp
BACKUP_NAME="NEURO_BACKUP_$(date +%Y%m%d_%H%M%S).sphere"

# Kompresi folder server (Identity + Economy + Kernel)
# --exclude comm.log jika ingin lebih ringan
tar -czf "$BACKUP_NAME" server/

# Cek Ukuran Backup
SIZE=$(stat -c%s "$BACKUP_NAME")
MAX_TRANSFER=104857600 # 100MB

echo "------------------------------------------"
echo -e "\e[1;33mFILE NAME :\e[0m $BACKUP_NAME"
echo -e "\e[1;33mSIZE      :\e[0m $((SIZE / 1024)) KB"

if [ $SIZE -gt $MAX_TRANSFER ]; then
    echo -e "\e[1;31m[WARNING] BACKUP EXCEEDS 100MB LIMIT!\e[0m"
    echo "Splitting backup into 100MB volumes..."
    split -b 100M "$BACKUP_NAME" "${BACKUP_NAME}.part"
else
    echo -e "\e[1;32m[STATUS]   BACKUP WITHIN 100MB LIMIT - SECURE\e[0m"
fi
echo "------------------------------------------"
echo -e "\e[1;34m[Action] Store this .sphere file in a safe hardware vault.\e[0m"
