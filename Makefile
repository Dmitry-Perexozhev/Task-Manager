build:
	poetry install
	python manage.py migrate

start:
	python -m gunicorn task_manager.wsgi:application

dev:
	python manage.py runserver

lint:
	poetry run flake8 task_manager --exclude migrations