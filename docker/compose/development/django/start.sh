#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python /app/manage.py collectstatic --noinput

echo "Django docker is fully configured successfully."

python /app/manage.py migrate
python /app/manage.py bridge
python /app/manage.py runserver_plus 0.0.0.0:8000
