#!/usr/bin/env bash


DATE=$(date +%F_%T)
USER_FILE=user.txt

function echo_color() {

    if [ $1 == "green" ]; then
        echo -e "\e[32;1m$2\033[0m"
    elif [ $1 == "red" ]; then
        echo -e "\e[31;1m$2\033[0m"
    fi

}


if [-s $USER_FILE ]; then
    mv $USER_FILE ${USER_FILE}-${DATE}.bak
    echo_color green "$USER_FILE exist, rename ${USER_FILE}-${DATE}.bak"
fi

echo -e "user\tpassword" >> $USER_FILE
echo "-------------------"  >> $USER_FILE

for USER in user{1..10}; do
    if ! id $USER &> /dev/null; then
        PASS=$(echo $RANDOM | md5sum | cut -c 1-8)
        useradd $USER
        echo $PASS |passwd --stdin $USER &>/dev/null
        echo -e "$USER\t$PASS" >> $USER_FILE
        echo "$USER user create successful."
    else
        echo_color red "$USER user already exists!"
    fi
done
