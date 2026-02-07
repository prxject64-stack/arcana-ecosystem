#!/bin/bash
# Arcana Sovereign Quick Swap Utility - Sauna Protocol v1.0
AMOUNT=$1
if [ -z "$AMOUNT" ]; then AMOUNT=100; fi

EXECUTOR=0x8eeC5Bce2fd5b4526EFFA61b7Ee890f3E0E4A87B
CC_TOKEN=0x8847E51E89A609D2D11Dc10020991A29D500ABf0
DESTINATION=0x7BfBFCAcEda78A54Fa0C6CAD236AB5a6c11B7a29
RPC="http://localhost:8547"
GOD_PRIV=93fdaa6afd2c665f9dedf7dd3e2ad0f1949719008740d3c03cf86233b9b68cb4

echo "Initiating swap of $AMOUNT CC via God-Key..."
cast send --private-key $GOD_PRIV \
  $EXECUTOR \
  "executeSwap(address,address,uint256)" \
  $CC_TOKEN \
  $DESTINATION \
  $AMOUNT \
  --rpc-url $RPC
