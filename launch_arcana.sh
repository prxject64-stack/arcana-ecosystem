#!/bin/bash
echo "--- ARCANA ECOSYSTEM BOOT SEQUENCE ---"

# 1. Kill any ghost processes
echo "[1/4] Clearing background ghosts..."
sudo pkill -f ngrok 2>/dev/null
sudo fuser -k 5000/tcp 2>/dev/null

# 2. Activate Virtual Environment
echo "[2/4] Grounding Virtual Environment..."
source venv/bin/activate

# 3. Start the Core in the background
echo "[3/4] Igniting Arcana Core..."
nohup python3 arcana_core.py > core.log 2>&1 &
sleep 2

# 4. Start the Global Gateway
echo "[4/4] Opening Ngrok Tunnel..."
echo "------------------------------------"
ngrok http 5000
