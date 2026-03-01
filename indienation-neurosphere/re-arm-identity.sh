#!/bin/bash
# [Neuro-Guard] IDENTITY RE-ARMAMENT PROTOCOL

echo -e "\e[1;36m=== RE-ARMING SOVEREIGN IDENTITY ===\e[0m"
echo -e "Node: LX-4-ALPHA-01 | Target: Cloud Gate (GitHub)"
echo -e "--------------------------------------------"

# 1. Bersihkan sisa kegagalan sebelumnya
git config --global --unset credential.helper
rm -rf ~/.git-credentials

# 2. Minta input Token secara senyap (tidak tampil di layar)
echo -n "Masukkan Token ghp_... Anda: "
read -s TOKEN
echo -e "\n\e[1;32m[Verified] Token diterima di buffer sementara.\e[0m"

# 3. Konfigurasi Vault Permanen (LUV-GENESIS Requirement)
git config --global credential.helper store

# 4. Injeksi Kredensial ke Vault (Bukan ke Skrip)
# Format: https://USER:TOKEN@github.com
echo "https://indonesiakukukuku-gif:$TOKEN@github.com" > ~/.git-credentials
chmod 600 ~/.git-credentials

# 5. Uji Coba Jabat Tangan (Handshake)
echo -e "\e[1;33m[Audit] Mencoba koneksi ke Cloud Gate...\e[0m"
if git ls-remote origin &>/dev/null; then
    echo -e "\e[1;32m[SUCCESS] Identitas Pulih. Sovereign Guard ACTIVE.\e[0m"
    # Hapus jejak token dari memory
    unset TOKEN
    exit 0
else
    echo -e "\e[1;31m[CRITICAL] Gagal! Token mungkin salah atau expired.\e[0m"
    unset TOKEN
    exit 1
fi
