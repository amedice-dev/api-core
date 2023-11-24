# Amedice

Это основное приложение (backend) агрегатора медицинских центров.

## Клонировать репозиторий
```
$ git clone git@github.com:amedice-dev/api-core.git
```

## Зависимости
1. run [docker](https://www.docker.com)

## Запуск dev-версии приложения 
```shell
docker compose up -d --build
```

## Документация
```
http://localhost:8000/doc/swagger
```
or
```
http://localhost:8000/doc/redoc
```

## Остановка приложения
```shell
docker compose down
```
