# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat curl
RUN curl --location --remote-name https://github.com/Orange-OpenSource/hurl/releases/download/4.1.0/hurl_4.1.0_amd64.deb
RUN apt update && apt install ./hurl_4.1.0_amd64.deb -y && rm ./hurl_4.1.0_amd64.deb

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY app/entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy the app folder
COPY app .

# copy the hurl folder
COPY hurl/dev ./hurl

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
