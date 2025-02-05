#!/bin/bash
#Author : Kaushal Darji
#Purpose : for loop
#Usage : ./variable.sh


fruits=("apple" "banana" "grapes" "mango")
for fruit in "${fruits[@]}"; do
	echo "I like to eat $fruit"
done