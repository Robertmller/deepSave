#!/bin/bash

sudo apt update -y && \n
sudo apt upgrade -y && \n
sudo apt-get install python3.10 -y && \n
sudo apt-get install python3.10-dev -y && \n
sudo apt-get install build-essential libssl-dev libffi-dev -y && \n
sudo apt-get install python3.10-venv -y
sudo apt-get install mysql-client -y && \n
sudo apt-get install libmysqlclient-dev -y && \n
sudo apt-get install libssl-dev -y && \n
sudo apt-get install nginx -y && \n
sudo /etc/init.d/nginx start