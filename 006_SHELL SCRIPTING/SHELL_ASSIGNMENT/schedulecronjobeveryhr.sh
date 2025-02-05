#!/bin/sh
# Author: Kaushal Darji
# Purpose: backup of file 
# Usage: ./schedulecronjobeveryhr.sh

echo "0 * * * * /path/to/script.sh" | crontab -
