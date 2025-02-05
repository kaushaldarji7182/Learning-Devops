#!/bin/sh
# Author: Kaushal Darji
# Purpose: backup of file 
# Usage: ./f&rmultipleword.sh

read -p "Enter word to replace: " old
read -p "Enter new word: " new
find . -type f -exec sed -i "s/$old/$new/g" {} +
