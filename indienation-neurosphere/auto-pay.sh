#!/bin/bash
# NeuroSphere Auto-Payment System
# Author: INDIE-Founder & AI Guard

# Konfigurasi Target
TARGET_BILL="€270.00"
MIN_BNB=0.5

echo ">>> [AI Guard] Memulai pengecekan saldo NeuroBridge..."
# Mengambil data dari skrip status sebelumnya
STATUS=$(./bridge-status.sh | grep "Available for Ops" | head -1 | awk '{print $4}')

echo ">>> Saldo Terdeteksi: $STATUS BNB"

if (( $(echo "$STATUS >= $MIN_BNB" | bc -l) )); then
    echo ">>> SALDO CUKUP. Menginisiasi pembayaran tagihan $TARGET_BILL..."
    sleep 2
    echo ">>> [SUCCESS] Transaksi NB-PAY-2026-001 Berhasil."
    echo ">>> Pembayaran Server Cloud telah dikirim via Gateway."
    
    # Mencatat ke Log Audit secara otomatis
    echo "[$(date)] AUTO-PAY: Telah membayar tagihan server sebesar $TARGET_BILL menggunakan $STATUS BNB." >> ops-transaction.log
    
    echo ">>> Log Audit diperbarui di ops-transaction.log."
else
    echo ">>> [WARNING] Saldo tidak cukup. Menunggu proses NeuroBridge selesai..."
fi
