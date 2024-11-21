build:
	poetry install
	python manage.py migrate

start:
	python -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

dev:
	python manage.py runserver

lint:
	poetry run flake8 task_manager --exclude migrations