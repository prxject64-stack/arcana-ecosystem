#!/bin/bash
# Sovereign Bridge Persistence - Feb 20, 2026
BRAIN="18.221.3.50:11434"

while true; do
  if curl -s --connect-timeout 2 http://$BRAIN/api/tags > /dev/null; then
    echo "[$(date)] Bridge Stable. Processing 4,500 Swaps..."
  else
    echo "[$(date)] BRAIN DISCONNECTED. Attempting emergency reconnection..."
    systemctl restart vampire-scout
  fi
  sleep 60
done
