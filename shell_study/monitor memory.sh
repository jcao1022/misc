#!/usr/bin/env bash

DATE=$(date +%F" "%H:%M)
IP=$(ifconfig eth0 |awk -F '[ :]+' '/inet addr/{print $4}') #Can be run on CentOS 6 only.
MAIL="example@mail.com"

TOTAL=$(free -m |awk '/Mem/{print $2}')
USE=$(free -m |awk '/Mem/{print $3-$6-$7}')
FREE=$(($TOTAL-$USE))
#内存小于1G发送报警邮件

if [ $FREE -lt 1024 ]: then
    echo "
    Date: $DATE
    Host: $IP
    Problem: Total=$TOTAL Use=$USE, Free=$FREE
    " mail -s "Memory Monitor" $MAIL
fi
