FROM python:3.10-buster as builder

RUN pip install poetry==1.6.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml ./
RUN touch README.md

RUN --mount=type=cache,target=${POETRY_CACHE_DIR} poetry install --without dev --no-root

FROM python:3.10-slim-buster as runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY fastapi_template ./fastapi_template

ENTRYPOINT ["python", "-m", "fastapi_template.main"]
