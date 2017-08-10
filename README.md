# README #

This README exists only to maintain a pattern with bitbucket/git. 

This repository exists to register my progress with Django classes by Alura.

The Django version that I use is 1.7.4

This project must be created by commands below:

django-admin.py startproject connectedin

python manage.py migrate

python manage.py runserver (can be python manage.py runserver 8008 or another port).

#create a new app inside the project:

python manage.py startapp perfis

#Edit file connectedin/connectedin/settings.py and register this new app (perfis)
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'perfis',    
)
#Don't forget the comma on end of 'perfis', <<--