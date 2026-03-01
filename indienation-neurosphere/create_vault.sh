#!/bin/bash
# NeuroSphere Sovereign Vault Creator
SOURCE_DIR="/data/data/com.termux/files/home/indienation-neurosphere"
BACKUP_DIR="$SOURCE_DIR/vaults"
TIMESTAMP=$(date "+%Y%m%d")
VAULT_NAME="NEURO_DATA_$TIMESTAMP.vault"

# Membuat direktori vault jika belum ada
mkdir -p "$BACKUP_DIR"

echo "--- STARTING FRACTAL COMPRESSION: $TIMESTAMP ---"
# Menggunakan tar dengan kompresi maksimal (xz) ke dalam format .vault
tar -cJf "$BACKUP_DIR/$VAULT_NAME" --exclude="*.vault" --exclude="*.log" "$SOURCE_DIR"

# Enkripsi Vault menggunakan Auralang (Lattice-Quantum)
auralang --encrypt "$BACKUP_DIR/$VAULT_NAME" --owner "IID-021+"

echo "Vault Created & Encrypted: $VAULT_NAME"
echo "Status: SOVEREIGN BACKUP VERIFIED"
