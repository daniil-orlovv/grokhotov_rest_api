import json
import os
import django


from .utils_for_parse import (print_info, download_json, download_picture,
                              check_keywords)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rest_api.settings")
django.setup()

from ..models import Book, Category, Author


def parse_json() -> None:
    with open('api/parsing_json/books.json', 'r') as f:
        data = json.load(f)

    if not os.path.exists('api/parsing_json/images'):
        os.mkdir('api/parsing_json/images')

    keywords = ['title', 'isbn', 'pageCount', 'publishedDate', 'thumbnailUrl',
                'shortDescription', 'longDescription', 'status', 'authors']
    books_to_create = []
    without_isbn = []
    duplicate_isbn = []
    duplicate_book = []

    count = 0
    for item in data:
        values_for_db = {}
        for keyword in keywords:
            values_for_db[keyword] = check_keywords(keyword, item)

        if 'thumbnailUrl' in item:
            download_picture(item['thumbnailUrl'])
        else:
            print('Изображение для книги отсутствует')

        categories = []

        if 'categories' not in item or not item['categories']:
            new_category, created = Category.objects.get_or_create(
                title="Новинки")
            categories.append(new_category)

        if 'categories' in item:
            for category_name in item.get('categories', []):
                category, created = Category.objects.get_or_create(
                    title=category_name)
                categories.append(category)

        authors = []

        if 'authors' in item:
            for author_name in item.get('authors', []):
                author, created = Author.objects.get_or_create(
                    name=author_name)
                authors.append(author)

        if values_for_db['isbn']:

            exist_isbn = Book.objects.filter(
                isbn=values_for_db['isbn']).first()
            exist_title = Book.objects.filter(
                title=values_for_db['title']).first()

            if exist_isbn:  # Если книга с таким isbn существует:
                if exist_isbn.title == values_for_db['title']:
                    print(f"Книга '{values_for_db['title']}' уже существует.")
                    continue
                duplicate_isbn.append(f'Книга 1: {values_for_db["title"]}\n'
                                      f'Книга 2: {exist_isbn.title}\n'
                                      f'ISBN: {values_for_db["isbn"]}')
            if exist_title:  # Если книга с таким title существует:
                print(f"Книга '{values_for_db['title']}' уже существует.")
                continue

        else:
            exist_title = Book.objects.filter(
                title=values_for_db['title']).first()
            if exist_title:  # Если книга с таким title существует:
                print(f"Книга '{values_for_db['title']}' уже существует.")
                without_isbn.append(f'{values_for_db["title"]}')
                continue
            else:
                without_isbn.append(f'{values_for_db["title"]}')

        book = Book(
            title=values_for_db['title'],
            isbn=values_for_db['isbn'],
            pagecount=values_for_db['pageCount'],
            publisheddate=values_for_db['publishedDate'],
            thumbnailurl=values_for_db['thumbnailUrl'],
            shortdescription=values_for_db['shortDescription'],
            longdescription=values_for_db['longDescription'],
            status=values_for_db['status']
        )
        book.save()

        if categories:
            book.categories.add(*categories)
        if authors:
            book.authors.add(*authors)

        books_to_create.append(book)
        print(f'Книга {item["title"]} добавлена в список ')
        count += 1
        print(f'Обработано: {count}')
        print('__________________')

    print(f'Книг всего обработано: {count}\n\n')

    print_info(without_isbn, duplicate_isbn, duplicate_book)

    Book.objects.bulk_create(books_to_create)


if __name__ == "__main__":
    download_json()
    parse_json()
