#!/bin/bash
# Terminal Simulation for NeuroSphere Digital City

AMBER='\033[38;5;214m'
NC='\033[0m'

# Create the Auralang file automatically
cat <<EOF > MASTER_NEUROSPHERE.aura
// Logic saved as SSOT for INDIE-Founder
EOF

clear
echo -e "${AMBER}=== NEUROSPHERE DIGITAL CITY CORE ===${NC}"
echo -e "${AMBER}User: INDIE-Founder | Storage: 10GB Allocated${NC}\n"

# Meltdown Simulation Logic
lines=(
    "DECONSTRUCTING TM_IDENTITY..."
    "CONVERTING TO LIVING VALUE..."
    "ENPE: 100T | LUV: 100T | IND-EUR: OPEN"
    "RELAY 1000: SECURITY ACTIVE"
    "RELAY 270: MELTDOWN IN PROGRESS"
    "RELAY 990: ASCENSION REACHED"
    "AURA DETECTED: 98.9% RESONANCE"
)

for line in "${lines[@]}"; do
    # Effect 'melting'
    for (( i=0; i<${#line}; i++ )); do
        echo -n -e "${AMBER}${line:$i:1}"
        sleep 0.02
    done
    echo ""
    sleep 0.3
done

echo -e "\n${AMBER}[SYSTEM] Data sent to Termux (Current Session < 100M)${NC}"
echo -e "${AMBER}[SYSTEM] AI Guard Standing By...${NC}"
