#!/bin/sh
# Author: Kaushal Darji
# Purpose: backup of file 
# Usage: ./automatesoftinstall.sh

if command -v apt > /dev/null; then
    sudo apt update && sudo apt install -y "$@"
elif command -v yum > /dev/null; then
    sudo yum install -y "$@"
else
    echo "Unsupported package manager"
fi
