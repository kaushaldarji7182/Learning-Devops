#!/bin/bash
#Author : Kaushal Darji
#Purpose : learning while loop
#Usage : ./multiply_while.sh


echo "Enter the number"
read -r  no
echo "MUltiplication od this $no "
counter=1
while [ $counter -le 10 ]
do
	mult=`expr $no \* $counter`
	echo "$no * $counter = $mult"
	counter=`expr $counter + 1`
done 