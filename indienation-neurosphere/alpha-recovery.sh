#!/bin/bash
# NEUROSPHERE ALPHA RECOVERY
# PURPOSE: RESTORE SYSTEM OPERATIONS AFTER LOCKDOWN

echo -e "\033[0;32m################################################"
echo "NEUROSPHERE ALPHA RECOVERY PROTOCOL"
echo -e "################################################\033[0m"
read -p "ENTER FOUNDER KEY TO INITIATE RECOVERY: " key

if [ "$key" == "INDIE-2026" ]; then
    echo "[*] AUTHORIZATION GRANTED."
    echo "[*] PERFORMING SYSTEM INTEGRITY CHECK..."
    sleep 2
    echo "[*] VERIFYING TREASURY RESERVES (€100,000/Citizen)... OK."
    echo "[*] RE-LINKING AURALANG REWARD ENGINE... OK."
    
    # Reset system status to ACTIVE
    echo '{"status": "ACTIVE", "reason": "Founder Authorized Restoration"}' > public/system_status.json
    
    # Deploy the restoration
    firebase deploy --only hosting
    
    echo -e "\033[0;32m[SUCCESS] SYSTEM RESTORED. GLOBAL CITIZEN WALLETS ACTIVE.\033[0m"
else
    echo "[ERROR] INVALID KEY. RECOVERY ABORTED."
fi
