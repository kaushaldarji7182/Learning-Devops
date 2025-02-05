#!/bin/sh
# Author: Kaushal Darji
# Purpose: Learning functions
# Usage: ./function.sh

function sum {
	local total=$(( $1 + $2 ))
    echo "total is $total"
}
# sum 
result=$(sum 5 8)
echo "the result is $result"