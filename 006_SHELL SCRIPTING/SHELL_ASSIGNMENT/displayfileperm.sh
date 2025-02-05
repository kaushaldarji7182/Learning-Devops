#!/bin/sh
# Author: Kaushal Darji
# Purpose: backup of file 
# Usage: ./displayfileperm.sh

read -p "Enter file name: " file
ls -l "$file" | awk '{print $1}'
