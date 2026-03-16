#!/bin/bash
DB_PATH=~/indienation-neurosphere/core/neuro_registry.db
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Register Task ke SQLite
sqlite3 $DB_PATH "INSERT INTO tasks (command, sector_id, status, created_at) VALUES ('ARGI_ECONOMY_CYCLE', 17, 'PENDING', '$TIMESTAMP');"

echo "🚀 [KERNEL] Task Registered: ARGI_ECONOMY_CYCLE (ID: $(sqlite3 $DB_PATH 'SELECT last_insert_rowid();'))"
echo "🧠 [ARGI] Orchestrating S6, S17, and S25..."

# Trigger Real Worker (Python)
python3 ~/indienation-neurosphere/core/argi_worker.py
