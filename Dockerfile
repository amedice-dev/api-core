# Base image
FROM python:3.11.4-slim-buster

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.5.1

# System deps:
RUN pip install --upgrade --progress-bar off pip && pip install --progress-bar off "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /
COPY poetry.lock pyproject.toml /

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --only main

WORKDIR app/
COPY ./app /app

# Создаем папки для static и mediafiles
RUN mkdir -p /app/staticfiles /app/mediafiles
