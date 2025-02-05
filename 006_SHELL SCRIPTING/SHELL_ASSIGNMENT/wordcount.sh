#!/bin/sh
# Author: Kaushal Darji
# Purpose: word count in string
# Usage: ./wordcount.sh


read -p "Enter a string: " str
echo "Word count: $(echo "$str" | wc -w)"
