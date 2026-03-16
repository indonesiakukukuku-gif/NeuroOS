#!/bin/bash
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="neurosphere_backup_$TIMESTAMP.tar.gz"

echo "📂 Archiving NeuroSphere Assets..."
tar -czf $BACKUP_NAME core modules scripts logs *.py *.js *.sh *.txt

echo "✅ Backup Created: $BACKUP_NAME"
echo "🔐 Location: $(pwd)/$BACKUP_NAME"
