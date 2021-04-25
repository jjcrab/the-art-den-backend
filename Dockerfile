FROM python:3

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/requirements.txt
RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

# RUN python manage.py makemigrations
# RUN python manage.py migrate



# CMD gunicorn artden.wsgi:application --bind 0.0.0.0:$PORT
# CMD python3 manage.py runserver 0.0.0.0:$PORT