#!/bin/bash
// Auralang Guard Logic
// Founder: INDIE-Founder [cite: 2026-01-29]

echo "--- [NEUROOS PRE-PUSH SCAN] ---"

# Mencari file JSON yang tidak sengaja masuk ke staging area
STAGED_JSON=$(git diff --cached --name-only | grep ".json")

if [ ! -z "$STAGED_JSON" ]; then
    echo "🚨 ALERT: SENSITIVE JSON DETECTED: $STAGED_JSON"
    echo "❌ ABORTING PUSH: Kedaulatan Terancam. Hapus file sensitif sebelum push."
    exit 1
fi

echo "✅ SCAN CLEAR: No sensitive metadata found. Proceeding..."
exit 0
