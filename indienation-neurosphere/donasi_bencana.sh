#!/bin/bash
# NeuroSphere: Disaster Relief & Emergency Distribution

LEDGER="neuro_ledger.json"

echo "----------------------------------------------------"
echo "[AI GUARD] EMERGENCY DONATION PROTOCOL ACTIVATED"
echo "----------------------------------------------------"

distribute_aid() {
    local target_id=$1
    local amount=$2

    # 1. Cek Ketersediaan Pool Donasi
    pool_avail=$(jq -r '.tokenomics.LUV.donation_pool' $LEDGER)

    if [ "$amount" -gt "$pool_avail" ]; then
        echo ">> [REJECTED] Amount exceeds Donation Pool reserves!"
        return 1
    fi

    # 2. Eksekusi Pencairan (Potong Pool, Tambah Dompet Target)
    tmp=$(mktemp)
    jq ".tokenomics.LUV.donation_pool -= $amount | .wallets[\"$target_id\"] += $amount | .tokenomics.LUV.circulating += $amount" $LEDGER > "$tmp" && mv "$tmp" $LEDGER

    echo ">> [SUCCESS] Aid of $amount LUV sent to $target_id"
    echo ">> [INFO] Remaining Disaster Pool: $(jq -r '.tokenomics.LUV.donation_pool' $LEDGER) LUV"
}

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: ./donasi_bencana.sh <TARGET_ID> <AMOUNT>"
else
    distribute_aid "$1" "$2"
fi
echo "----------------------------------------------------"
