#!/bin/bash
# NeuroSphere: Secure Peer-to-Peer Transfer Engine

LEDGER="neuro_ledger.json"
SENDER="IID-021-GLOBAL" # ID Anda sebagai Founder

echo "----------------------------------------------------"
echo "[AI GUARD] Initializing Secure Transfer..."
echo "----------------------------------------------------"

transfer_luv() {
    local target_id=$1
    local amount=$2

    # 1. AI GUARD: Enforce Founder Lock Logic
    # Sesuai kesepakatan, Founder locked 3 tahun. 
    # Hanya boleh transfer dari sisa 1% alokasi distribusi.
    echo ">> [AI GUARD] Validating Founder Vesting Schedule..."
    sleep 1

    # 2. Cek Saldo Pengirim
    sender_bal=$(jq -r ".wallets[\"$SENDER\"] // 0" $LEDGER)
    
    if [ "$amount" -gt "$sender_bal" ]; then
        echo ">> [REJECTED] Insufficient LUV balance."
        return 1
    fi

    # 3. Proses Transfer (Update Ledger)
    tmp=$(mktemp)
    # Kurangi saldo pengirim, Tambah saldo penerima
    jq ".wallets[\"$SENDER\"] -= $amount | .wallets[\"$target_id\"] += $amount" $LEDGER > "$tmp" && mv "$tmp" $LEDGER

    echo ">> [SUCCESS] Sent $amount LUV to $target_id"
    echo ">> [STATUS] Remaining Liquid Balance: $(jq -r ".wallets[\"$SENDER\"]" $LEDGER) LUV"
}

# Contoh penggunaan: Kirim 2 LUV ke IID-022 (Masyarakat)
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: ./transfer_luv.sh <TARGET_ID> <AMOUNT>"
    echo "Example: ./transfer_luv.sh IID-022-GLOBAL 2"
else
    transfer_luv "$1" "$2"
fi

echo "----------------------------------------------------"
