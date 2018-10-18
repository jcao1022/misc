#!/usr/bin/env bash

#method 1

function echo_color() {

    if [ $1 == "green" ]; then
        echo -e "\e[32;1m$2\033[0m"
    elif [ $1 == "red" ]; then
        echo -e "\e[31;1m$2\033[0m"
    fi

}

echo_color red "test####################################"
echo_color green "test##################################"

#method 2
function echo_color2() {

    case $1 in
        green)
            echo -e "\e[32;1m$2\033[0m"
            ;;
        red)
            echo -e "\e[31;1m$2\033[0m"
            ;;
        *)
            echo -e "Example: echo_color red 'string'"
            ;;
    esac

}
echo_color2 red "test####################################"
echo_color2 green "test##################################"