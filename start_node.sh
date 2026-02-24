#!/bin/bash
nohup geth --datadir /root/arcana-ecosystem/arcana_data \
--networkid 136 \
--http --http.api eth,net,web3,miner,admin \
--cache 4096 \
--allow-insecure-unlock > g8_osaka_reboot.log 2>&1 &
