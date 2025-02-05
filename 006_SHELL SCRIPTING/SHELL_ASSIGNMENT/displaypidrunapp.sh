#!/bin/sh
# Author: Kaushal Darji
# Purpose: backup of file 
# Usage: ./displaypidrunapp.sh

read -p "Enter process name: " pname
pgrep "$pname"
