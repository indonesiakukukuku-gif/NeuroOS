#!/bin/bash
# [Neuro-Guard] LUV GENESIS COUNTDOWN MONITOR

TARGET_DATE="2027-02-01"
echo -e "\e[1;35m=== NEUROSPHERE GENESIS COUNTDOWN ===\e[0m"
echo -e "Event: Distribusi 1 Juta LUV (Alokasi Founder) [cite: 2025-12-20]"
echo -e "Target: 1 Juta Pionir Pertama [cite: 2026-01-31]"
echo -e "--------------------------------------------"

while true; do
    CURRENT_DATE=$(date +%s)
    TARGET_SEC=$(date -d "$TARGET_DATE" +%s)
    DIFF=$((TARGET_SEC - CURRENT_DATE))

    if [ $DIFF -le 0 ]; then
        echo -e "\e[1;32m[STATUS] KICK-OFF DIMULAI! DISTRIBUSI AKTIF.\e[0m"
        break
    fi

    DAYS=$((DIFF / 86400))
    HOURS=$(( (DIFF % 86400) / 3600 ))
    MINS=$(( (DIFF % 3600) / 60 ))
    SECS=$(( DIFF % 60 ))

    echo -ne "\rT-Minus: $DAYS Hari $HOURS Jam $MINS Menit $SECS Detik "
    sleep 1
done
