FROM python:3.10-slim

WORKDIR /app

RUN pip install poetry

ENV POETRY_VIRTUALENVS_CREATE=false

COPY pyproject.toml poetry.lock .

RUN poetry install --no-root --only main

COPY . .

EXPOSE 5000

CMD ["gunicorn", "task_manager.wsgi:application", "--bind", "0.0.0.0:8000"]
