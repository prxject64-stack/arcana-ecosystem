#!/bin/bash
# Arcana Sovereign Dashboard - v1.0 (Feb 20, 2026)

while true; do
    clear
    echo "==============================================================="
    echo "        ARCANA SOVEREIGN - VAMPIRE SCOUT DASHBOARD            "
    echo "==============================================================="
    echo "  NODE: Linode G8 (The Hands) | BRAIN: AWS r7i (18.221.3.50)  "
    echo "---------------------------------------------------------------"

    # System Health
    CPU=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1"%"}')
    RAM=$(free -m | awk '/Mem:/ { printf("%3.1f%%", $3/$2*100) }')
    echo "  [HEALTH] CPU: $CPU | RAM: $RAM | DISK: $(df -h / | awk 'NR==2 {print $5}')"

    # Bot Status
    STATUS=$(systemctl is-active arcana-bot)
    echo "  [STATUS] Vampire Scout Service: $STATUS"

    # Swap Intelligence (Parsed from Logs)
    VERIFIED=$(grep -c "SUCCESS" /var/log/arcana-bot.log 2>/dev/null || echo "0")
    FAILED=$(grep -c "ERROR" /var/log/arcana-bot.log 2>/dev/null || echo "0")
    echo "  [SWAPS]  Verified Whales: $VERIFIED | Verification Failures: $FAILED"
    echo "  [TARGET] Progress: $(echo "scale=2; ($VERIFIED/4500)*100" | bc 2>/dev/null || echo "0")% of 4,500 Goal"

    echo "---------------------------------------------------------------"
    echo "  LATEST LOG ENTRIES:"
    tail -n 5 /var/log/arcana-bot.log | awk '{print "  > " $0}'

    echo "---------------------------------------------------------------"
    echo "  [ESC] to exit dashboard | Refresh Rate: 5s"
    sleep 5
done
