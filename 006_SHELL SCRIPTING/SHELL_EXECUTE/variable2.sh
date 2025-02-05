
#!/bin/bash
echo "Hello world"
#Author : Kaushal Darji
#Purpose : creating variable
#Usage : ./variable.sh
var1=10
var2="hello"
hostname=$(hostname)
date=`date`
#The following definitions are not allowed
1value=100
false@linux=false
echo "var1=$var1"
echo "var2=$var2"
echo "hostname=$hostname"
echo "date=$date"
echo "1value=$1value"
echo "false@linux=$false@linux"
