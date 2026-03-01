#!/bin/bash
OUTPUT_DIR="~/indienation-neurosphere/public/identity-qrs"
echo -e "\n[NEUROLANG]: Membangun Identitas Visual Pioneer..."

PIONEERS=(
"IID-2026-000000011" "IID-2026-000000012" "IID-2026-000000013"
"IID-2026-000000014" "IID-2026-000000015" "IID-2026-000000016"
"IID-2026-000000017" "IID-2026-000000018" "IID-2026-000000019"
"IID-2026-000000020"
)

for iid in "${PIONEERS[@]}"
do
    # Membuat QR Code dengan level koreksi tinggi (H) agar mudah di-scan meski layar HP kusam
    qrencode -t PNG -o ~/indienation-neurosphere/public/identity-qrs/${iid}.png "$iid"
    echo "[✔] Generated: ${iid}.png"
done

echo -e "\n[SYSTEM]: 10 Paspor Digital siap di ~/indienation-neurosphere/public/identity-qrs/\n"
