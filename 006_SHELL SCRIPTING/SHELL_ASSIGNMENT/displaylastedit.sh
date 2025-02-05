#!/bin/sh
# Author: Kaushal Darji
# Purpose: backup of file 
# Usage: ./displaylastedit.sh

ls -lt | head -n 2 | tail -n 1 | awk '{print $9}'
