#!/bin/bash

set -e

export PYTHONUNBUFFERED=1

python ./manage.py check_postgres

python ./manage.py migrate

python ./manage.py create_defaults


NAME="Berrymore"
DJANGODIR=/opt/app
SOCKFILE=/tmp/berrymore.sock
NUM_WORKERS=1
DJANGO_WSGI_MODULE=berrymore.wsgi

export DJANGO_SETTINGS_MODULE=berrymore.settings

exec gunicorn $DJANGO_WSGI_MODULE:application \
 --name $NAME \
 --workers $NUM_WORKERS \
 --bind=$LISTEN_HOST:$LISTEN_PORT \
 --access-logfile - \
 --error-logfile - \
 --threads=1000 \
 --log-level=debug \
 --no-sendfile \
 --timeout 30
