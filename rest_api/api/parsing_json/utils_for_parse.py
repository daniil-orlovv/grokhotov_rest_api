import os
import requests


def print_info(without_isbn, duplicate_isbn, duplicate_book):
    if without_isbn:
        print("Следующие книги не имеют ISBN:")
        for book in without_isbn:
            print(f'{book}')
        print('\n')
    if duplicate_isbn:
        print("Следующие книги могут иметь дубликаты ISBN:")
        for book in duplicate_isbn:
            print(f'{book}')
        print('\n')
    if duplicate_book:
        print("Следующие книги имеют дубли:")
        for book in duplicate_book:
            print(f'{book}')
        print('\n')


def check_keywords(keyword, item):
    if keyword == 'publishedDate':
        if 'publishedDate' in item:
            published_date = item['publishedDate']
            result = published_date.get('$date', None)
        else:
            result = None
    else:
        result = None if keyword not in item else item.get(keyword, None)
    return result


def download_picture(url):
    filename = os.path.join('images', os.path.basename(url))
    if os.path.exists(filename):
        print(f"Изображение '{filename}' уже существует.")
        return

    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as file:
            file.write(response.content)


def download_json():
    url = "https://gitlab.grokhotov.ru/hr/python-test-vacancy/-/raw/master/books.json?inline=false"
    file_name = 'books.json'
    response = requests.get(url)

    if response.status_code == 200:
        with open(file_name, "wb") as file:
            file.write(response.content)
        print(f"Файл {file_name} успешно загружен и сохранен в проекте.")
    else:
        print("Ошибка при загрузке файла:", response.status_code)
