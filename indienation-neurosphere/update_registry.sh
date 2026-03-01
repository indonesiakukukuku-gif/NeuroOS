#!/bin/bash
# NeuroSphere Auto-Sync Aggregator
echo "🔄 Sinkronisasi Metadata Auralang ke Ledger..."

# Membuat file JSON pusat dari kumpulan file .aura
echo "{" > public/pioniere-registry.json
echo '  "system": "NeuroSphere",' >> public/pioniere-registry.json
echo '  "pioneers": [' >> public/pioniere-registry.json

FIRST=true
for file in identities/*.aura; do
    if [ "$FIRST" = true ]; then FIRST=false; else echo "," >> public/pioniere-registry.json; fi
    
    # Ekstraksi Nama dan IID dari file Auralang
    IID=$(grep -oP 'DEFINE IDENTITY "\K[^"]+' "$file" || grep -oP 'IID-\K[0-9]+' "$file" | head -1)
    HOLDER=$(grep -oP 'HOLDER: "\K[^"]+' "$file" | head -1)
    
    echo "    {\"iid\": \"$IID\", \"name\": \"$HOLDER\", \"status\": \"ANCHORED\"}" >> public/pioniere-registry.json
done

echo '  ]' >> public/pioniere-registry.json
echo "}" >> public/pioniere-registry.json

echo "✅ Ledger diperbarui berdasarkan folder identities/."
