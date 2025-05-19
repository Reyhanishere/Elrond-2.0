# FROM python:3.12-bullseye
# ENV PYTHONUNBUFFERED=

# RUN apt update
# RUN apt install gettext -y

# RUN mkdir /code
# WORKDIR /code

# RUN pip install poetry

# COPY pyproject.toml poetry.lock ./
# RUN poetry install --no-root

# COPY . .

# EXPOSE 8000

# CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

# Example Dockerfile
FROM python:3.12

# Set work directory
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy only poetry config first to install dependencies
COPY pyproject.toml poetry.lock ./

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the rest of your project
COPY . .

# Run your app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
