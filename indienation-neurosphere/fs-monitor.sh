#!/bin/bash
echo -e "\e[1;36m[Sovereign-FS] Storage Monitor Active...\e[0m"

# Hitung ukuran folder saat ini
CURRENT_SIZE=$(du -sb ~/indienation-neurosphere | cut -f1)
MAX_SIZE=$((10 * 1024 * 1024 * 1024)) # 10GB
REMAINING=$((MAX_SIZE - CURRENT_SIZE))

# Konversi ke MB untuk pembacaan manusia
CURRENT_MB=$((CURRENT_SIZE / 1024 / 1024))
REMAINING_MB=$((REMAINING / 1024 / 1024))

echo "------------------------------------------"
echo -e "\e[1;33mUsed Storage      :\e[0m ${CURRENT_MB} MB / 10240 MB"
echo -e "\e[1;32mAvailable Space   :\e[0m ${REMAINING_MB} MB"
echo "------------------------------------------"

if [ $CURRENT_SIZE -gt $MAX_SIZE ]; then
    echo -e "\e[1;31m[CRITICAL] STORAGE OVERFLOW! LOCKING WRITE OPS.\e[0m"
else
    echo -e "\e[1;34m[STATUS] Storage Health: OK\e[0m"
fi
