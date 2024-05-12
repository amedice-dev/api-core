# Amedice

Это основное приложение (backend) агрегатора медицинских центров.

## Запуск dev-версии приложения

Зависимости

1. [docker](https://www.docker.com)
2. [poetry](https://python-poetry.org)


Запуск базы данных

```shell
docker compose up -d --build
```

Копировать и изменить `config.yaml`, в соответсвии с параметрами базы данных
```shell
cp config.yaml.template /app/etc/config/config.yaml
```

Статика, миграции, root-пользователь

```shell
make dev-deps
```
Запуск приложения

```shell
make run-app
```

Наполнение базы данных
```shell
make db-filling
```

Просмотр документации

[Swagger Documentation](http://localhost:8000/api/doc/swagger) | [ReDoc Documentation](http://localhost:8000/api/doc/redoc)


Остановка приложения

```shell
docker compose down
```

## Сброрка и отправка образа в Docker hub (пока ручками)

Авторизация
```shell
docker login
```
Сборка
```shell
docker build -t api-core:<тег> . --no-cache
```
Новый тег образа
```shell
docker tag api-core:<тег> amedicedev/api-core:<тег>
```
Отправка образа
```shell
docker push amedicedev/api-core:<тег>
```