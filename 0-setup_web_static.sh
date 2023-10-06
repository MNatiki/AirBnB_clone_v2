#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

echo "This is a test HTML file." > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

sudo sed -i "s-\tserver_name _;-\tserver_name _;\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n-" /etc/nginx/sites-available/default

service nginx restart

exit 0
