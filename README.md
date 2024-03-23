# Amedice

Это основное приложение (backend) агрегатора медицинских центров.

## Запуск dev-версии приложения

Клонировать репозиторий
```
$ git clone git@github.com:amedice-dev/api-core.git
```

Зависимости
1. run [docker](https://www.docker.com)

Запуск 
```shell
docker compose up -d --build
```

Просмотр документации
```
http://localhost:8000/api/doc/swagger
```
or
```
http://localhost:8000/api/doc/redoc
```

Остановка приложения
```shell
docker compose down
```

## Сброрка и отправка образа в Docker hub

Авторизация
```shell
docker login
```
Сборка
```shell
docker build -t api-core:<тег> -f Dockerfile.prod . --no-cache
```
Новый тег образа
```shell
docker tag api-core:<тег> amedicedev/api-core:<тег>
```
Отправка образа
```shell
docker push amedicedev/api-core:<тег>
```