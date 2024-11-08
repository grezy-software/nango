#!/bin/bash

set -o errexit
set -o nounset

if [[ ${DB_ENGINE} == "postgres" ]]; then
    /wait-for-it.sh $POSTGRES_HOST:$POSTGRES_PORT --timeout=10 --strict -- echo "postgres is up"
fi
celery \
    -A config.celery_app \
    -b "${CELERY_BROKER_URL}" \
    flower \
    --basic_auth="${CELERY_FLOWER_USER}:${CELERY_FLOWER_PASSWORD}"
