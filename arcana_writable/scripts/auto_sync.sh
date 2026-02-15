#!/bin/bash
# High-Frequency Sauna Sync
rclone sync ~/arcana-ecosystem/vault/sauna_protocol/ google:arcana_backup -P --transfers 16 --checkers 16 --drive-chunk-size 64M
echo "Sync Complete at $(date)" >> ~/sync_log.txt
