#!/bin/bash
RPC="http://127.0.0.1:8545"
CC_TOKEN="0x261D8c5e9742e6f7f1076Fa1F560894524e19cad"
TREASURY="0x90F79bf6EB2c4f870365E785982E1f101E93b906"
AMOUNT="1000000000000000000000" # 1,000 CC
COUNT=4500

echo "Initiating 4,500 CC Liquidity Swaps..."

# Impersonate Treasury for the batch
cast rpc anvil_impersonateAccount $TREASURY --rpc-url $RPC

for i in $(seq 1 $COUNT); do
    # Generate address using openssl/cast (bypass cast wallet new issues)
    PEER=$(openssl rand -hex 20 | sed 's/^/0x/')
    
    # Execute CC Transfer
    cast send $CC_TOKEN "transfer(address,uint256)" $PEER $AMOUNT \
    --rpc-url $RPC --from $TREASURY --unlocked --async > /dev/null
    
    if [ $((i % 100)) -eq 0 ]; then
        echo "Sent $i / $COUNT swaps..."
    fi
done

cast rpc anvil_stopImpersonatingAccount $TREASURY --rpc-url $RPC
echo "Stress Test Complete. 4.5M CC Circulated to 4,500 Peers."
