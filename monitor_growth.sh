#!/bin/bash
echo "------------------------------------------------"
echo "TRUSTSTACK AI: SOVEREIGN REVENUE MONITOR (2026)"
echo "------------------------------------------------"

# 1. Check total number of active clients
CLIENT_COUNT=$(aws dynamodb scan --table-name TrustStack_Clients --select "COUNT" --query "Count" --output text)
REVENUE=$((CLIENT_COUNT * 5000))

echo "Total Active Clients: $CLIENT_COUNT"
echo "Monthly Recurring Revenue (MRR): $${REVENUE}"
echo "------------------------------------------------"
echo "LATEST CLIENT REGISTRATIONS:"
aws dynamodb scan --table-name TrustStack_Clients --query "Items[].[client_id, status, plan]" --output table
echo "------------------------------------------------"
