#!/bin/sh
# Author: Kaushal Darji
# Purpose: backup of file 
# Usage: ./occurword.sh

#!/bin/bash
read -p "Enter file name: " file
tr -s ' ' '\n' < "$file" | sort | uniq -c | sort -nr | head -n 1


