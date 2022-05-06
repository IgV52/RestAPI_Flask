FROM python:3.10
# Устанавливаем рабочую директорию для проекта в контейнере
WORKDIR /RestAPI_Flask
# Скачиваем/обновляем необходимые библиотеки для проекта 
COPY requirements.txt /RestAPI_Flask
RUN pip3 install --upgrade pip -r requirements.txt
# |ВАЖНЫЙ МОМЕНТ| копируем содержимое папки, где находится Dockerfile, 
# в рабочую директорию контейнера
COPY . /RestAPI_Flask
# Устанавливаем порт, который будет использоваться для сервера
EXPOSE 5000
