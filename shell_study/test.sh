#!/usr/bin/env bash
cd ~
mkdir tmptest
cd tmptest

for ((i=0; i<10; i++)); do
  touch test_$i.txt
done

