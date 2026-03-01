#!/bin/bash
# [Neuro-Guard] SOVEREIGN SECURITY DASHBOARD v1.3

while true; do
    echo -e "\n\e[1;36m=== NEUROSPHERE SOVEREIGN GUARD ===\e[0m"
    echo -e "Node: LX-4-ALPHA-01 | Founder: INDIE-Founder"
    echo -e "--------------------------------------------"
    echo -e "[1] VERIFY - Validasi Token Cloud Gate"
    echo -e "[2] SYNC   - Sinkronisasi Data (Auto-Pull)"
    echo -e "[3] PANIC  - Emergency Lock & Wipe Keys"
    echo -e "[4] EXIT   - Keluar ke Kernel Shell"
    echo -en "\e[1;33mPilih Opsi [1-4]: \e[0m"
    read OPTION

    case $OPTION in
        1)
            ./verify-identity.sh
            ;;
        2)
            ./auto-pull.sh
            ;;
        3)
            ./panic_lock.sh
            break
            ;;
        4)
            echo "Kembali ke mode operasional..."
            break
            ;;
        *)
            echo -e "\e[1;31mOpsi tidak valid.\e[0m"
            ;;
    esac
done
