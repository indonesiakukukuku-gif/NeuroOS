#!/bin/bash
echo "[$(date)] >>> INITIALIZING PULSE CYCLE <<<"

# 1. Update Metadata & Aura (Logic Only)
# (Bagian ini tetap menjaga angka €100.000 dan Aura Abang)

# 2. Persiapan Folder Deployment
rm -rf public_tmp && mkdir -p public_tmp

# 3. MENGATUR POSISI LAYER (SINKRONISASI KRUSIAL)
# Kita tidak lagi menimpa index dengan dashboard lama
cp access.html public_tmp/index.html
cp authority.html public_tmp/authority.html
cp wallet.html public_tmp/wallet.html
cp investment.html signup.html signin.html public_tmp/investment.html
cp inheritance.html public_tmp/inheritance.html
cp indiescan.html public_tmp/indiescan.html

# 4. Copy data pendukung (Certificates & API)
mkdir -p public_tmp/certificates
cp certificates/*.txt public_tmp/certificates/ 2>/dev/null || :
cp system_status.json public_tmp/ 2>/dev/null || :

# 5. Eksekusi Deploy ke Firebase
rm -rf public && mv public_tmp public
firebase deploy --only hosting

echo "[$(date)] >>> PULSE CYCLE COMPLETED SUCCESSFULLY <<<"
