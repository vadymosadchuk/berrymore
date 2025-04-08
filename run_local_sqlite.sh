#!/bin/bash

set -a

source .env.sqlite
source ./.venv/bin/activate

python ./manage.py migrate

python ./manage.py create_defaults
if [ $? -eq 1 ]
  then
    exit 1
fi

python ./manage.py runserver $LISTEN_HOST:$LISTEN_PORT
