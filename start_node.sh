#!/bin/bash
geth --datadir ./node_data \
  --networkid 136 \
  --mine \
  --miner.etherbase "0x4654cfdd1a9eaeaa43c985d5dfda6b4297a1e688" \
  --unlock "0x4654cfdd1a9eaeaa43c985d5dfda6b4297a1e688" \
  --password password.txt \
  --http --http.api "eth,net,web3,personal,miner" \
  --allow-insecure-unlock \
  --nodiscover \
  --cache 2048
