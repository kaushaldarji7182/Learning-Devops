#!/bin/sh
# Author: Kaushal Darji
# Purpose: backup of file 
# Usage: ./filebackup.sh

read -p "Enter directory to backup: " dir
tar -czvf "${dir}_backup_$(date +%F).tar.gz" "$dir"
