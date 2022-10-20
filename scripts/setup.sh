#!/bin/bash

curl -sL https://deb.nodesource.com/setup_16.x | sudo bash -
sudo apt update
sudo apt install -y nodejs
sudo npm install -g yarn

git clone https://github.com/jphacks/C_2204.git

# run
cd ./C_2204/client/
yarn install --prod --frozen-lockfile
yarn build
yarn start


#!/bin/bash

curl -sL https://deb.nodesource.com/setup_16.x | sudo bash -

sudo apt update

sudo apt install mysql-server -y

sudo apt install nginx -y

sudo systemctl reload nginx

sudo apt-get install python3-dev default-libmysqlclient-dev build-essential -y
sudo apt install python3-pip -y

sudo apt install -y nodejs
sudo npm install -g yarn

pip install -r ./server/requirements.txt
