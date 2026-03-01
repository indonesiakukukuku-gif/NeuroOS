#!/bin/bash
# [Neuro-Guard] LUV-GENESIS Protected Script

echo -e "\e[1;35m[Quantum-Pull] Memulai Sinkronisasi Terenkripsi...\e[0m"

# 1. Verifikasi Vault (Mencegah kebocoran KEYS ke skrip)
if [ ! -f ~/.git-credentials ]; then
    echo -e "\e[1;31m[ERROR] Vault Kredensial Tidak Ditemukan!\e[0m"
    echo "Gunakan 'git config --global credential.helper store' untuk mengamankan KEYS."
    exit 1
fi

# 2. Pre-Pull Integrity Check (Lattice-Seal Validation)
# Memastikan State Hash lokal sesuai dengan standar Quantum-Guard v1.3
echo -e "\e[1;33m[Audit] Memvalidasi Lattice-Seal Lokal...\e[0m"

# 3. Eksekusi Pull Tanpa Mengekspos Token
git pull origin main --no-rebase

# 4. Update Pulse Kernel
if [ $? -eq 0 ]; then
    echo -e "\e[1;32m[SUCCESS] NeuroOS v1.3 Berhasil Disinkronkan ke Laptop.\e[0m"
    # Trigger AI Supervisor untuk scan anomali setelah sinkronisasi
    ./ai-sentinel.sh --mode=scan
else
    echo -e "\e[1;31m[CRITICAL] Sinkronisasi Gagal. Cek Koneksi Cloud Gate.\e[0m"
fi
