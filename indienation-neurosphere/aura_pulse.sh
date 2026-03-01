#!/bin/bash
# NEUROSPHERE AURA PULSE ENGINE
# Melambangkan detak jantung sistem IID-021+

# Fungsi Pulse (Warna Hijau Terang ke Gelap)
pulse() {
    local colors=("\033[1;32m" "\033[0;32m" "\033[1;30m")
    for color in "${colors[@]}"; do
        echo -ne "\rAI GUARD STATUS : ${color}PULSING (ENCRYPTED)${NC}      "
        sleep 0.3
    done
}

# Warna NC (No Color)
NC='\033[0m'

# Menjalankan Pulse 3 kali sebagai tanda sistem sehat
for i in {1..3}; do
    pulse
done
echo -e "\rAI GUARD STATUS : \033[1;32mACTIVE (INTEGRITY: OK)\033[0m      "
