#!/bin/bash
# 動作確認
# ps -aux | grep python

cd ~/C_2204/server
sudo pip install -r ./requirements.txt

nohup python3 ./main.py &
