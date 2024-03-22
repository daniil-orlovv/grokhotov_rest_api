import os
import requests
from typing import List, Optional, Union

from dotenv import load_dotenv

load_dotenv()
URL_FOR_GET_JSON_FILE = os.getenv('URL_FOR_GET_JSON_FILE', default='url')


def print_info(
        without_isbn: List,
        duplicate_isbn: List,
        duplicate_book: List
        ) -> None:

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


def check_keywords(keyword: str, item: dict) -> Optional[Union[str, int]]:

    if keyword == 'publishedDate':
        if 'publishedDate' in item:
            published_date = item['publishedDate']
            result = published_date.get('$date', None)
        else:
            result = None
    else:
        result = None if keyword not in item else item.get(keyword, None)
    return result


def download_picture(url: str) -> None:

    filename = os.path.join('api/parsing_json/images', os.path.basename(url))
    if os.path.exists(filename):
        print(f"Изображение '{filename}' уже существует.")
        return

    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as file:
            file.write(response.content)


def download_json() -> None:

    url = URL_FOR_GET_JSON_FILE
    file_name = 'api/parsing_json/books.json'
    response = requests.get(url)

    if response.status_code == 200:
        with open(file_name, "wb") as file:
            file.write(response.content)
        print(f"Файл {file_name} успешно загружен и сохранен в проекте.")
    else:
        print("Ошибка при загрузке файла:", response.status_code)
