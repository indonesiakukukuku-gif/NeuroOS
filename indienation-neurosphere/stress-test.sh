#!/bin/bash
echo -e "\e[1;31m[STRESS-TEST] Launching Anomaly Rapid Fire...\e[0m"
for i in {1..10}
do
   echo -e "\e[1;33m[Attempt $i]\e[0m Sending Invalid Nonce Packet..."
   # Simulasi pengiriman data tanpa tanda tangan Ed25519 yang valid
   ./tx-sim.sh "INTRUDER_DATA" 2>/dev/null
   
   echo -e "\e[1;33m[Attempt $i]\e[0m Testing 100MB+ Buffer Overflow..."
   # Mencoba mengirim payload besar secara paksa
   dd if=/dev/urandom bs=1M count=110 2>/dev/null | ./tx-sim.sh 2>/dev/null
done
echo -e "\e[1;32m[STRESS-TEST] Finished. Checking Kernel Integrity...\e[0m"
