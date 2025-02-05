#!/bin/bash
#Author : Kaushal Darji
#Purpose : reading input from terminal variable
#Usage : ./variable.sh
#we can use $1 for input also



file=variable2.sh
if [ -f "$file" ]; then #for file name with space 
	echo "files $file exists"
else 
	echo "file doesnt exists"
fi



file=variable2.sh
if [[ -f "$file" ]]; #for file name with space 
	echo "files $file exists"
else 
	echo "file doesnt exists"
fi


file=$1
if [ -f $file ]; then 
	echo "files $file exists"
else 
	echo "file doesnt exists"
fi