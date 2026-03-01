#!/bin/bash
echo "Daemon Relay IID-000000001 Aktif..."
while true; do
  CURRENT_HOUR=$(date +%H)
  CURRENT_MIN=$(date +%M)
  
  # Jika jam 08:00
  if [ "$CURRENT_HOUR" == "08" ] && [ "$CURRENT_MIN" == "00" ]; then
    echo "Waktunya Relay: $(date)"
    # Jalankan alias relay-now secara manual
    node ~/indienation-neurosphere/scripts/auto_relay.cjs && node ~/indienation-neurosphere/scripts/auralang-run.cjs sync_fire.aura
    # Tunggu 61 detik agar tidak trigger dua kali di menit yang sama
    sleep 61
  fi
  # Cek setiap 30 detik
  sleep 30
done
