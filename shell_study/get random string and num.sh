#!/usr/bin/env bash

#method 1
echo $RANDOM |md5sum | cut -c 1-8

#method 2
openssl rand -base64 6

#method 3
cat /proc/sys/kernel/random/uuid | cut -c 1-8


