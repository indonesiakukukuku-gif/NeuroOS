#!/bin/bash
if ! ps aux | grep -v grep | grep "core/sentinel.py" > /dev/null
then
    echo "⚠️ Sentinel down! Restarting..." >> logs/sentinel.log
    auralang core/sentinel.py >> logs/sentinel.log 2>&1 &
fi
