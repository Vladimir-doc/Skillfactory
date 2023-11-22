#!/bin/bash

#Start Nginx
nginx


#Start Gunicorn
gunicorn --bind 0.0.0.0:8000 django_app.wsgi:application