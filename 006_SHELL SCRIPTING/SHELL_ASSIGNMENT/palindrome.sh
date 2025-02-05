#!/bin/sh
# Author: Kaushal Darji
# Purpose: Palindrome of an string
# Usage: ./palindrome.sh


read -p "Enter a string: " str
len=${#str}
rev_str=""

for (( i=len-1; i>=0; i-- )); do
    rev_str="$rev_str${str:i:1}"
done

if [[ "$str" == "$rev_str" ]]; then
    echo "Palindrome"
else
    echo "Not a palindrome"
fi
