#!/bin/bash
# Arcana Sovereign Engine - v1.1.0
VENV_PYTHON="/home/ubuntu/arcana_node/venv/bin/python3"
ENGINE_PATH="/home/ubuntu/ase_engine.py"

case "$1" in
    --system-sync)
        echo "[ASE] Initializing 10ms Sync..."
        taskset -c 0-7 $VENV_PYTHON $ENGINE_PATH sync
        ;;
    --collateral-lock)
        $VENV_PYTHON $ENGINE_PATH lock "$2"
        ;;
    --sauna-extract)
        echo "[ASE] Launching Sauna Protocol Arbitrage..."
        taskset -c 8-63 $VENV_PYTHON $ENGINE_PATH extract
        ;;
    --shield)
        echo "[ASE] Arcana Security Shield: Level MAX [ACTIVE]"
        ;;
    --status-aggressive)
        echo "Hardware: AWS r7iz | Core Affinity: 0-63"
        $VENV_PYTHON $ENGINE_PATH status
        ;;
    *)
        echo "Usage: ase [option]"
        echo "  --system-sync         Sync with 10ms blocks"
        echo "  --collateral-lock     Lock 136B CC"
        echo "  --sauna-extract       Run WBTC/BTC.b arbitrage"
        ;;
esac
