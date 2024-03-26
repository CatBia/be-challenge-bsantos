devmode:
	docker compose -f development/docker-compose.dev.yml run --entrypoint /bin/bash --service-ports --rm be-app

build:
	docker compose -f development/docker-compose.dev.yml build --no-cache

run:
	docker compose -f development/docker-compose.dev.yml run --entrypoint 'python application/main.py' --service-ports --rm be-app
test:
	docker compose -f development/docker-compose.dev.yml run --entrypoint 'python -m pytest' --service-ports --rm be-app
