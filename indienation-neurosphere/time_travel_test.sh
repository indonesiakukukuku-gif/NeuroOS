#!/bin/bash
# NeuroSphere: AI Guard Time-Lock Testing Module

LEDGER="neuro_ledger.json"
LOCK_RELEASE_DATE="2029-02-01"

echo -e "\033[1;33m----------------------------------------------------\033[0m"
echo -e "\033[1;33m[AI GUARD] TIME-TRAVEL SIMULATION: TESTING LOCKS...\033[0m"
echo -e "\033[1;33m----------------------------------------------------\033[0m"

# Simulasi input tanggal masa depan
if [ -z "$1" ]; then
    CURRENT_SIM_DATE=$(date +%Y-%m-%d)
else
    CURRENT_SIM_DATE=$1
fi

echo "Current Simulation Date: $CURRENT_SIM_DATE"
echo "Target Release Date   : $LOCK_RELEASE_DATE"

# Logika Perbandingan Tanggal
if [[ "$CURRENT_SIM_DATE" > "$LOCK_RELEASE_DATE" ]] || [[ "$CURRENT_SIM_DATE" == "$LOCK_RELEASE_DATE" ]]; then
    echo -e "\033[1;32m>> [SUCCESS] LOCK EXPIRED: 20% Founder Allocation is now LIQUID.\033[0m"
    echo -e "\033[1;32m>> [ACTION] AI Guard transferring 20 Trillion LUV to IID-021-GLOBAL...\033[0m"
else
    echo -e "\033[1;31m>> [DENIED] LOCK ACTIVE: Access to 20% Founder Allocation is RESTRICTED.\033[0m"
    days_left=$(( ( $(date -d "$LOCK_RELEASE_DATE" +%s) - $(date -d "$CURRENT_SIM_DATE" +%s) ) / 86400 ))
    echo ">> [INFO] Remaining Time: $days_left Days."
fi
echo -e "\033[1;33m----------------------------------------------------\033[0m"
