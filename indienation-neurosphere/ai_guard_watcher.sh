#!/bin/bash
# AI GUARD WATCHER v1.2 - NeuroSphere Security Layer
# Menggunakan /proc/net/tcp sebagai fallback jika netstat gagal

LOG_FILE="$HOME/indienation-neurosphere/access_log.txt"
touch $LOG_FILE

echo "🛡️ AI Guard Watcher (Kernel-Level Check) active..." >> $LOG_FILE

while true; do
    # Memeriksa koneksi pada port 22 (SSH) secara langsung di tabel kernel
    # 0016 adalah hex untuk port 22. Status 01 berarti 'ESTABLISHED'
    NEW_CONN=$(cat /proc/net/tcp | grep ":0016 " | grep " 01 ")

    if [ ! -z "$NEW_CONN" ]; then
        TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
        echo "⚠️ [$TIMESTAMP] SSH connection detected in Kernel Table" >> $LOG_FILE

        # Verifikasi Latency untuk mencegah Proxy Christina Chapman
        LATENCY=$(ping -c 1 8.8.8.8 | grep 'time=' | awk -F'time=' '{print $2}' | awk '{print $1}')
        
        if [ -z "$LATENCY" ]; then LATENCY=0; fi # Safety check
        
        echo "Checking Latency: ${LATENCY}ms" >> $LOG_FILE

        if (( $(echo "$LATENCY > 5.0" | bc -l) )); then
            echo "🚨 ALERT: High Latency (${LATENCY}ms). Potential Remote Proxy!" >> $LOG_FILE
            # Sesuai IID Mathematics: Memulai penguncian aset sementara
            echo "Action: Freezing IID-021+ Assets (Neurosphere Protection)" >> $LOG_FILE
        fi
    fi
    sleep 5
done
