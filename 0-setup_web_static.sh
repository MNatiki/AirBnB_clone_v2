#!/usr/bin/env bash
# a bash script that set up web server for web deployment
sudo apt update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
sudo echo "testing server configration files" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i "s-\tserver_name _;-\tserver_name _;\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n-" /etc/nginx/sites_enabled/default
sudo sed -i "s-\tserver_name _;-\tserver_name _;\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n-" /etc/nginx/sites_available/default
sudo service nginx restart

