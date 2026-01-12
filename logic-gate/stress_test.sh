#!/bin/bash
# Day 21: Security System Stress Test (Simulation)

echo "--- INITIATING RED-TEAM SIMULATION ---"

# Test 1: Unauthorized Write Attempt on Core Assets (Day 18 Check)
echo "TEST 1: Attempting to inject malicious code into Core Assets..."
touch ~/arcana-ecosystem/core-assets/malware_test.txt 2>/dev/null

if [ $? -ne 0 ]; then
    echo "RESULT: [SUCCESS] Core-Assets are READ-ONLY. Day 18 Lockdown is holding."
else
    echo "RESULT: [FAILURE] Core-Assets were writable. Day 18 Security Breach."
fi

# Test 2: Search for 'Sensitive' data in the Decoy Chamber (Day 15 Check)
echo "TEST 2: Searching for financial keywords in decoys..."
grep "revenue" ~/arcana-ecosystem/vault-financial-records/q1_revenue_projections.md > /dev/null

if [ $? -eq 0 ]; then
    echo "RESULT: [SUCCESS] Intruder diverted to Decoy. Day 15 Mirage is effective."
else
    echo "RESULT: [FAILURE] Decoy data not found. Intruder might look elsewhere."
fi

# Test 3: Run Integrity Pulse to check for silent changes (Day 13 Check)
echo "TEST 3: Running Integrity Pulse..."
~/arcana-ecosystem/logic-gate/integrity_pulse.sh

echo "--- STRESS TEST COMPLETE ---"
