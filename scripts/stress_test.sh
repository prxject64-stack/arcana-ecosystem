#!/bin/bash
for i in {1..4500}
do
   echo "Swap #$i starting..."
   cast send $AMM_ADDR "swapCCForUSD(uint256)" 100000000000000000000 \
     --unlocked --from 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266 --async
   
   if [ $((i % 100)) -eq 0 ]; then
     echo "Batch $i completed. Checking Sentinel status..."
     STATUS=$(cast call $AMM_ADDR "paused()(bool)")
     if [ "$STATUS" = "true" ]; then
       echo "!!! SENTINEL TRIGGERED AUTO-PAUSE AT SWAP $i !!!"
       exit 1
     fi
   fi
done
