#!/bin/bash
geth --datadir /home/ubuntu/arcana_data \
--networkid 2026 \
--mine \
--miner.etherbase "0x14A3256052c02f9d87FE1Cc3b712D4530061b25c" \
--unlock "0x14A3256052c02f9d87FE1Cc3b712D4530061b25c" \
--password /home/ubuntu/miner_pass.txt \
--allow-insecure-unlock \
--nodiscover \
--http \
--http.api "eth,net,web3,personal,miner,clique" \
--miner.gaslimit 80000000
