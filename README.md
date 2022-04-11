# justwork
Проект представляет собой django app, который показывает весь список существующих сущностей,
с возможностью просматривать детально. 

## Начало установки

### Stack
1. Python 3.6+
2. Django 2+2.
3. Django Rest Framework
4. Celery
5. PostgreSQL
6. Docker + docker-compose

## Переменные окружения:

* SECRET_KEY: криптографическая подпись
* DEBUG: режим дебага включить/выключить
* ALLOWED_HOSTS: разрешенные хост
* DB_HOST: хост базы данных
* DB_PORT: порт базы данных
* POSTGRES_DB: имя базы данных
* POSTGRES_USER: пользователь базы данных
* POSTGRES_PASSWORD: пароль базы данных


## Зависимости:
Все зависимости в `requirements.txt`

## Запуск:
* docker-compose up --build
* Запуск кода `docker-compose up runserver`

## API
* Все страницы (GET) - http://127.0.0.1:8000/apps/pages?page=1 - по 100 обьектов
* Детальная информация одной страницы (GET) - http://127.0.0.1:8000/apps/page/1 - при вызове данного API срабатывает celery task
