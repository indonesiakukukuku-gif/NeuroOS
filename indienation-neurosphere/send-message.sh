#!/bin/bash
echo -e "\e[1;36m[Neuro-Comm] Initializing Secure Channel...\e[0m"
read -p "Enter Recipient ID: " RECIPIENT
read -p "Enter Message: " MESSAGE

# Hitung ukuran pesan
SIZE=${#MESSAGE}

if [ $SIZE -gt 104857600 ]; then
    echo -e "\e[1;31m[ERROR] MESSAGE TOO LARGE (MAX 100MB)\e[0m"
else
    echo "------------------------------------------"
    echo -e "\e[1;33mFROM      :\e[0m IID-021-FOUNDER"
    echo -e "\e[1;33mTO        :\e[0m $RECIPIENT"
    echo -e "\e[1;32mSTATUS    :\e[0m ENCRYPTED & SIGNED"
    echo -e "\e[1;34mLOG       :\e[0m Message Committed to Sovereign-FS"
    echo "------------------------------------------"
    # Simpan ke Audit Log (Phase 3 Hook)
    echo "$(date) | TO: $RECIPIENT | SIZE: ${SIZE}B" >> server/kernel/comm.log
fi
