# REST API for Grokhotov
## REST API для интернет-магазина по продаже книг

# Описание проекта
В проекте реализованы ручки для получения всех книг(всех книг определенной категории), одной конкретной книги, всех категорий и подкатегорий. Реализована авторизация с помощью jwt-token. Есть форма обратной связи. Реализована админ-панель для управления записями бд.

В проекте, по пути `/rest_api/api/parsing_json/parsing_json.py` находится скрипт для парсинга данных из json-файла в БД, а также вспомогательный файл с утилитами для парсинга `utils_for_parse.py`

- Файл для парсинга запрашивается по сети при указании ссылки для получения файла в `.env`
- В скрипте парсинга, после обработки всех книг - выводится информация о книгах, у которых одинаковый ISBN и о книгах, у которых нет ISBN
- Изображения хранятся в проекте: `/rest_api/api/parsing_json/images` с использованием `volume`
- При повторном парсинге не возникает дублей
- Книгам, не имеющим категорию, указывается категория "Новинки"
- На странице определенной книги выводятся еще 5 книг, относящихся к той же категории
- Данные об отзывах хранятся в БД



# Установка, настройка и запуск проекта
1. Установовить и запустить Docker

2. Склонировать проект 
`git clone git@github.com:daniil-orlovv/-grokhotov_rest_api.git`

3. Перейти в следующую директорию, где находится docker-compose.yml
`cd /grokhotov_rest_api/rest_api`

4. Запустить docker-compose:
`docker-compose up`

5. Зайти в контейнер:
`winpty docker exec -it rest_api-backend-1 bash`(`rest_api-backend-1`) - название контейнера)

6. Выполнить миграции, находясь в `/app#`:
`python manage.py makemigrations api` -> `python manage.py migrate`

7. Создать суперюзера для входа в админку
`python manage.py createsuperuser`

8. Создать файл `.env` в контейнере в директории `/app` и указать сгенерированный секретный ключ Django и ссылку на books.json

- Ссылка: https://gitlab.grokhotov.ru/hr/python-test-vacancy/-/raw/master/books.json?inline=false
- Сайт для генерации ключа: https://djecrety.ir/
   
9. Выполнить парсинг данных в бд, находясь в директории `/app#`:
`python -m api.parsing_json.parsing_json`
Дождаться выполнения скрипта и вывода результата, в котором указано, сколько книг обработано, какие книги имеют одинаковый ISBN и у каких книг его нет.

10. Данные наполнены, можно зайти и проверить наполнение в админке по адресу http://127.0.0.1:8000/admin, используя данные для входа, созданные с помощью `createsuperuser`

# Описание эндпоинтов 

- `GET` -> `/api/v1/books` -> Получение всех книг
- `GET` -> `api/v1/book/{id}` -> Получение определенной книги по ее id
- `GET` -> `/api/v1/books?categories__title={Название категории}` -> Получение книг, отфильтрованных по опредеденной категории
- `GET` -> `/api/v1/books?title={Название книги}` -> Получение книг, отфильтрованных по названию
- `GET` -> `/api/v1/books?authors={Имя автора}` -> Получение книг, отфильтрованных по автору
- `GET` -> `/api/v1/books?status={Статус}` -> Получение книг, отфильтрованных по статусу
- `GET` -> `/api/v1/books?publisheddate={Дата публикации}` -> Получение книг, отфильтрованных по дате публикации

- `GET` -> `/api/v1/category` -> Получение всех категорий
- `GET` -> `/api/v1/subcategory/` -> Получение всех подктегорий

- `POST` -> `/api/v1/feedback/` -> Отправка обратной связи
Тело запроса:
{
    "email": "mail@mail.ru",
    "name": "Имя",
    "comment": "Коммент",
    "phone": "79999999999"
}

`POST` -> `/auth/users/` -> Создание(регистрация) юзера
Тело запроса:
```
{
    "username": "username",
    "password": "12345678abc"
}
```
Ответ:
```
{
    "email": "",
    "username": "username",
    "id": 2
}
```
- `POST` -> `/auth/jwt/create/` -> Получение токена для аутентификации
Тело запроса:
```
{
    "username": "username",
    "password": "12345678abc"
}
```
Ответ:
```
{
    "refresh": "eyJhbGciOiJIUzItNiIsInR5cCI6IrpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMTE1MjUwNSwianRpIjoiMWIyN2U4OGYyZmM3NDViMzk5NzQzYjk4MGNiMjVjOTQiLCJ1c2VyX2lkIjoyfQ.jyj9E24EKF13UIZw9jGiDNKoFxbZ_mjXNcnf7HuaT6E",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzExMTUyNTA1LCJqdGkfOiJlN2RlM2NfWYxOTM0NGUwYTZjNzk1Nzk0MDJlNWRmOSIsInVzZXJfaWQiOjJ9.ANpkdo1L39o1x3QiYpVWRjUQuUNSc9MNnWJxObLULMQ"
}
```


Токен access использовать при запросе, указывая его в Authorization с типом `Bearer Token` без кавычек


- reDoc -> http://127.0.0.1:8000/redoc/
- Swagger -> http://127.0.0.1:8000/swagger/

Запросы тестировались с помощью `Postman`

# Стек технологий

- Django
- Django REST Framework
- Django Filter
- requests
- Djoser
- SimpeJWT
- Python-dotenv
- DRF-YASG
- SQLite
- Docker
- docker-compose
