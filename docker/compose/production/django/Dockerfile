# pull official base image
ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION} AS python

# ----------------------------------------------------------------------------------------
# Python build stage
FROM python AS python-build-stage
ARG BUILD_ENVIRONMENT=production

# Update and install 
RUN apt-get update && apt-get install --no-install-recommends -y \
    # psycopg2 dependencies
    libpq-dev \
    # Translations dependencies
    gettext \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Create Python Dependency and Sub-Dependency Wheels.
COPY ./backend/requirements .
RUN pip wheel --wheel-dir /usr/src/app/wheels \
    -r ${BUILD_ENVIRONMENT}.txt

# ----------------------------------------------------------------------------------------
# Python 'run' stage
FROM python AS python-run-stage

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG BUILD_ENVIRONMENT=production
ARG APP_HOME=/app

# set work directory
WORKDIR ${APP_HOME}

# Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    # psycopg2 dependencies
    libpq-dev curl \
    # Translations dependencies
    gettext \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# All absolute dir copies ignore workdir instruction. All relative dir copies are wrt to the workdir instruction
# copy python dependency wheels from python-build-stage
COPY --from=python-build-stage /usr/src/app/wheels  /wheels/

# use wheels to install python dependencies
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -rf /wheels/


# Commands
COPY ./docker/compose/${BUILD_ENVIRONMENT}/django/start.sh /start.sh
RUN sed -i 's/\r$//g' /start.sh && chmod +x /start.sh

COPY ./docker/compose/${BUILD_ENVIRONMENT}/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//g' /entrypoint.sh && chmod +x /entrypoint.sh

COPY ./docker/compose/${BUILD_ENVIRONMENT}/django/wait-for-postgres.sh /wait-for-postgres.sh
RUN sed -i 's/\r$//g' /wait-for-postgres.sh && chmod +x /wait-for-postgres.sh

COPY ./docker/wait-for-it.sh /wait-for-it.sh
RUN sed -i 's/\r$//g' /wait-for-it.sh && chmod +x /wait-for-it.sh

COPY ./docker/compose/${BUILD_ENVIRONMENT}/django/celery/worker/start.sh /start-celeryworker.sh
RUN sed -i 's/\r$//g' /start-celeryworker.sh && chmod +x /start-celeryworker.sh

COPY ./docker/compose/${BUILD_ENVIRONMENT}/django/celery/beat/start.sh /start-celerybeat.sh
RUN sed -i 's/\r$//g' /start-celerybeat.sh && chmod +x /start-celerybeat.sh

COPY ./backend .

RUN useradd -ms /bin/bash celery

ENTRYPOINT ["/entrypoint.sh"]