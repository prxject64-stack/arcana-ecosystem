#!/bin/bash
RPC="http://127.0.0.1:8545"
PK="0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"
CC_P="0x5FbDB2315678afecb367f032d93F642f64180aa3"
SA_USD="0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512"

forge create src/ArcanaAMMV2.sol:ArcanaAMMV2 \
  --constructor-args $CC_P $SA_USD \
  --rpc-url $RPC \
  --private-key $PK \
  --gas-limit 5000000
