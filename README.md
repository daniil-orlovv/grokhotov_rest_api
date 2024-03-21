# REST API for Grokhotov
### REST API для интернет-магазина по продаже книг

# Описание проекта
В проекте реализованы ручки для получения всех книг(всех книг определенной категории), одной конкретной книги, всех категорий и подкатегорий. Реализована авторизация с помощью jwt-token. Есть форма обратной связи. Реализована админ-панель для управления записями бд.

# Описание проекта
...
# Установка, настройка и запуск проекта
1. Установовить и запустить Docker

2. Склонировать проект 
`git clone git@github.com:daniil-orlovv/-grokhotov_rest_api.git`

3. Перейти в следующую директорию, где находится docker-compose.yml
`cd /grokhotov_rest_api/rest_api`

4. Запустить docker-compose:
`docker-compose up`

5. Зайти в контейнер:
`winpty docker exec -it rest_api-backend-1 bash`(`rest_api-backend-1` - название контейнера)

6. Выполнить миграции:
`python manage.py makemigrations` -> `python manage.py migrate`


# Стек технологий
