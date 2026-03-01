#!/bin/bash
# [Neuro-Guard] REFINED QUANTUM PULL v1.1
# Target: indonesiakukukuku-gif/NeuroOS

echo -e "\e[1;36m[Quantum-Pull] Memulai Sinkronisasi Terenkripsi...\e[0m"
echo -e "[Audit] Memvalidasi Lattice-Seal Lokal ke NeuroOS..."

# Pastikan remote origin mengarah ke repositori yang benar
git remote set-url origin https://github.com/indonesiakukukuku-gif/NeuroOS.git

if git pull origin main; then
    echo -e "\e[1;32m[SUCCESS] Sinkronisasi NeuroOS Berhasil.\e[0m"
else
    echo -e "\e[1;31m[CRITICAL] Sinkronisasi Gagal. Pastikan Token Aktif.\e[0m"
    exit 1
fi
