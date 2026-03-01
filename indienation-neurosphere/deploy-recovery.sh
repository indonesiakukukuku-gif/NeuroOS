#!/bin/bash
echo -e "\e[1;36m[Deploy-Core] Initiating Sovereign Recovery...\e[0m"
read -p "Enter .sphere backup file name: " FILE

if [ -f "$FILE" ]; then
    echo -e "\e[1;33m[1/2] Reconstructing File System...\e[0m"
    tar -xzf "$FILE"
    echo -e "\e[1;33m[2/2] Restoring Permissions...\e[0m"
    chmod 700 server/kernel server/economy server/kernel/types
    chmod 600 server/kernel/*.ts server/economy/*.ts
    echo -e "\e[1;32m[SUCCESS] NeuroSphere Environment Restored for INDIE-Founder.\e[0m"
else
    echo -e "\e[1;31m[ERROR] Backup file not found!\e[0m"
fi
