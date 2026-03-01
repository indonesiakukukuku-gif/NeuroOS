#!/bin/bash
# [Neuro-Guard] IDENTITY VERIFICATION PROTOCOL

echo -e "\e[1;36m[Identity] Memulai Verifikasi Kredensial Cloud Gate...\e[0m"

# 1. Cek Konektivitas ke API GitHub (Tanpa mengekspos KEYS ke log)
STATUS_CODE=$(curl -s -o /dev/null -I -w "%{http_code}" -H "Authorization: token $(git config --get credential.helper > /dev/null && git push --dry-run 2>&1 | grep -o 'ghp_[a-zA-Z0-9]*')" https://api.github.com/user)

# 2. Logika Verifikasi Berbasis Token
if git ls-remote origin &>/dev/null; then
    echo -e "\e[1;32m[SUCCESS] Identitas INDIE-Founder Terverifikasi.\e[0m"
    echo -e "\e[1;33m[Status] Token Aktif | Node: LX-4-ALPHA-01\e[0m"
    exit 0
else
    echo -e "\e[1;31m[CRITICAL] Kegagalan Autentikasi: Token Tidak Valid atau Expired.\e[0m"
    echo -e "\e[1;33m[Action] Jalankan 'panic_lock.sh' jika ini bukan tindakan Anda.\e[0m"
    exit 1
fi
