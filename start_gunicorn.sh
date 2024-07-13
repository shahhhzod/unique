#!/bin/bash
source /var/www/unique/venv/bin/activate
exec gunicorn unique_website.wsgi:application -c gunicorn_config.py
