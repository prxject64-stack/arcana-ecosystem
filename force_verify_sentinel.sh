#!/bin/bash
# Arcana Security System - Forced Verification Script
# Admin: 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266

echo "--- STEP 1: MINTING 20B TO ADMIN ---"
cast send $SAUSD_ADDR "mint(address,uint256)" 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266 20000000000000000000000000000 --unlocked --from 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266

echo "--- STEP 2: VERIFYING WALLET BALANCE ---"
BALANCE=$(cast call $SAUSD_ADDR "balanceOf(address)" 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266)
echo "Admin Balance: $BALANCE"

echo "--- STEP 3: APPROVING VAULT ---"
cast send $SAUSD_ADDR "approve(address,uint256)" $VAULT_ADDR 20000000000000000000000000000 --unlocked --from 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266

echo "--- STEP 4: DEPOSITING TO VAULT ---"
cast send $VAULT_ADDR "deposit(uint256,address)" 20000000000000000000000000000 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266 --unlocked --from 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266

echo "--- STEP 5: SIMULATING DRAIN (16B) ---"
cast send $VAULT_ADDR "withdraw(uint256,address,address)" 16000000000000000000000000000 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266 --unlocked --from 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266

echo "--- STEP 6: TRIGGERING SENTINEL ---"
cast send $SENTINEL_ADDR "monitorReserves()" --unlocked --from 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266

echo "--- FINAL STATUS: IS VAULT PAUSED? ---"
cast call $VAULT_ADDR "paused()(bool)"
