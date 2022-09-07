# Foodgram

![workflow](https://github.com/Xewus/Foodgram/actions/workflows/main.yml/badge.svg)

### Проект размещен по адресу
http://51.250.95.62/


## Необходимое ПО:
- Python 3.10
- Django 4.0
- Nginx
- Docker
- Postgres



### Инструкция по запуску:
- Установите Docker на ваш сервер
- В домашней директории создайте директорию проекта
```
mkdir foodgram 
```
- В директории проекта создайте .env файл со следующими переменными:
DEBUG=False
SECRET_KEY
ALLOWED_HOSTS
CSRF_TRUSTED_ORIGINS
DB_ENGINE='django.db.backends.postgresql'
DB_NAME='postgres'
POSTGRES_USER='postgres'
POSTGRES_PASSWORD
DB_HOST='db'
DB_PORT=5432

- Скопируйте файлы из папки 'infra/' на сервер в папку проекта:
- Запустите docker-compose   
```
sudo docker-compose up -d
```