#!/bin/sh
# Author: Kaushal Darji
# Purpose: backup of file 
# Usage: ./killprbyname.sh


read -p "Enter process name: " pname
pkill "$pname"
