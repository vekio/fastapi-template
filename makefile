build:
	docker compose build
build-force:
	docker compose build --no-cache
run:
	docker compose up
service:
	docker compose up --detach
stop:
	docker compose rm --stop --force --volumes
