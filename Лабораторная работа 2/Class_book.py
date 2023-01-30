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


# TODO написать класс Book

class Book:
    # Инициализация экземпляра класса
    def __init__(self, id, name, pages):
        self.id = id  # type: int
        self.name = name  # type: str
        self.pages = pages  # type: int

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'


if __name__ == '__main__':
    result = []
    # инициализируем список книг
    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    for book in list_books:
        print(f"{book}")  # проверяем метод __str__
    print(list_books)
