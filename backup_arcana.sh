#!/bin/bash
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="arcana_sovereign_backup_$TIMESTAMP.tar.gz"

echo "--- STARTING SYSTEM ARCHIVE ---"

# Create a temporary directory for the backup
mkdir -p ./backups/$TIMESTAMP

# Copy Smart Contracts and Build Artifacts
cp -r ./contracts ./backups/$TIMESTAMP/
cp *.js ./backups/$TIMESTAMP/

# Copy the Geth Keystore (Contains your encrypted Private Keys)
cp -r ./data/keystore ./backups/$TIMESTAMP/

# Create the compressed archive
tar -czf $BACKUP_NAME -C ./backups/$TIMESTAMP .

echo "--- BACKUP COMPLETE ---"
echo "Archive File: $BACKUP_NAME"
echo "CRITICAL: Move this file to a secure, off-site location (USB, Cold Storage)."
