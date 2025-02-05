#!/bin/bash
# Author: Kaushal Darji
# Purpose: Learning while loop
# Usage: ./until.sh

echo -e "please enter the ip to ping\c"
read -r ip
until ping $ip
do 
	echo "host i $ip is down"
	sleep 1
done 
echo "host in $ip is up"