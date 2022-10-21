#!/bin/bash

curl -sL https://deb.nodesource.com/setup_16.x | sudo bash -

sudo apt update
sudo apt install -y nodejs
sudo npm install -g yarn
npm i -g next

sudo apt install mysql-server -y

sudo apt install nginx -y

sudo apt-get install python3-dev default-libmysqlclient-dev build-essential -y
sudo apt install python3-pip -y

git clone https://github.com/jphacks/C_2204.git

echo "ユーザとスキーマの作成"
echo "環境変数の設定"
