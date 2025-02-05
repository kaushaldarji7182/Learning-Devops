#!/bin/sh
# Author: Kaushal Darji
# Purpose: backup of file 
# Usage: ./removeduplicateline.sh

read -p "Enter file name: " file
sort "$file" | uniq > temp && mv temp "$file"
