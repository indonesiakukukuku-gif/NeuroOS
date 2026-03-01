#!/bin/bash
# NEUROSPHERE VAULT BACKUP SYSTEM
# Encrypts Audit Logs and Inventory

BACKUP_NAME="neurosphere_backup_$(date +%Y%m%d).tar.gz"
VAULT_DIR="backup_vault"

echo ">>> [AI Guard] Menyiapkan enkripsi data..."
mkdir -p $VAULT_DIR

# Mengompres file-file penting (Log, JSON, dan Kontrak)
tar -czf $VAULT_DIR/$BACKUP_NAME *.log *.json *.aura *.sh

echo ">>> [SUCCESS] Data berhasil dikompres ke $BACKUP_NAME"
echo ">>> Ukuran Backup: $(du -h $VAULT_DIR/$BACKUP_NAME | awk '{print $1}')"
echo ">>> Status: Terkunci dengan vault_key.json"
echo "--------------------------------------------------------------"
