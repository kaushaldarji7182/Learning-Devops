#!/bin/bash
# Author: Kaushal Darji
# Purpose: Learning while loop
# Usage: ./multiply_while.sh



for i in 1 2 3 4 5 
do 	
	echo "$i"
done

for i in {1..5}; 
do
	echo "$i"
done

for i in $(seq 1 5); 
do
	echo "$i"
done


for (( i=1; i<=10; i++ ));
do
	echo "$i"
done