#!/bin/bash
# NEURO-OS: SOVEREIGN MONITORING HUB v1.0
# Designed for INDIE-Founder

# Colors for UI
GOLD='\033[0;33m'
SAPPHIRE='\033[0;34m'
NC='\033[0m' # No Color

while true; do
    clear
    echo -e "${GOLD}=====================================================${NC}"
    echo -e "${GOLD}      NEURO-OS: SOVEREIGN MONITORING HUB v1.0       ${NC}"
    echo -e "${GOLD}      FOUNDER: INDIE-Founder | $(date)              ${NC}"
    echo -e "${GOLD}=====================================================${NC}"
    echo ""
    
    echo -e "${SAPPHIRE}--- [ 🧠 BRAIN STATE: kernel_memory.json ] ---${NC}"
    if [ -f ~/indienation-neurosphere/core/kernel_memory.json ]; then
        # Pretty-print JSON using python's built-in tool
        cat ~/indienation-neurosphere/core/kernel_memory.json | python3 -m json.tool
    else
        echo "⚠️ Memory file not found."
    fi
    
    echo ""
    echo -e "${SAPPHIRE}--- [ 💓 LIVE PULSE: kernel.log (Last 10) ] ---${NC}"
    if [ -f ~/indienation-neurosphere/core/kernel.log ]; then
        tail -n 10 ~/indienation-neurosphere/core/kernel.log
    else
        echo "⚠️ Log file not found. Is the Kernel running?"
    fi
    
    echo ""
    echo -e "${GOLD}=====================================================${NC}"
    echo " [CTRL+C] to Exit | Refreshing every 10s..."
    
    sleep 10
done
