#!/usr/bin/env bash
#Method 1
IP_LIST="192.168.18.1 192.168.1.1 192.168.18.2"
for IP in $IP_LIST; do
    NUM=1
    while [ $NUM -le 3 ]; do
        if ping -c 1 $IP > /dev/null; then
            echo '$IP ping is successful.'
            break
        else
            FAIL_COUNT[$NUM]=$IP
            let NUM++
        fi
    done
    if [ ${#FAIL_COUNT[*]} -eq 3 ]; then
        echo "${FAIL_COUNT[1]} ping is failure!"
        unset FAIL_COUNT[*]
    fi
done



#Method 2
IP_LIST="192.168.18.1 192.168.1.1 192.168.18.2"
for IP in $IP_LIST; do
    FAIL_COUNT=0
    for ((i=1; i<=3; i++)); do
        if ping -c 1 $IP > /dev/null; then
            echo '$IP ping is successful.'
            break
        else

            let FAIL_COUNT++
        fi
    done
    if [ ${#FAIL_COUNT[*]} -eq 3 ]; then
        echo "$IP ping is failure!"
    fi
done

#Method 3
ping_success_status() {
    if ping -c 1 $IP > /dev/null; then
        echo '$IP ping is successful.'
        continue
    fi
}

IP_LIST="192.168.18.1 192.168.1.1 127.0.0.1"
for IP in $IP_LIST; do
    ping_success_status
    ping_success_status
    ping_success_status
    echo "$IP ping is failure!"
done


