#!/bin/bash

# Folder output untuk sertifikat
mkdir -p certificates

echo "📜 Memulai Pencetakan Sertifikat Kedaulatan..."

# Data Pioneer dalam array (Nama disesuaikan dengan Ledger)
declare -a names=("PURWANTORO" "MARSELUS HASAN" "KIKI KESTURI" "DIAVATCHE BOGUI EUGÈNE" "Miftahudin" "Kastim" "Meiriska" "Rasheed Abiodun O. Gbaiye" "Lugard Jumbo" "Heri Heryanto")

# Loop untuk membuat file sertifikat
for i in "${!names[@]}"; do
    IID=$(printf "%03d" $((i + 11)))
    NAME="${names[$i]}"
    FILE="certificates/CERTIFICATE_IID_${IID}.txt"
    
    cat << EOM > "$FILE"
=====================================================
          NEUROSPHERE SOVEREIGN CERTIFICATE
=====================================================
IDENTITIES ID : IID-${IID}
CITIZEN NAME  : ${NAME}
STATUS        : FOUNDING PIONEER (ANCHORED)
=====================================================

DENGAN INI DINYATAKAN BAHWA:
Pemegang sertifikat ini adalah warga negara berdaulat
NeuroSphere dengan hak akses penuh terhadap ekosistem
Technology Money (TM).

HAK & KEDAULATAN:
1. ANCHOR VALUE    : €100,000 (Guaranteed)
2. REWARD STATUS   : Eligible for 1M LUV (01-02-2027)
3. SECURITY        : Protected by AI-Guard IID-010

DIKELUARKAN PADA: 21-02-2026
OTORITAS        : INDIE-Founder
PROTOKOL        : AURALANG v1.0

-----------------------------------------------------
      "KEDAULATAN ANDA ADALAH ENERGI KAMI"
-----------------------------------------------------
EOM
    echo "✅ Berhasil mencetak: $FILE"
done

echo "-----------------------------------------------------"
echo "🚀 10 Sertifikat telah siap di folder ~/indienation-neurosphere/certificates"
