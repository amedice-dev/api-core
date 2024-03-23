# pull official base image
FROM python:3.11-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apk add --no-cache netcat-openbsd
RUN apk add --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing hurl

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy the app folder
COPY app .

# copy the hurl folder
COPY hurl/dev ./hurl

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
