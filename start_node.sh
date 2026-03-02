#!/bin/bash
geth --datadir ./node_data --networkid 136 --cache 2048 --http --http.addr "127.0.0.1" --mine --miner.threads 1 --allow-insecure-unlock --unlock "0x4654cfdd1a9eaeaa43c985d5dfda6b4297a1e688" --password password.txt
