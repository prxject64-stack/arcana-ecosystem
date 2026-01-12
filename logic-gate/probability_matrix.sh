#!/bin/bash
# Phase 2, Day 25: Trade-Probability-Matrix (Confidence Scoring Protocol)

SENTIMENT_FILE="/dev/shm/resonance_sentiment"
VALIDATION_STATE="/dev/shm/validation_state"
OUTPUT_SCORE="/dev/shm/matrix_confidence"

# Default values
SENTIMENT=0
[[ -f "$SENTIMENT_FILE" ]] && SENTIMENT=$(cat "$SENTIMENT_FILE")
VALID=$(cat "$VALIDATION_STATE" 2>/dev/null || echo "0")

echo "--- CALCULATING PROBABILITY MATRIX ---"

# 12D Logic: Combine Sentiment (vibe) with Validation (truth)
# Base Score starts at 0.5
SCORE=0.5

# Adjust based on Sentiment (Day 11)
if [ "$SENTIMENT" -gt 5 ]; then SCORE=$(echo "$SCORE + 0.3" | bc); fi
if [ "$SENTIMENT" -lt -5 ]; then SCORE=$(echo "$SCORE - 0.3" | bc); fi

# Adjust based on Validation (Day 23)
if [ "$VALID" -eq 1 ]; then SCORE=$(echo "$SCORE + 0.2" | bc); fi

# Final Boundary Control
if (( $(echo "$SCORE > 1.0" | bc -l) )); then SCORE=1.0; fi
if (( $(echo "$SCORE < 0.0" | bc -l) )); then SCORE=0.0; fi

echo "$SCORE" > "$OUTPUT_SCORE"
echo "Matrix Confidence: $SCORE"

# Decision Gate: Threshold 0.7
if (( $(echo "$SCORE >= 0.7" | bc -l) )); then
    echo "PROBABILITY HIGH: Signal permitted for 10,000,000 CC path."
    echo "1" > /dev/shm/matrix_gate
else
    echo "PROBABILITY LOW: Signal suppressed as Entropy."
    echo "0" > /dev/shm/matrix_gate
fi
