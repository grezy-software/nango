#!/bin/bash

set -o errexit
set -o nounset

if [[ ${DB_ENGINE} == "postgres" ]]; then
    /wait-for-it.sh $POSTGRES_HOST:$POSTGRES_PORT --timeout=10 --strict -- echo "postgres is up"
fi
sleep 10
rm -f './celerybeat.pid'

celery -A config.celery_app beat --max-interval=3600 -l INFO
