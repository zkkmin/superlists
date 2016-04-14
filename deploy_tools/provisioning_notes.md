Provisioning a new site
======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:
	sudo apt-get install nginx git python3 python3-pip
	sudo pip3 isntall virtualenv

## Nginx Viratual Host config

* see nginx.template.conf
* replace SITEMAP with, eg, staging.my-domain.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITEMAP with, eg, staging.my-domain.com

## Folder structure
Assume we have a user account at /home/username

/home/username
|__ sites
	|__ SITENAME
		|__ database
		|__ source
		|__ static
		|__ virtualenv


