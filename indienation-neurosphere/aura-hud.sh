#!/bin/bash
clear
# Fetch Storage Data
CURRENT_SIZE=$(du -sb ~/indienation-neurosphere 2>/dev/null | cut -f1)
[ -z "$CURRENT_SIZE" ] && CURRENT_SIZE=0
MAX_SIZE=$((10 * 1024 * 1024 * 1024))
CURRENT_MB=$((CURRENT_SIZE / 1024 / 1024))
PERCENTAGE=$((CURRENT_MB * 100 / 10240))

echo -e "\e[1;35m==========================================\e[0m"
echo -e "\e[1;36m    NEUROSPHERE DIGITAL CITY - AURA HUD   \e[0m"
echo -e "\e[1;35m==========================================\e[0m"
echo -e "\e[1;33mFOUNDER    :\e[0m INDIE-Founder"
echo -e "\e[1;33mENTITY ID  :\e[0m IID-021-ROOT-$(hostname | cut -c1-4)"
echo -e "\e[1;33mTRUST      :\e[0m 1.0 (MAXIMUM)"
echo -e "------------------------------------------"
echo -e "\e[1;32m[STABLE] IND-EUR :\e[0m €100,000"
echo -e "\e[1;34m[GIFT]   LUV     :\e[0m 1,000,000 Aura"
echo -e "------------------------------------------"
echo -e "\e[1;33mSTORAGE    :\e[0m ${CURRENT_MB}MB / 10240MB (${PERCENTAGE}%)"
echo -e "\e[1;31mSOCIAL TAX :\e[0m 15% (HARD-ENFORCED)"
echo -e "\e[1;35m==========================================\e[0m"
echo -e "\e[5m[STATUS: SOVEREIGN]\e[0m"
