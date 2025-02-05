#!/bin/bash
# Author: Kaushal Darji
# Purpose: Learning while loop
# Usage: ./multiply_while.sh

echo "Enter the marks"
read -r mk

if [ "$mk" -le 20 ]; then
    echo "fail"
elif [ "$mk" -gt 20 ] && [ "$mk" -le 40 ]; then
    echo "pass with C grade"
elif [ "$mk" -gt 40 ] && [ "$mk" -le 80 ]; then
    echo "pass with B grade"
else
    echo "pass with A grade"
fi
