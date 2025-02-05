#!/bin/sh
# Author: Kaushal Darji
# Purpose: Linux in shell with backup
# Usage: ./backup.sh

function backup {
    echo "enter the file name"
    read -r myfile
    if [ -f $myfile ]; then
    echo "file exists"
    cp $myfile /tmp/backup.sh
    else 
        echo "file doesnt exist"
    fi
    cp $myfile /tmp/backup.sh
    #if previous command is executed then $? will print 1
    echo $? 
    if [ $? -ne 0 ]; then
       echo "backup failed $?"
    fi
}
backup