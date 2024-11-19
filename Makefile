SHELL := /bin/bash
.PHONY: setup script
OS := $(shell uname)
# .PHONY: script
SCRIPT := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(SCRIPT):;@:)

setup-front:
	pnpm i --dir ./frontend

setup-back:
ifeq ($(OS), Darwin)       # Mac OS X
	./setup/setup-osx.sh
else ifeq ($(OS), Linux)
	if [ "ID_LIKE=debian" != "" ]; then ./setup/setup-debian.sh; fi
else
	echo "Unsupported OS: $(OS). Please follow the manual installation."
endif

setup: setup-back setup-front

test:
	docker exec nango_django coverage run manage.py test -v2 --keepdb

up: 
	docker compose -f docker/development-postgres.yml up -d --no-color --build --remove-orphans 

up-prod: 
	docker compose -f docker/production.yml up -d --no-color --build --remove-orphans 

build-prod:
	docker compose -f docker/production.yml build
	
down:
	docker compose -f docker/development-postgres.yml down

downv:
	docker compose -f docker/development-postgres.yml down -v

nango:
	docker exec nango_django python manage.py bridge -t
	cp -r ./backend/.nango_front/ts_types ./frontend/src/api/nango_front/
	ruff format

route:
	docker exec nango_django python manage.py bridge -r

script:
	docker exec nango_django python manage.py runscript $(SCRIPT)
	
django:	# Go insine the Django container
	docker exec -it nango_django bash

makemigrations:
	docker exec -it nango_django python manage.py makemigrations
	ruff format

migrate:
	docker exec -it nango_django python manage.py migrate

coverage: test
	docker exec nango_django coverage html
	docker exec nango_django coverage report

stripe:
	# stripe login
	stripe listen --forward-to http://localhost:8000/api/stripe/webhook/
