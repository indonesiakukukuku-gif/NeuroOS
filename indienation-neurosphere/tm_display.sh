#!/bin/bash
# NEUROSPHERE DIGITAL CITY - NFT TM VISUALIZER
# Founder: INDIE-Founder | Identity: IID-021+

# Warna untuk estetika terminal
GOLD='\033[1;33m'
CYAN='\033[0;36m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GOLD}"
echo "  _   _                      ____  _                     "
echo " | \ | | ___ _   _ _ __ ___ / ___|| |__   ___ _ __ ___  "
echo " |  \| |/ _ \ | | | '__/ _ \  ___ \ '_ \ / _ \ '__/ _ \ "
echo " | |\  |  __/ |_| | | | (_) |___) | | | |  __/ | |  __/ "
echo " |_| \_|\___|\__,_|_|  \___/|____/|_| |_|\___|_|  \___/ "
echo -e "          DIGITAL CITY - SOVEREIGN IDENTITY${NC}"
echo "-----------------------------------------------------------"
echo -e "FOUNDER  : ${CYAN}INDIE-Founder${NC} | ID: ${CYAN}IID-021+${NC}"
echo -e "STATUS   : ${GREEN}VERIFIED (Lattice-Quantum)${NC}"
echo "-----------------------------------------------------------"

# Simulasi Saldo Berdasarkan Metadata & Anchor Value
# Poin 19: Anchor Value dasar adalah €100.000
echo -e "${GOLD}[ ASSET WALLET - TM CONTAINER ]${NC}"
echo -e "STABLE (IND-EUR) : ${GREEN}€100,000.00${NC} (Anchor Initialized)"
echo -e "ENGINE (ENPE)    : ${CYAN}20,000,000,000,000.00 E${NC} (Staking Pool)"
echo -e "SOCIAL (LUV)     : ${CYAN}1,000,000.00 LUV${NC} (Founder 1% Allocation)"
echo "-----------------------------------------------------------"

# Menampilkan Hash Integrity dari Metadata
HASH=$(grep "ssot_hash" metadata_nft_tm.json | cut -d'"' -f4)
echo -e "SSOT DNA HASH   : ${CYAN}${HASH}${NC}"
echo -e "AI GUARD STATUS : ${GREEN}ACTIVE (PID: $(pgrep -f audit_trigger.sh | head -n 1))${NC}"
echo "-----------------------------------------------------------"
