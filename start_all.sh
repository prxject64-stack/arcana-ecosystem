#!/bin/bash
source ~/arcana-ecosystem/arcana_env/bin/activate
pkill -9 geth || true
# Explicitly clear stale IPC
rm -f arcana_data/geth.ipc

echo "Igniting G8 Xeon Core in Full-State Mode..."
# 1. Start the Node (Mining disabled initially for stability)
nohup geth --datadir arcana_data \
     --networkid 2026 \
     --http --http.addr "0.0.0.0" --http.api "eth,net,web3,miner,admin,personal" \
     --cache 4096 \
     --state.scheme path \
     --miner.etherbase "0xe7B7B6cC21D01e6120197f0413d224923243B69c" \
     --allow-insecure-unlock \
     --ipcpath arcana_data/geth.ipc \
     --verbosity 3 > arcana.log 2>&1 &

sleep 10

# 2. Check if IPC exists before attaching
if [ -S arcana_data/geth.ipc ]; then
    echo "Node stabilized. Activating Sealer..."
    # Now trigger mining and verify balance
    geth --datadir arcana_data attach arcana_data/geth.ipc --exec "miner.start(); console.log('CC-P Balance: ' + web3.fromWei(eth.getBalance('0xe7B7B6cC21D01e6120197f0413d224923243B69c'), 'ether') + ' CC-P')"
    echo "--- Arcana Sovereign System Online ---"
else
    echo "[CRITICAL] Geth failed to start Full-State. Check arcana.log for 'Fatal' errors."
    tail -n 20 arcana.log
fi
