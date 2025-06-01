#!/usr/bin/env bash
#The script to set up the servers for the deployment of our web_static

sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test  /data/web_static/shared
echo "<html>
    <head>
    </head>
    <body>
      Holberton School
    </body>
   </html>" > /data/web_static/releases/test/index.html
 
sudo ln -sfn /data/web_static/releases/test/  /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '44i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
