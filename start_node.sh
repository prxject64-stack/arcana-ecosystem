#!/bin/bash
geth --datadir ./node_data \
  --networkid 136 \
  --mine \
  --miner.etherbase "0x218e8c79F8a12472a4bA48dd76B55A3e39e40cc8" \
  --unlock "0x218e8c79F8a12472a4bA48dd76B55A3e39e40cc8" \
  --password password.txt \
  --allow-insecure-unlock \
  --http --http.addr "127.0.0.1" --http.port 8545 --http.corsdomain "*" \
  --nodiscover
