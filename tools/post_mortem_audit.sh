#!/bin/bash
echo "--- Obsidian Layer: Post-Mortem Data Extraction ---"
echo "Target: AMAZON_HQ_01 | Log: /var/log/miner_gate.log"
echo "---------------------------------------------------"

# Scrape for the 'CRITICAL' flag
grep "CRITICAL" /var/log/miner_gate.log 2>/dev/null | tail -n 5 || echo "No critical events found."

# Calculate the Peak TPS
PEAK_TPS=$(grep "TPS" /var/log/miner_gate.log 2>/dev/null | awk '{print $NF}' | sort -nr | head -n 1)
echo "Peak Throughput Detected: ${PEAK_TPS:-0} TPS"

# Check Vault Status
VAULT_SNAPSHOT=$(sec-sys --check-vault --asset CC --silent)
echo "Vault Integrity Post-Incident: $VAULT_SNAPSHOT"
