#!/bin/bash
nohup geth --datadir arcana_data \
     --networkid 136 \
     --http --http.addr "0.0.0.0" --http.api "eth,net,web3,personal,admin,clique,miner" \
     --allow-insecure-unlock \
     --unlock "0xC4BBB118aCc45f1Be50De724f1757b1A19E19De3" \
     --password passwords.txt \
     --mine --miner.etherbase "0xC4BBB118aCc45f1Be50De724f1757b1A19E19De3" \
     > arcana.log 2>&1 &
echo "Arcana Sovereign Node Started."
