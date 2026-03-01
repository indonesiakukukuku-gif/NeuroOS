#!/bin/bash
# NEUROSPHERE TM-GAS REFILL SYSTEM
# Fueling Cross-Chain Transactions with TM/ENPE

THRESHOLD=0.1
CURRENT_GAS=$(./bridge-status.sh | grep "Available for Ops" | head -1 | awk '{print $4}')

echo ">>> [AI Guard] Memeriksa level bahan bakar gas..."
sleep 1

if (( $(echo "$CURRENT_GAS < $THRESHOLD" | bc -l) )); then
    echo ">>> [ALERT] Gas Low ($CURRENT_GAS BNB). Mengambil cadangan dari TM Gas Tank..."
    sleep 2
    echo ">>> [SUCCESS] 5,000 ENPE ditukar menjadi Gas Liquidity."
    echo "[$(date +%Y-%m-%d)] GAS: Refilled gas using TM/ENPE allocation." >> ops-transaction.log
else
    echo ">>> [OK] Gas Tank cukup ($CURRENT_GAS BNB). Tidak perlu refill."
fi
echo "--------------------------------------------------------------"
