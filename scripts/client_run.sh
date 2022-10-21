#!/bin/bash
# 動作確認
# ps -aux | grep yarn

cd ~/C_2204/client

yarn install --prod --frozen-lockfile
yarn build
nohup yarn start &
