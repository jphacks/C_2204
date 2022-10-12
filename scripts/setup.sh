#!/bin/bash

curl -sL https://deb.nodesource.com/setup_16.x | sudo bash -
sudo apt update
sudo apt install -y nodejs
sudo npm install -g yarn

git clone https://github.com/jphacks/C_2204.git
cd ./C_2204/client/
sudo yarn install