from typing import List

# TODO написать класс Book
BOOKS_INFORM = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 234,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 785,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_INFORM
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__


# TODO написать класс Library

class Library:
    def __init__(self, books: List[Book] = []):
        self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        else:
            return len(self.books) + 1

    def get_index_by_book_id(self, id_: int):
        for _id_, info in enumerate(self.books):
            if _id_ == id_ - 1:
                return _id_
            else:
                raise ValueError("Книги с запрашиваемым id не существует")
        # TODO написать класс Library


if __name__ == '__main__':
    empty_library = Library()  # Инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # Проверка следующего id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"],
             pages=book_dict["pages"]) for book_dict in BOOKS_INFORM
    ]
    library_with_books = Library(books=list_books)  # Инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # Проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # Проверяем индекс книги с id = 1
