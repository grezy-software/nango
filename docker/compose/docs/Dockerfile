# FROM squidfunk/mkdocs-material

# WORKDIR /app
# COPY ./backend/requirements ./requirements
# RUN pip install -r ./requirements/docs.txt

# COPY ./mkdocs.yml .

# ENTRYPOINT ["mkdocs", "serve"]

FROM python:3.12-slim-bullseye

WORKDIR /app

COPY ./backend/requirements ./requirements
RUN pip install -r ./requirements/docs.txt

COPY ./mkdocs.yml .
COPY ./docs ./docs

EXPOSE 8000

CMD ["mkdocs", "serve", "--dev-addr", "0.0.0.0:8000"]
