#!/bin/bash

set -o errexit
set -o nounset

if [[ ${DB_ENGINE} == "postgres" ]]; then
    /wait-for-it.sh $POSTGRES_HOST:$POSTGRES_PORT --timeout=10 --strict -- echo "postgres is up"
fi

# local settings
watchfiles celery.__main__.main --ignore-paths db --args '-A config.celery_app worker -P prefork -l INFO'
