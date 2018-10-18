#!/usr/bin/env bash

#method 1
echo $RANDOM |cksum | cut -c 1-8

#method 2
openssl rand -base64 6 | cksum | cut -c 1-8

#method 3
date +%N |cut -c 1-8