#!/bin/sh
# Author: Kaushal Darji
# Purpose: backup of file 
# Usage: ./Append.sh

read -p "Enter file name: " file
read -p "Enter text to append: " text
echo "$text" >> "$file"
