FROM python:3.8-alpine


RUN apk update \
    && apk add --no-cache --virtual bash \
    && apk add gcc \
    && apk add musl-dev \
    && apk add linux-headers \
    && apk add jpeg-dev \
    && apk add zlib-dev \
    && apk add mariadb-dev \
    && apk add libffi-dev

# install pypi packages

RUN pip install --upgrade pip

# COPY ./requirements.txt .
COPY requirements.txt /requirements.txt
COPY requirements_prod.txt /requirements_prod.txt

RUN pip install -r requirements_prod.txt

COPY ./djangoproject /app

WORKDIR /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
