# deepSave - Documentation

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

<br>

## Routes

~~~
http://localhost:8000/documentation - GET DOCUMENTATIO
http://localhost:8000/admin - Controll Panel Django
http://localhost:8000/api/v1/link
http://localhost:8000/api/v1/document