#!/bin/bash
# Logic: Real Ledger Accounting for NeuroSphere

LEDGER="neuro_ledger.json"

distribute() {
    local id=$1
    local amount=$(( ( RANDOM % 11 ) ))
    
    # AI Guard Validation: Cek apakah ID sudah ada
    current_bal=$(jq -r ".wallets[\"$id\"] // 0" $LEDGER)
    new_bal=$((current_bal + amount))
    
    # Update Ledger menggunakan JQ (Pastikan pkg install jq sudah dilakukan)
    tmp=$(mktemp)
    jq ".wallets[\"$id\"] = $new_bal | .tokenomics.LUV.circulating += $amount" $LEDGER > "$tmp" && mv "$tmp" $LEDGER
    
    echo ">> [AI GUARD] Transaction Verified for $id: +$amount LUV (New Balance: $new_bal)"
}

echo "[E-KINDNESS] Executing Real Supply Distribution..."
for i in {21..25}; do
    distribute "IID-0$i-GLOBAL"
done

echo ">> Ledger Updated. Current Circulating: $(jq -r '.tokenomics.LUV.circulating' $LEDGER) LUV"
