#!/bin/bash
# Load Blacklist Logic (Simulated)
VIOLATIONS_FILE="server/kernel/identity/violations.log"

echo -e "\e[1;36m[Neuro-VM] Initiating Sovereign Transaction...\e[0m"

# 1. Cek apakah user sudah masuk daftar EXILED
if [ -f "$VIOLATIONS_FILE" ] && [ $(grep -c "BAN" "$VIOLATIONS_FILE") -ge 1 ]; then
    echo -e "\e[1;31m[CRITICAL] ACCESS DENIED: YOUR ENTITY IS EXILED.\e[0m"
    exit 1
fi

read -p "Enter Amount of LUV to Transfer: " AMOUNT

# 2. Logika Verifikasi (Simulasi Gagal jika input bukan angka)
if [[ ! $AMOUNT =~ ^[0-9]+$ ]]; then
    echo -e "\e[1;33m[WARNING] Invalid Input Detected.\e[0m"
    echo "VIOLATION_RECORD: $(date)" >> "$VIOLATIONS_FILE"
    
    COUNT=$(wc -l < "$VIOLATIONS_FILE")
    if [ $COUNT -ge 3 ]; then
        echo "STATUS: BAN" >> "$VIOLATIONS_FILE"
        echo -e "\e[1;31m[KERNEL_PANIC] 3 Violations Reached. Permanent Ban Imposed.\e[0m"
    else
        echo -e "\e[1;33m[AI-SENTINEL] Violation $COUNT/3. Be careful.\e[0m"
    fi
    exit 1
fi

# 3. Success Path
TAX=$(echo "$AMOUNT * 0.15" | bc)
echo -e "\e[1;32m[SUCCESS] Transaction Authorized.\e[0m"
echo -e "\e[1;34m[SOCIAL TAX] 15% Enforced: $TAX LUV distributed.\e[0m"
