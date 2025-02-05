#!/bin/sh
# Author: Kaushal Darji
# Purpose: word replace
# Usage: ./wordreplace.sh


read -p "Enter file name: " file
read -p "Enter word to replace: " old
read -p "Enter new word: " new
sed -i "s/$old/$new/g" "$file"
