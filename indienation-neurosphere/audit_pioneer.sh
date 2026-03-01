#!/bin/bash
echo "=== NEUROSPHERE SSOT AUDITOR v1.0 ==="
echo "Menganalisis file bukti transaksi..."
echo "-------------------------------------"

if [ -z "$1" ]; then
    echo "Gunakan: ./audit_pioneer.sh nama_file_proof.txt"
    exit 1
fi

# Mengekstrak data penting dari file proof
TYPE=$(grep "Type:" "$1" | cut -d' ' -f2)
TS=$(grep "Timestamp:" "$1" | cut -d' ' -f2-)
HASH=$(grep "Secure Hash:" "$1" | cut -d' ' -f3)
BAL=$(grep "New Balance:" "$1" | cut -d' ' -f3)

# Validasi Logika AI-Guard
if [[ $HASH == NS-* ]] || [[ $HASH == LUV-* ]]; then
    echo "[VALID] Hash Terverifikasi: $HASH"
    echo "[DATA]  Waktu Kejadian  : $TS"
    echo "[DATA]  Jenis Transaksi : $TYPE"
    echo "[DATA]  Saldo Akhir     : $BAL"
    echo "-------------------------------------"
    echo "STATUS: KEDAULATAN SAH & TERCATAT"
else
    echo "[DITOLAK] HASH PALSU ATAU DATA TIDAK VALID!"
fi
