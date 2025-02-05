#!/bin/sh
# Author: Kaushal Darji
# Purpose: backup of file 
# Usage: ./finddeleteemptyfiles.sh

find . -type f -empty -delete
echo "Empty files deleted"
