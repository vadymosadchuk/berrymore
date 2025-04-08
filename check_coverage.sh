#!/bin/bash

set -a

source .env.sqlite
source ./.venv/bin/activate

coverage run --source=app --omit=*/migrations/* ./manage.py test
coverage report
