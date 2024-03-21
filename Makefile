devmode:
	docker compose -f development/docker-compose.dev.yml run --entrypoint /bin/bash --service-ports --rm be-app

build:
	docker compose -f development/docker-compose.dev.yml build --no-cache

run:
	docker compose -f docker-compose.dev.yml up
