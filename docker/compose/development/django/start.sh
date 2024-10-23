#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py collectstatic --noinput

echo "Django docker is fully configured successfully."

python manage.py bridge
python manage.py runserver_plus 0.0.0.0:8000
