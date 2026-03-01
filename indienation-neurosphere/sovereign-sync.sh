#!/bin/bash
echo -e "\e[1;36m[Sync-Core] Initiating Sovereign Synchronization...\e[0m"

# 1. Hitung Ukuran Folder (Batas 10GB)
USAGE=$(du -sm . | cut -f1)
echo -e "\e[1;33m[1/3] Current Storage Usage: ${USAGE}MB / 10240MB\e[0m"

# 2. Buat Backup lokal (Batas 100MB)
./sovereign-backup.sh

# 3. Git Push ke GitHub
echo -e "\e[1;33m[2/3] Committing Changes to Repository...\e[0m"
git add .
git commit -m "Sovereign Update: $(date +%Y-%m-%d) | Node: LX-4-ALPHA-01"

echo -e "\e[1;33m[3/3] Pushing to Cloud Gate (GitHub)...\e[0m"
git push origin main

echo "------------------------------------------"
echo -e "\e[1;32m[SUCCESS] NeuroSphere Synced & Secured.\e[0m"
echo "------------------------------------------"
