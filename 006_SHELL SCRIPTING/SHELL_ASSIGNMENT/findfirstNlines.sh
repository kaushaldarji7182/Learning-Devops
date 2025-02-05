#!/bin/sh
# Author: Kaushal Darji
# Purpose: backup of file 
# Usage: ./findfirstNlines.sh

read -p "Enter file name: " file
head -n 10 "$file"
