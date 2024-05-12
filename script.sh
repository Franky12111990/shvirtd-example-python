#!/bin/bash

git clone https://github.com/Franky12111990/shvirtd-example-python.git

cd ~/root/shvirtd-example-python

docker build -t Dockerfile.pythone .

docker compose -f compose.yaml up -d
