#!/bin/sh
# Author: Kaushal Darji
# Purpose: Linux in shell with command parameter
# Usage: ./linuxparamcomment.sh



hour=$(date +%H)
echo "Right now time is $hour"

if [ "$hour" -lt 12 ]; then
    echo "Good Morning"
elif [ "$hour" -lt 16 ]; then
    echo "Good Afternoon"
elif [ "$hour" -lt 20 ]; then
    echo "Good Evening"
else
    echo "Good Night"
fi
