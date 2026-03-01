#!/bin/bash
echo -e "\e[1;36m[Neuro-Portal] Launching Visual Dashboard...\e[0m"
echo -e "\e[1;33m[Link] http://localhost:8080\e[0m"
echo -e "\e[1;32m[Action] Buka browser HP Anda dan ketik localhost:8080\e[0m"
echo "Tekan CTRL+C untuk mematikan portal."

# Menjalankan server di folder public
cd public && python -m http.server 8080
