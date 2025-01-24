FROM python:3.10

COPY . .

RUN pip install poetry

COPY pyproject.toml poetry.lock /

RUN poetry install --no-root


EXPOSE 8000

CMD ["poetry", "run", "python","manage.py", "makemigrations"]

CMD ["poetry", "run", "python","manage.py", "migrate"]

CMD ["poetry", "run", "python","manage.py", "runserver", "0.0.0.0:8000"]