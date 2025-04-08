#!/bin/bash

set -a

source .env.sqlite
source ./.venv/bin/activate

python ./manage.py test
