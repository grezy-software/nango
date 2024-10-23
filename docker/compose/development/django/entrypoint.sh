#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

# N.B. If only .env files supported variable expansion...
export CELERY_BROKER_URL="${REDIS_URL}"

if [[ ${DB_ENGINE} == "postgres" ]]; then
    echo "Using Postgres..."
    bash /wait-for-postgres.sh
elif [[ ${DB_ENGINE} == "litestream" ]]; then
    echo "Using Litestream..."
else
    echo "DB_ENGINE must be one of 'postgres' or 'litestream' (DB_ENGINE=${DB_ENGINE})"
    exit 1
fi

echo "Running command: $@"

exec "$@"
