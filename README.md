# yamdb_final
[![yamdb_final workflow](https://github.com/cheepok/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?branch=master)](https://github.com/cheepok/yamdb_final/actions/workflows/yamdb_workflow.yml)

### Проект размещен по адресу
http://51.250.95.62/

Админка:
http://51.250.95.62/admin/login/
admin
admin

## Описание
Сайт является отзовиком по музыкальным произведениям. Пользователи могут оставлять рецензии на песни, а еще комментировать чужие отзывы.
Админы могут поплнять базу произведений и категорий.

## Необходимое ПО

Docker
Docker-compose

## Инструкция по запуску

Из корневой папки выполните:
```
docker-compose up --build
```
Узнайте id существующих контейнеров
```
docker container ls
```
Скопируйте id web-контейнера и войдите в него
```
docker exec -it <CONTAINER ID> sh
```
Сделайте миграцию БД и сбор статики
```
python manage.py migrate
python manage.py collectstatic
```
## Окружение
Для хранения важных данных использован .env файл. Файл добавлен в .gitignore, чтобы исключить попадание в Git. 
Для запуска сайта необходимо в папке infra создать .env файл со следующими переменными:
DB_ENGINE
DB_NAME
POSTGRES_USER
POSTGRES_PASSWORD
DB_HOST
DB_PORT  

## Автор

* **Никита Колпаков** - https://github.com/cheepok
