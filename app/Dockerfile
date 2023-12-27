# pull official base image
FROM python:slim-bullseye

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y netcat python3-pip

# install dependencies
# RUN pip install --upgrade pip
COPY ./requirements.txt .
# COPY ./requirements.prod.txt .
RUN pip install --no-cache-dir -r requirements.txt


# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]