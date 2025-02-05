#!/bin/sh
# Author: Kaushal Darji
# Purpose: Auto populate in error handling 
# Usage: ./regularexpression.sh

numString="12345678"
if [[ $numString =~ ^1.*8 ]]; then 
echo "$numString start with 1 adn 8 is present"
else 
echo "not present"
fi