#!/bin/sh
# Author: Kaushal Darji
# Purpose: Linux in shell with command parameter
# Usage: ./linuxparamcomment.sh

command=`ls -ltr /etc`
echo "$command"


#ANOTHER WAY TO PRINT 
command="ls -ltr /etc"
eval $command