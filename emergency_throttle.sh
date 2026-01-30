#!/bin/bash
miner --provision-gate --id AMAZON_HQ_01 --limit 500 --priority high
echo "[ALERT] Amazon Gate throttled to 500/s due to liquidity spike."
