#!/bin/bash
#Author : Kaushal Darji
#Purpose : for loop with index
#Usage : ./variable.sh


fruits=("apple" "banana" "grapes" "mango")
for i in "${!fruits[@]}"; do
	if [ $((i%2)) == 0 ]; then
		echo "fruit ate $i is ${fruits[$i]}"
	fi
done