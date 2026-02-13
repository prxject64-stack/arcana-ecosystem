#!/bin/bash
ENODE="enode://0f89a8e29f030ab20fbf77140cdf199c1922d186468a54e635db0cbe2169f0369790b333c5d235016698c00ba3778b250077e36d186913c23370832d87547a4d@18.221.3.50:30303"
for i in {1..100}; do
    DIR="/tmp/peer_$i"
    mkdir -p $DIR
    geth --datadir $DIR init genesis_minimal.json > /dev/null 2>&1
    nohup geth --datadir $DIR --networkid 2026 --port $((30303 + i)) --bootnodes $ENODE --ipcdisable --maxpeers 1 --nodiscover --verbosity 1 > "$DIR/peer.log" 2>&1 &
    echo "Peer $i online."
done
