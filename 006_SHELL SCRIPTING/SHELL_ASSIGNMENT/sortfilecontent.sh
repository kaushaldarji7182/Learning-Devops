#!/bin/sh
# Author: Kaushal Darji
# Purpose: backup of file 
# Usage: ./sortfilecontent.sh

read -p "Enter file name: " file
sort "$file" -o "$file"
