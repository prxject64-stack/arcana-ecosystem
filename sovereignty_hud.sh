#!/bin/bash
# Arcana Sovereignty HUD - Android/Termux Edition
while true; do
    clear
    echo -e "\e[1;34m================================================\e[0m"
    echo -e "\e[1;33m   ARCANA SOVEREIGNTY HUD - $(date +'%Y-%m-%d')\e[0m"
    echo -e "\e[1;34m================================================\e[0m"
    
    # Process Priority Stats
    TARGET_PID=$(pgrep -f "mining" | head -n 1)
    if [ ! -z "$TARGET_PID" ]; then
        NI_VAL=$(ps -o ni= -p $TARGET_PID)
        CPU_VAL=$(ps -o %cpu= -p $TARGET_PID)
        echo -e " DAEMON STATUS:   \e[1;32mACTIVE (PID: $TARGET_PID)\e[0m"
        echo -e " PRIORITY LEVEL:  \e[1;35m$NI_VAL (MAX OVERDRIVE)\e[0m"
        echo -e " CPU LOAD:        $CPU_VAL%"
    else
        echo -e " DAEMON STATUS:   \e[1;31mOFFLINE\e[0m"
    fi
    
    echo -e "\e[1;34m------------------------------------------------\e[0m"
    
    # Financial Milestone from Golden Record
    TOTAL_CC=$(grep "Mined" ~/arcana-ecosystem/vault-financial-records/golden_record.arcana | wc -l | awk '{print $1 * 1000000 + 415000000000}')
    echo -e " GROSS ASSETS:     \e[1;32m$TOTAL_CC CC\e[0m"
    echo -e " 12D-ALIGNMENT:    CONNECTED"
    
    echo -e "\e[1;34m================================================\e[0m"
    echo " (Ctrl+C to exit HUD)"
    sleep 5
done
