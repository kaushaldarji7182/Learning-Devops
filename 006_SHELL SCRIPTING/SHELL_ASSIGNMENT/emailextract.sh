#!/bin/sh
# Author: Kaushal Darji
# Purpose: word replace
# Usage: ./emailextract.sh

read -p "Enter file name: " file
grep -oE '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' "$file"
