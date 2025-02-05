#!/bin/sh
# Author: Kaushal Darji
# Purpose: Auto populate in error handling 
# Usage: ./regularexpression.sh

echo "Marks Calculator"

# Read marks
echo "Enter Maths marks: "
read -r marks1
echo "Enter Science marks: "
read -r marks2
echo "Enter English marks: "
read -r marks3

# Calculate total and average (use $(( ... )) for arithmetic in shell)
total=$((marks1 + marks2 + marks3))
average=$((total / 3))

# Display results
echo "Total Marks: $total"
echo "Average Marks: $average"

# Determine Grade
if [ "$average" -lt 30 ]; then
    echo "Result: Fail "
elif [ "$average" -ge 30 ] && [ "$average" -lt 45 ]; then
    echo "Result: C Distinction"
elif [ "$average" -ge 45 ] && [ "$average" -lt 60 ]; then
    echo "Result: Mid-Level Distinction"
elif [ "$average" -ge 60 ] && [ "$average" -lt 80 ]; then
    echo "Result: Very Good"
elif [ "$average" -ge 80 ] && [ "$average" -le 100 ]; then
    echo "Result: Excellent "
else
    echo "Invalid marks entered!"
fi
