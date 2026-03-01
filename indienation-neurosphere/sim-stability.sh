#!/bin/bash
# NEUROSPHERE STABILITY SIMULATION
# Testing AI-Guard Validation Accuracy

echo "------------------------------------------------"
echo "INITIATING 24-HOUR STABILITY SIMULATION..."
echo "TARGET: 100 RANDOM ACTS OF KINDNESS"
echo "------------------------------------------------"

for i in {1..100}
do
   # Randomize Empathy Score (0.0 to 1.0)
   SCORE=$(awk -v min=0 -v max=100 'BEGIN{srand(); print (min+rand()*(max-min))/100}')
   CITIZEN="IID-$(($RANDOM % 1000 + 21))"
   
   if (( $(echo "$SCORE >= 0.4" | bc -l) )); then
      STATUS="[\033[0;32mVALIDATED\033[0m]"
      REWARD=$(echo "$SCORE * 10" | bc | cut -d'.' -f1)
      echo -e "$STATUS Citizen $CITIZEN | Score: $SCORE | Reward: $REWARD LUV"
   else
      STATUS="[\033[0;31mREJECTED\033[0m]"
      echo -e "$STATUS Citizen $CITIZEN | Score: $SCORE | Action: Sent to Appeal"
   fi
   # Mimic processing time
   sleep 0.1 
done

echo "------------------------------------------------"
echo "SIMULATION COMPLETE: AI-GUARD STABLE"
echo "------------------------------------------------"
