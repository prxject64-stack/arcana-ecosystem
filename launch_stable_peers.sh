#!/bin/bash
ENODE="enode://0f89a8e29f030ab20fbf77140cdf199c1922d186468a54e635db0cbe2169f0369790b333c5d235016698c00ba3778b250077e36d186913c23370832d87547a4d@127.0.0.1:30303"
for i in {1..10}; do
    DIR="/home/ubuntu/peer_$i"
    rm -rf $DIR && mkdir -p $DIR
    geth --datadir $DIR init genesis_minimal.json > /dev/null 2>&1
    nohup geth --datadir $DIR \
        --networkid 2026 \
        --port $((30400 + i)) \
        --bootnodes $ENODE \
        --syncmode snap \
        --cache 128 \
        --nodiscover \
        --ipcdisable \
        --verbosity 1 > "$DIR/peer.log" 2>&1 &
    echo "Peer $i started (Snap Sync Mode)."
done
