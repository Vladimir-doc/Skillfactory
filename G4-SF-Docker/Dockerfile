FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
# Установка необходимых пакетов
RUN apt-get update && apt-get install -y python3 python3-pip python3-dev postgresql-client nginx
RUN pip3 install Django gunicorn

# Создаем и переходим в рабочую директорию
WORKDIR /django_app
VOLUME django_app
# Копируем файлы проекта в контейер
COPY . /django_app

# Установка PostgreSQL клиента и дополнительных пакетов
RUN apt-get install -y postgresql-client postgresql-contrib

# Настройка PostgreSQL (пример настройки, замените на свои параметры)
ENV POSTGRES_DB=mydb
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_HOST=db

# Установка и настройка Nginx
COPY nginx/nginx.conf /etc/nginx/nginx.conf

# Установка зависимостей Python из requirements.txt
COPY requirements.txt /django_app/requirements.txt
RUN pip3 install -r /django_app/requirements.txt

# Запускаем миграции и собираем статические файлы Django
RUN python3 manage.py migrate
RUN python3 manage.py createsuperuser --noinput --username admin --email admin@admin.com 

COPY start.sh /start.sh
RUN chmod +x /
CMD ["start.sh"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "django_app.wsgi:application"]