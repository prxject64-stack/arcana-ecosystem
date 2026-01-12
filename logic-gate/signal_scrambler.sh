#!/bin/bash
# Day 26: The Sauna Heat-Seal (Rotating Key Protocol)

TEMP_DIR=/dev/shm/arcana_noise
mkdir -p $TEMP_DIR

# Generate a unique key based on the current 10-minute window
# This ensures the key rotates every 600 seconds
ROTATING_KEY=$(date +%Y%m%d%H$(($(date +%M)/10)))
SECRET="12D_ARCANA_${ROTATING_KEY}"

# Generate the noise
dd if=/dev/urandom of=$TEMP_DIR/noise.tmp bs=1K count=$((1 + RANDOM % 5)) 2>/dev/null

# Encrypt with the rotating secret
echo "$SECRET" | gpg --batch --yes --passphrase-fd 0 --symmetric $TEMP_DIR/noise.tmp

# Move to outbound and clean up old signals
mv $TEMP_DIR/noise.tmp.gpg ~/arcana-ecosystem/outbound-signals/signal_$(date +%s).gpg
find ~/arcana-ecosystem/outbound-signals/ -name "signal_*" -mmin +5 -delete
rm -rf $TEMP_DIR
