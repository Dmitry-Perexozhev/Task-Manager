install:
	poetry install

start:
	gunicorn task_manager.wsgi