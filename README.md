# DeepSave - Documentation

## Deployed with ```Django-Apache-Nginx-Uwsgi``` on Ubuntu Server:22.0

- Data Distribuition by API REST with ```Django Rest Framework```

- Geteway with ``Apache``
- Reverse proxying, LoadBalancing with ``Nginx``
 

## Requirements
 - `Python 3.10`
 - `Mysql:8`


<br>

## Quickstart

<br>

Installng a virtual env:

`pip (or pip3) install virtualenv`

create a virtualenv:

`python (or python3) -m venv venv`

Starting your virtualenv:

`venv/Scripts/activate` - on Windows

`source venv/bin/activate` - on Linux

Necessary packages instalation:

`pip (or pip3) install -r requirements.txt`

create migrations:

`python (or python3) manage.py makemigrations`

Collect Staticfiles:

``` python manage.py collectstatic ```

migrating on database:

`python (or python3) manage.py migrate`

Create a user:

`python (or python3) manage.py createsuperuser`

~~~
- Input: Username
- Input: Email
- Input: Password
- Input: Confime password
~~~

Starting App 

`python (or python3) manage.py runserver`


## Running with Docker

``docker compose up -d``

or

```doker build -t name_image .```

``docker run -d --name name_container -p 8000:portB name_image:tag``

<br>

## Routes
- http://localhost:8000/documentation - GET DOCUMENTATIO
- http://localhost:8000/admin - Controll Panel Django
- http://localhost:8000/api/v1/link
- http://localhost:8000/api/v1/document


<br>
<br>


 * Make sure your settings.py has the following configurations:
 ```
 STATIC_URL = '/static/'
 STATIC_ROOT = os.path.join(BASE_DIR, "static")
 
 MEDIA_URL = '/media/'
 MEDIA_ROOT = os.path.join(BASE_DIR, "media")
 ```
 
 * Run Django collectstatic
 ```python manage.py collectstatic```

 
 ## Install and Setup 
 * Install Nginx and Dependencies
 
 ```
 ./setup.sh
```
## Configure Nginx

* Create NGINX config file at /etc/nginx/sites-available
```
upstream deepsave {
    server unix:///home/{USER}/deepSave/dp.sock; 
}

server {
    listen      8000;
    server_name example.com;
    charset     utf-8;

    client_max_body_size 75M; 

    location /media  {
        alias /home/{USER}/deepSave/media; 
    }

    location /static {
        alias /home/{USER}/deepSave/static;
    }

    location / {
        uwsgi_pass  deepsave;
        include     /home/{USER}/deepSave/uwsgi_params; 
    }
}
```

* Create a symlink on sites-enabled
sudo ln -s ~/path/to/your/mysite/mysite_nginx.conf /etc/nginx/sites-enabled/

* Restart Nginx
```sudo /etc/init.d/nginx restart```

* Download an image to media folder and test

* Run and test using Unix sockets
```uwsgi --socket mysite.sock --module mysite.wsgi --chmod-socket=666```

* Create the ini file

```
[uwsgi]
chdir           = /home/{USER}/deepSave
module          = deepsave.wsgi
home            = /home/{USER}/env
master          = true
processes       = 10
socket          = /home/{USER}/deepSave/dp.sock
vacuum          = true
chmod-socket    = 666
```

* Testing with .ini file
```uwsgi --ini dp_uwsgi.ini```


## Configuring the uWSGI
```
sudo mkdir /etc/uwsgi
sudo mkdir /etc/uwsgi/vassals
sudo ln -s /home/{USER}/deepSave/dp_uwsgi.ini /etc/uwsgi/vassals/
uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data
```
## Setup systemctl to start on boot

```
cd /etc/systemd/system/

sudo vim deepsave.service

======
[Unit]
Description=Django uWSGI
After=syslog.target

[Service]
ExecStart=/home/{USER}/env/bin/uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data
RuntimeDirectory=uwsgi
Restart=always
KillSignal=SIGQUIT
Type=notify
StandardError=syslog
NotifyAccess=all
User={USER}

[Install]
WantedBy=multi-user.target
======

sudo chmod 664 /etc/systemd/system/deepsave.service

sudo systemctl daemon-reload

sudo systemctl enable deepsave.service

 sudo systemctl start deepsave.service

 sudo systemctl status deepsave.service

journalctl -u deepsave.service

```

## Setup Apache2 with Nginx as a reverse Proxy

* disable nginx default symlink to open port 80
``` 
 cd /etc/nginx/sites-enabled/
 sudo rm -rf default
 sudo /etc/init.d/nginx restart
```

```
sudo apt-get install apache2
sudo a2enmod proxy
sudo a2enmod proxy_http
sudo a2enmod proxy_balancer
sudo a2enmod lbmethod_byrequests
```

```sudo systemctl restart apache2```

* Creating the Vhost

``` 
cd /etc/apache2/sites-available
sudo vim deepsave.conf
```

```
<VirtualHost *:80>
    ServerName 52.16.70.162
    ProxyPass / http://127.0.0.1:8000/
    ProxyPassReverse / http://127.0.0.1:8000/
</VirtualHost>
```

* Enable symlink on site-enable
```
sudo ln -s /etc/apache2/sites-available/deepsave.conf /etc/apach
e2/sites-enabled/
```

* Edit default vhost to your extra website

## Setup Django to user Mysql:8
```
TESTE
```