# Base image
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install poetry

COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-root --only main

COPY . /app/

# 🔹 removed collectstatic step since no static files
# RUN poetry run python manage.py collectstatic --noinput

EXPOSE 80

CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:80", "book_shop.wsgi:application"]
