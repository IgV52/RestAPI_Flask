# API - POST

Приложение выполняет POST запрос и адресует его на jservice.io

## <br><b>Установка</b>

<b>Скачайте Docker на</b> https://www.docker.com/products/docker-desktop/

### <br><b>Откройте консоль</b>

<b>Выполните в консоли</b>             
    <details><summary> Команду: </summary>
```
git clone https://github.com/IgV52/RestAPI_Flask.git
```
</details>

### <br><b>Настройки</b>

<br><b>Зайдите в каталог RestAPI_Flask</b>

<b>Создайте в каталоге webapp/ файл config.py</b>             
    <details><summary> Параметры: </summary>
```
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI "postgresql://{имя пользователя}:{пароль}@db:5432/{название вашей базы данных}"
                Пример =  "postgresql://ivan:123456@db:5432/mydb"
```
</details>

<br><b>Вернитесь в каталог RestAPI_Flask</b>

<b>Откройте файлик docker-compose.yml</b>
    <details>
    <summary> Отредактируйте пользовательские параметры: </summary></b>
```
POSTGRES_DB: "{название вашей базы данных}"
POSTGRES_USER: "{имя пользователя}"
POSTGRES_PASSWORD: "{пароль}"
```
</details>

## <br><b>Запуск</b>

### <br><b>Откройте консоль</b>

<b>Выполните в консоли</b>             
    <details><summary> Команду: </summary>
```
docker-compose up --build
```
</details>

### <br><b>Дождитесь установки всех пакетов и надпись о том что база готова</b>

### <br><b>PostgreSQL init process complete; ready for start up.</b>

### <br><b>Работа с приложением</b>

<br><b>Зайдите в консоль</b>

<b>Выполните в консоли</b>             
    <details><summary> Команду: </summary>
```
curl -i -H "Content-Type: application/json" -X POST -d "{""num_questions"": int(число)}" http://адрес_вашего_сервера:5000/api/
```
</details>




