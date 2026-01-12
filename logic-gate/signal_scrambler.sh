#!/bin/bash
# Day 23: Signal-to-Noise Optimizer (RAM-Disk Protocol)

# Use Shared Memory (RAM) to avoid Disk Space issues
TEMP_DIR=/dev/shm/arcana_noise
mkdir -p $TEMP_DIR

# Generate chatter in RAM
dd if=/dev/urandom of=$TEMP_DIR/noise.tmp bs=1K count=$((1 + RANDOM % 5)) 2>/dev/null
gpg --batch --yes --symmetric --passphrase "12thDimensionSuccess" $TEMP_DIR/noise.tmp

# Send signal to the outbound-signals folder (Disk) only briefly
mv $TEMP_DIR/noise.tmp.gpg ~/arcana-ecosystem/outbound-signals/signal_$(date +%s).gpg

# Immediate cleanup of old signals to maintain 968M space
find ~/arcana-ecosystem/outbound-signals/ -name "signal_*" -mmin +2 -delete
rm -rf $TEMP_DIR
