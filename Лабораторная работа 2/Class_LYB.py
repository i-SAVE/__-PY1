BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id, name, pages):
        self.id = id  # type: int
        self.name = name  # type: str
        self.pages = pages  # type: int


# TODO написать класс Book

class Library:  # класс Library

    def __init__(self, books=list()):  # Инициализация экземпляра
        self.books = books  # Список книг, изначально пустой

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            id_res = self.books["id"]
            return id_res + 1


# TODO написать класс Library

if __name__ == '__main__':
    """
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
    """

    books = {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    }
    res = Library(books=books)
    print(res.get_next_book_id())
