# FROM python:3.12-bullseye
# ENV PYTHONUNBUFFERED=1

# RUN mkdir /code

# WORKDIR /code

# RUN pip install poetry

# COPY pyproject.toml poetry.lock ./

# RUN poetry install

# COPY . .

# EXPOSE 8000

# ENTRYPOINT ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3.12-bullseye
ENV PYTHONUNBUFFERED=1

RUN mkdir /code

WORKDIR /code

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

COPY . .

RUN poetry install --no-root

CMD ["sh", "-c", "poetry install && python manage.py runserver 0.0.0.0:8000"]


EXPOSE 8000

ENTRYPOINT ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

