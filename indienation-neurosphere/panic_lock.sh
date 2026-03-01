#!/bin/bash
# [Neuro-Guard] REFINED EMERGENCY PANIC LOCK

echo -e "\e[1;31m[!] MENYALAKAN PROTOKOL PANIC LOCK...\e[0m"

# 1. Wipe Kredensial
git config --global --unset credential.helper
[ -f ~/.git-credentials ] && rm -rf ~/.git-credentials

# 2. Reset Remote (Fix Syntax)
git remote set-url origin https://github.com/indonesiakukukuku-gif/NeuroOS.git

# 3. Kunci Kernel (Folder kernel sekarang sudah ada)
echo "RESTRICTED" > kernel/status.lock
echo -e "\e[1;32m[SUCCESS] Akses Cloud Terputus. Sistem Terkunci Total.\e[0m"
