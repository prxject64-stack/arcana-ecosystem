#!/bin/bash
echo "Initiating 10-Block Wealth Pulse..."
for i in {1..10}
do
   echo "Mining Block $i..."
   curl -s http://127.0.0.1:5000/mine
   echo -e "\n----------------------------"
   sleep 1
done
echo "Pulse Complete. 500 Arcana secured to Architect Wallet."
