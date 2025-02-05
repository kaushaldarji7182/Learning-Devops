#!/bin/bash
#Author : Kaushal Darji
#Purpose : for loop with index
#Usage : ./variable.sh


fruits=("apple" "banana" "grapes" "mango")
for i in "${!fruits[@]}"; do
	echo "fruit ate $i is ${fruits[$i]}"
done