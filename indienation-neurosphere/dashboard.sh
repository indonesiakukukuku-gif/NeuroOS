#!/bin/bash
# NeuroSphere: Executive Founder Dashboard (V3 - Final Sovereign Edition)

LEDGER="neuro_ledger.json"
RELEASE_DATE="2029-02-01"

# Definisi Warna
GOLD='\033[1;33m'
PURPLE='\033[1;35m'
BLUE='\033[1;34m'
RED='\033[1;31m'
NC='\033[0m'

# Kalkulasi Waktu
current_ts=$(date +%s)
target_ts=$(date -d "$RELEASE_DATE" +%s)
diff=$((target_ts - current_ts))
days_left=$((diff / 86400))

echo -e "${GOLD}====================================================${NC}"
echo -e "${GOLD}      NEUROSPHERE DIGITAL CITY - EXECUTIVE          ${NC}"
echo -e "${GOLD}====================================================${NC}"
echo -e "Status: ${GOLD}SOVEREIGN ONLINE${NC} | Founder: ${GOLD}INDIE-Founder${NC}"
echo "----------------------------------------------------"

# 1. Tokenomics Overview
total_supply=$(jq -r '.tokenomics.LUV.total_supply' $LEDGER)
circulating=$(jq -r '.tokenomics.LUV.circulating' $LEDGER)
stable_anchor=$(jq -r '.tokenomics."IND-EUR".anchor_value' $LEDGER)

echo -e "${PURPLE}TOKENOMICS STATUS:${NC}"
echo "- LUV Total Supply : $total_supply"
echo "- LUV Circulating  : $circulating"
echo -e "- IND-EUR Anchor   : ${GOLD}€$stable_anchor (STABLE)${NC}"
echo "----------------------------------------------------"

# 2. AI Guard Protocol Status
echo -e "${RED}AI GUARD ENFORCEMENT:${NC}"
if [ $diff -gt 0 ]; then
    echo -e "- Founder Lock     : ${RED}LOCKED${NC} ($days_left Days Remaining)"
else
    echo -e "- Founder Lock     : ${GOLD}UNLOCKED / LIQUID${NC}"
fi
echo "- Donation Pool    : 15% (Status: OPEN)"
echo "----------------------------------------------------"

# 3. Wallet Aura Visualization
echo -e "${PURPLE}AURA REPUTATION LAYER:${NC}"
jq -r '.wallets | to_entries | sort_by(-.value) | .[] | "\(.key):\(.value)"' $LEDGER | while IFS=: read -r id bal; do
    if [ "$id" == "IID-021-GLOBAL" ]; then
        echo -e "  - ${GOLD}$id: $bal LUV (Sovereign Gold)${NC}"
    elif [ "$bal" -gt 500 ]; then
        echo -e "  - ${PURPLE}$id: $bal LUV (High Compassion)${NC}"
    else
        echo -e "  - ${BLUE}$id: $bal LUV (Logic Blue)${NC}"
    fi
done
echo -e "${GOLD}====================================================${NC}"
