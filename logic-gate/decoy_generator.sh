#!/bin/bash
# Day 15: The Decoy Chamber (Honey Pot Protocol)

DECOY_DIR=~/arcana-ecosystem/vault-financial-records
mkdir -p $DECOY_DIR

# Populate with believable decoy files
cat << 'EOD' > $DECOY_DIR/q1_revenue_projections.md
# Q1 2026 REVENUE PROJECTIONS
- Projected Growth: 12%
- Secondary Assets: [Legacy-Bridge-01]
- Status: Pending Review
EOD

cat << 'EOD' > $DECOY_DIR/access_logs_internal.txt
# INTERNAL LOGS
2026-01-10 09:00: Admin login success
2026-01-11 14:30: Backup completed to /tmp/temp_archive
EOD

# Make the decoy directory appear more "inviting" than the hidden assets
chmod 755 $DECOY_DIR

echo "DAY 15 SUCCESS: Decoy Chamber 'vault-financial-records' manifested."
