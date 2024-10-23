#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python /app/manage.py makemigrations
python /app/manage.py migrate
python /app/manage.py collectstatic --noinput
python /app/manage.py bridge

/usr/local/bin/gunicorn config.wsgi --bind 0.0.0.0:8000 --chdir=/app --workers=2 --threads=2 --max-requests 1000 --max-requests-jitter 50
