#!/bin/sh
# Author: Kaushal Darji
# Purpose: backup of file 
# Usage: ./emailnotifylowdspace.sh

THRESHOLD=90
USAGE=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')

if [ "$USAGE" -ge "$THRESHOLD" ]; then
    echo "Warning: Disk space is above $THRESHOLD%" | mail -s "Disk Space Alert" user@example.com
fi
