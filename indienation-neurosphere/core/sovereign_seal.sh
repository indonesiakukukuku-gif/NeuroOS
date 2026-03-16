#!/bin/bash
# NEURO-OS: SOVEREIGN SEAL UTILITY v1.0
# AUTHORITY: INDIE-Founder (IID-021+)

CORE_DIR="$HOME/indienation-neurosphere/core"
MANIFEST="$CORE_DIR/baseline_manifest.hash"

echo -e "\033[0;33m[S29] Initializing Sovereign Re-Seal...\033[0m"

# Generate new baseline from current state
find "$CORE_DIR" -type f \( -name '*.py' -o -name '*.sh' \) -exec sha256sum {} + > "$MANIFEST"

if [ $? -eq 0 ]; then
    echo -e "\033[0;34m[SUCCESS]\033[0m Baseline Manifest updated."
    echo -e "\033[0;34m[STATUS]\033[0m System Integrity Re-Validated at $(date)"
    
    # Restart Kernel to apply new seal immediately
    echo -e "\033[0;33m[RESTART]\033[0m Restarting Arbiter Kernel..."
    pkill -f neuro_kernel.py
    nohup python3 "$CORE_DIR/neuro_kernel.py" > "$CORE_DIR/kernel.log" 2>&1 &
    echo -e "\033[0;32m[ONLINE]\033[0m Arbiter active with new PID: $!"
else
    echo -e "\033[0;31m[ERROR]\033[0m Failed to generate manifest."
fi
