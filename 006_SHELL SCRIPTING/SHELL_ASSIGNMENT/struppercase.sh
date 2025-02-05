#!/bin/sh
# Author: Kaushal Darji
# Purpose: converting string lower to upper 
# Usage: ./struppercase.sh


echo "enter String"
read -r str
#read -p "Enter a string: " str (another way to read input)
echo "$str" | tr '[:lower:]' '[:upper:]'