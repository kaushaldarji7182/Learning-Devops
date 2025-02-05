#!/bin/sh
# Author: Kaushal Darji
# Purpose: Linux in shell with command parameter
# Usage: ./linuxparamcomment.sh


while getopts :a:b: flag;do
    case $flag in
    a) ab=$OPTARG;;
    b) bc=$OPTARG;;
    ?) echo "i dont undertsand"
    esac
    
done
    echo " first value $ab,second value $bc"