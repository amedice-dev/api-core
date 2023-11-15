# medical-centers-aggregator

This is the main application (backend) aggregator of medical centers.

## Clone this repository
```
$ git clone git@github.com:Medical-Centers-Aggregator/medical-centers-aggregator.git
```

## Requirements
1. install all requirements
```shell
pip install -r requirements.txt
```
2. run [docker](https://www.docker.com)

## Run App
```shell
docker compose up --wait --build --pull always
```

## Check Documentation
```
http://localhost:8080/doc/swagger
```
or
```
http://localhost:8080/doc/redoc
```

## Stop App
```shell
docker compose down
```
