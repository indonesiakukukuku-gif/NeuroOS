#!/bin/bash
DB_PATH=~/indienation-neurosphere/core/neuro_registry.db
LOG_FILE=~/indienation-neurosphere/core/sovereign_audit.log
MARKET_FILE=~/indienation-neurosphere/core/market_registry.json

while true; do
    clear
    # Hitung Pemasukan & Investasi
    COUNT=$(sqlite3 $DB_PATH "SELECT COUNT(*) FROM tasks WHERE command LIKE 'S03_%' AND status='COMPLETED';")
    INVEST=$(sqlite3 $DB_PATH "SELECT COUNT(*) FROM tasks WHERE command='S17_INVEST_UPGRADE';")
    
    GROSS=$(( COUNT > 0 ? 1000 + (COUNT-1)*270 : 0 ))
    TOTAL=$(( GROSS - (INVEST * 500) )) 
    
    # Ambil Data Produksi & Level
    LUV=$(python3 -c "import json,os; p='$MARKET_FILE'; print(json.load(open(os.path.expanduser(p)))['total_produced_luv']) if os.path.exists(os.path.expanduser(p)) else print(0)")
    RATE=$(python3 -c "import json,os; p='$MARKET_FILE'; print(json.load(open(os.path.expanduser(p)))['stalls'][0]['production_rate']) if os.path.exists(os.path.expanduser(p)) else print(0)")
    LEVEL=$(python3 -c "import json,os; p='$MARKET_FILE'; print(json.load(open(os.path.expanduser(p)))['stalls'][0]['level']) if os.path.exists(os.path.expanduser(p)) else print(0)")

    echo "=== NEURO-OS CONTROL CENTER (IID-021+) ==="
    echo " [S25] TOTAL TM (NET)     : €$TOTAL"
    echo " [S06] TRAVEL DISTANCE    : $GROSS KM"
    echo " [S01] AURA REWARDS       : $LUV LUV"
    echo "------------------------------------------"
    echo " [S17] PRODUCTION RATE    : +$RATE LUV/Day (LVL $LEVEL)"
    echo " [S29] INTEGRITY STATUS   : $(grep -q "BREACH" <(tail -n 5 $LOG_FILE) && echo "⚠️ BREACH" || echo "✅ OK")"
    echo "------------------------------------------"
    echo " [STATUS] INDIE-AI GOVERNOR IS ACTIVE | 'q' to Exit

    read -t 5 -n 1 cmd
    if [ "$cmd" == "q" ]; then 
        # AUTO-SEAL ON EXIT
        find ~/indienation-neurosphere/ -type f \( -name "*.py" -o -name "*.aura" -o -name "*.sh" \) -exec sha256sum {} + > ~/indienation-neurosphere/core/genesis_manifest.hash
        break
    fi
    if [ "$cmd" == "e" ]; then
        sqlite3 $DB_PATH "INSERT INTO tasks (command, sector_id, status, created_at) VALUES ('S03_RELAY_DAY_$((COUNT+1))', 3, 'PENDING', '$(date)');"
        python3 ~/indienation-neurosphere/core/argi_worker.py
        sleep 1
    fi
    if [ "$cmd" == "u" ]; then
        python3 ~/indienation-neurosphere/core/market_upgrade.py
        sleep 1
    fi
done
