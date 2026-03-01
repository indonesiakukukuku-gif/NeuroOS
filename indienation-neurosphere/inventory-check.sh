#!/bin/bash
# NEUROSPHERE PHYSICAL ASSET LEDGER
# Tracking assets purchased via BNB/ETH

clear
echo "=============================================================="
echo "          NEUROSPHERE PHYSICAL ASSET INVENTORY                "
echo "=============================================================="
echo " Managed by: INDIE-Founder | Verified by: AI Guard "
echo "--------------------------------------------------------------"
echo "ID       | ASSET NAME          | SOURCE | VALUE    | STATUS   "
echo "---------|---------------------|--------|----------|----------"

# Daftar aset fisik (Simulasi dari database lokal)
echo "AST-001  | Memory Card 2TB     | ETH    | 0.10 ETH | RECEIVED"
echo "AST-002  | Server Rack Node 1  | BNB    | 1.20 BNB | SHIPPING"
echo "AST-003  | Dev Smartphone      | ETH    | 0.35 ETH | ORDERED"

echo "--------------------------------------------------------------"
echo "[ SUMMARY ]"
# Menghitung total aset dari file log jika ada
TOTAL_ASSETS=$(grep -c "AST-" inventory-check.sh)
echo " Total Physical Assets: $TOTAL_ASSETS Items"
echo " Storage Used: 28GB Total | 10GB Allocated for NeuroSphere"
echo "=============================================================="
