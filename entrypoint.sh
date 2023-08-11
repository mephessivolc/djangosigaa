#!/bin/sh
python scripts/create_env.py -dev
python manage.py makemigrations address congress core discipline institute professors students users
python manage.py migrate --no-input
python manage.py collectstatic --noinput

# DJANGO_SUPERUSER_PASSWORD="66Kw!AEhNaCw" python manage.py createsuperuser --username "Clovis Caface" --email "clovis.caface@gmail.com" --noinput

gunicorn --reload djangoproject.wsgi:application -c ./gunicorn.py --bind 0.0.0.0:8000
# gunicorn --reload config.wsgi -c ./gunicorn.py -b 0.0.0.0:8888