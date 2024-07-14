#!/usr/bin/env bash
# configuration using puppet

exec { 'custom_http_header':
	command  => 'sudo apt-get update;
	sudo apt-get -y install nginx;
	sudo sed -i "/server_name _/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default
	sudo service nginx restart',
	provider => shell,
} 
