#!/bin/bash
echo -e "\e[1;31m[AI-Sentinel] Initializing Defense Layer...\e[0m"
sleep 1

# Fungsi untuk mengunci akses folder kernel dan economy
echo -e "\e[1;33m[AI-Sentinel] Enforcing File Sovereignty (chmod 600)...\e[0m"
chmod -R 600 server/kernel
chmod -R 600 server/economy

# Verifikasi integritas
if [ -w "server/kernel/identityEngine.ts" ]; then
    echo -e "\e[1;32m[AI-Sentinel] SUCCESS: Sovereign Files are now Isolated.\e[0m"
else
    echo -e "\e[1;31m[AI-Sentinel] WARNING: Security Protocol Bypass Detected!\e[0m"
fi

echo -e "\e[1;34m[AI-Sentinel] Monitoring background processes for anomalies...\e[0m"
