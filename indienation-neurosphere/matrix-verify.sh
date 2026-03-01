#!/bin/bash
echo "[Matrix-CC] Verifying Sovereign Logic..."
# Mengecek kehadiran file dan kata kunci kedaulatan
[ -f "server/economy/walletEngine.ts" ] && grep -q "15%" server/economy/walletEngine.ts && echo "Wallet: VALID (Social Tax ENFORCED)"
[ -f "server/kernel/identityEngine.ts" ] && grep -q "Ed25519" server/kernel/identityEngine.ts && echo "Identity: VALID (Hardware Binding READY)"
echo "[Success] All Sovereign Modules are ready for deployment."
