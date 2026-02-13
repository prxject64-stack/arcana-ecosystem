#!/bin/bash
ENODE="enode://0f89a8e29f030ab20fbf77140cdf199c1922d186468a54e635db0cbe2169f0369790b333c5d235016698c00ba3778b250077e36d186913c23370832d87547a4d@127.0.0.1:30303"
for i in {1..100}; do
    DIR="/tmp/peer_$i"
    mkdir -p $DIR
    # Use the EXACT same genesis you used for the 136B CC vault
    geth --datadir $DIR init genesis_minimal.json > /dev/null 2>&1
    # Launch with syncmode full to ensure they validate the Clique headers
    nohup geth --datadir $DIR --networkid 2026 --port $((30303 + i)) --bootnodes $ENODE --syncmode full --nodiscover --ipcdisable --verbosity 1 > "$DIR/peer.log" 2>&1 &
    echo "Peer $i online (Consensus: Clique)."
done
