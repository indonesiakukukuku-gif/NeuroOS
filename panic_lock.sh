#!/bin/bash
# [Neuro-Guard] EMERGENCY AUTO-LOCK PROTOCOL

echo -e "\e[1;31m[!] MENYALAKAN PROTOKOL PANIC LOCK...\e[0m"

# 1. Hapus Kredensial dari Cache Memory
git config --global --unset credential.helper [cite: 2026-02-22]

# 2. Hapus File Kredensial Fisik (Vault)
if [ -f ~/.git-credentials ]; then
    rm -rf ~/.git-credentials [cite: 2026-02-22]
    echo -e "\e[1;33m[Audit] Vault Kredensial Telah Dihancurkan.\e[0m"
fi

# 3. Reset Remote ke URL Bersih (Hapus Token dari URL jika ada)
git remote set-url origin https://github.com/indonesiakukukuku-gif/NeuroOS.git [cite: 2026-02-22]

# 4. Kunci Kernel ke Mode RESTRICTED
echo "RESTRICTED" > kernel/status.lock
echo -e "\e[1;32m[SUCCESS] Akses Cloud Terputus. Sistem Terkunci.\e[0m"
