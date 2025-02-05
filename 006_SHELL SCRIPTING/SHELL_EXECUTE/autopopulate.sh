#!/bin/sh
# Author: Kaushal Darji
# Purpose: Auto populate in error handling 
# Usage: ./autopopulate.sh

echo "show All arguements will included here : $*"
echo "show no of arguement : $#"
echo "shows first arguement : $1"
echo "expand all the command line on seperate word : $@"
echo "process id of current process : $$"

#& when we use & it will run as background process
sleep 400 &
echo "file name of current program : $0"
echo "process id of recently background process : $!"