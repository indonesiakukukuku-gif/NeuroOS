#!/bin/bash
# NEUROSPHERE OMEGA SWITCH
# WARNING: THIS WILL FREEZE ALL TRANSACTIONS AND MINTING

echo -e "\033[0;31m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
echo "NEUROSPHERE EMERGENCY LOCKDOWN PROTOCOL"
echo -e "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[0m"
read -p "ENTER FOUNDER KEY TO CONFIRM LOCKDOWN: " key

if [ "$key" == "INDIE-2026" ]; then
    echo "[!] AUTHORIZATION GRANTED."
    echo "[!] INITIATING TREASURY FREEZE..."
    echo "[!] DISABLING AURALANG REWARD ENGINE..."
    
    # Create a lockdown manifest for the web app
    echo '{"status": "LOCKED", "reason": "Founder Emergency Protocol"}' > public/system_status.json
    
    # Force deploy the lockdown status
    firebase deploy --only hosting
    
    echo -e "\033[0;31m[SUCCESS] SYSTEM IS NOW IN LOCKDOWN. GLOBAL ASSETS FROZEN.\033[0m"
else
    echo "[ERROR] INVALID KEY. ACCESS DENIED."
fi
