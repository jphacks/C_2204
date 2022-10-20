#!/bin/bash

cd ~/C_2204/client

yarn install --prod --frozen-lockfile
yarn build
nohup yarn start &
