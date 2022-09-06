# Foodgram

![workflow](https://github.com/Xewus/Foodgram/actions/workflows/main.yml/badge.svg)

#### *Diploma work for Yandex*

***
Господа, раз уж скачиваете (собственно, для этого оно и открыто) справа вверху можно тыкнуть звёздочку.  
П.С. В `docker-compose.yml` в настройках для `nginx` вам нужно будет сменить порт `8001` на `80`.
У меня так настроено, потому что на одном сервере и IP висит несколько сайтов.
***

## Tecnhologies:
- Python 3.10
- Django 4.0
- Django REST framework 3.13
- Nginx
- Docker
- Postgres


## http://foodgram.gq


Here you can share recipes of dishes, add them to favorites and display a shopping list for cooking your favorite dishes.
To preserve order - only administrators are allowed to create tags and ingredients.

### To deploy this project need the next actions:
- Download project with SSH (actually you only need the folder 'infra/')
```
git@github.com:Xewus/foodgram-project-react.git
```
- Connect to your server:
```
ssh <server user>@<server IP>
```
- Install Docker on your server
```
sudo apt install docker.io
```
- Install Docker Compose (for Linux)
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
- Get permissions for docker-compose
```
sudo chmod +x /usr/local/bin/docker-compose
```
- Create project directory (preferably in your home directory)
```
mkdir foodgram && cd foodgram/
```
- Create env-file:
```
touch .env
```
- Fill in the env-file like it:
```
DEBUG=False
SECRET_KEY=<Your_some_long_string>
ALLOWED_HOSTS='localhost, 127.0.0.1, <Your_host>'
CSRF_TRUSTED_ORIGINS='http://localhost, http://127.0.0.1, http://<Your_host>'
DB_ENGINE='django.db.backends.postgresql'
DB_NAME='postgres'
POSTGRES_USER='postgres'
POSTGRES_PASSWORD=<Your_password>
DB_HOST='db'
DB_PORT=5432
```
- Copy files from 'infra/' (on your local machine) to your server:
```
scp -r infra/* <server user>@<server IP>:/home/<server user>/foodgram/
```
- Run docker-compose   

51.250.95.62 ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHUn582nCJeXdmG3BKthmc6Jlc9IC+8OpZpcHV5eUOE03/1hlAcFcmnziL9AFXt//hKMQRvrtUINXrJ+Nogh+5c=
51.250.95.62 ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDAn+YzSZYwmq3xR74HCYXSuQPt9mOq6HeBdtTAtgcFCNG261Efzja2qDV6q3QsmMjtLxkrAC4HG0o1FJDKrOUrerzwcZCzGw7lguPNyFsFZjB3bpevuHZluI+YcqqVpEY7zQv+vXGcj1yf1Czpie6cQX91esPWwGnFgxcSTNW8uWnYvce6u4UH4qvtZm74+k1W6xeO8nNkPEf/5qGkLi92avz5Wrj+Aej4ECbDnj05Dz/yiqKqI9KzEZ306+nRer5z/bYosikojeo9KKEPVBcB+cHRfqP5+J7ZwgxcBmCY6R3cE/za2N7HSd3KnV1SzPfNKlqyNGDHLS9IZ+7fmkslnaL5Pn+w54n/75x6hmG9bgNiWQi8IQw+g6umpOcqmmvNTOG8/pF19cmjkRam/pdAXk5eyxN1osRPnGbrYFx8AprXNmeYuYp2u6fMA0V4MXYvb72MbgqUd4yi3Bo15YOP/YDs71nf7SYuDLz6/C3vJesm9nyZXrHlyaK6nKQJDVs=
51.250.95.62 ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDdBAURtvr40GcwwvvyVYuQtcNb2OfF+lYoQ9Roeb8KR


```
sudo docker-compose up -d
```
Wait a few seconds...
Your service is work!
![Иллюстрация к проекту](https://github.com/Xewus/Foodgram/blob/master/screen.png)

## Enjoy your meal !

If you need, you can use the list of ingredients offered by us to write
recipes.
Upload it to the database with the following command 
### (this will also add a superuser with username - "qqq", password - "q", email - "q@q.qq
## DON'T FORGET TO CHANGE PASSWORD !!!):
```
sudo docker exec -it foodgram_backend_1 python manage.py loaddata data/dump.json
```

### *Backend by:*
https://github.com/Xewus
### *Frontend by:*
https://github.com/yandex-praktikum/foodgram-project-react
