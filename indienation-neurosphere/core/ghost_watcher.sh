#!/bin/bash
# @authority: IID-021+
# @purpose: Auto-Recovery for Sentinel Daemon (S29)

PID_FILE=~/indienation-neurosphere/core/sentinel.pid
LOG_FILE=~/indienation-neurosphere/core/sovereign_audit.log

echo "[GHOST] Immunity Layer Activated. Monitoring Sentinel..."

while true; do
    if [ -f $PID_FILE ]; then
        SPID=$(cat $PID_FILE)
        if ! ps -p $SPID > /dev/null; then
            echo "[$(date '+%Y-%m-%d %H:%M:%S')] ⚠️ ALERT: Sentinel Dead. Recovering..." >> $LOG_FILE
            nohup python3 ~/indienation-neurosphere/core/sentinel_daemon.py > /dev/null 2>&1 &
            sleep 2
            echo "[$(date '+%Y-%m-%d %H:%M:%S')] ✅ RECOVERY: Sentinel Restarted." >> $LOG_FILE
        fi
    else
        nohup python3 ~/indienation-neurosphere/core/sentinel_daemon.py > /dev/null 2>&1 &
    fi
    sleep 5
done
