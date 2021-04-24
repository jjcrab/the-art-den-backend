FROM python:3

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./
RUN set -ex \
    && pip3 install --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt

ADD . .