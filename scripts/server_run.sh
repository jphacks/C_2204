#!/bin/bash

cd ~/C_2204/server
sudo pip install -r ./requirements.txt

nohup python3 ./main.py &
