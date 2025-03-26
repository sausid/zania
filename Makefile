APP_NAME=ecommerce

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

runserver:
	python manage.py runserver

test:
	python manage.py test

collectstatic:
	python manage.py collectstatic --noinput

deploy:
	build collectstatic run

down:
	docker-compose down

up:
	docker-compose up -d

build:
	docker-compose build

rundocker:
	docker-compose down
	docker-compose build
	docker-compose up -d
	docker exec -it $(APP_NAME) sh -c "python manage.py migrate"
	docker exec -it $(APP_NAME) sh -c "python manage.py collectstatic --noinput"
