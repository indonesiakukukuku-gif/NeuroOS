#!/bin/bash
echo "🛡️ Guardian Loop Started. Sentinel is under my protection."
while true; do
    ./scripts/keep_alive.sh
    sleep 300 # Cek setiap 5 menit (300 detik)
done
