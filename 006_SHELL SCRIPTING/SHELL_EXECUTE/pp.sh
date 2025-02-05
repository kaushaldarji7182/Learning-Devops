#!/bin/sh

# echo "hello world"

# read -p "enter no" no
# echo "no is $no"

# time=$(date +%H)
# if [ "$time" -le 12 ] ; then
# echo "good afternoon"
# else 
# echo "invalid"
# fi

# set `date`
# echo "day is $1"
# echo "month is $2"
# echo "date is $3"
# echo "year is $4"
# echo "timezone is $5"
# echo "am pm is $6"


# echo -e "enter ip to ping " 
# read -r ip
# until ping $ip
# do
#     echo "ip is down"
#     sleep 1
# done 
# echo "ip is up"



substr="12345678"
if [[ $substr =~ ^1.*8 ]]; then
echo "done"
else 
echo "not done"
fi