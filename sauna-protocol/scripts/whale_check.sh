#!/bin/bash
ADDRESSES=("0xCA8Fa8f0b631EcdB18Cda619C4Fc9d197c8aFfCa" "0xE92d1A43df510F82C66382592a047d288f85226f" "0x5fd79d46eba7f351fe49bff9e87cdea6c821ef9f")
SUSD="0x8c6f28f2f1a3c87f0f938b96d27520d9751ec8d9"
RPC="https://mainnet.optimism.io"

for addr in "${ADDRESSES[@]}"; do
    echo "Checking $addr..."
    cast call $SUSD "balanceOf(address)(uint256)" $addr --rpc-url $RPC
done
