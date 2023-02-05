class Book:
    """ Базовый класс - книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        """Геттер не принимает никаких агрументов, но должен возвращать какой-то результат."""
        return self._name  # внутри класса обращаемся к защищенному атрибуту

    @property
    def author(self):
        """Геттер не принимает никаких агрументов, но должен возвращать какой-то результат."""
        return self._author  # внутри класса обращаемся к защищенному атрибуту

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Дочерний класс - бумажная книга"""

    def __init__(self, pages: int, name: str, author: str):
        super().__init__(name, author)
        self.pages = pages  # отработает setter свойства!

    # вместо get_pages используется метод pages и @property
    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages

    # вместо set_pages используется метод pages и @pages.setter
    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages


class AudioBook(Book):
    """Дочерний класс - аудиокнига"""

    def __init__(self, duration: float, name: str, author: str):
        super().__init__(name, author)
        self._duration = duration  # отработает setter свойства!

    # вместо get_duration используется метод duration и @property
    @property
    def duration(self) -> float:
        """Возвращает продолжительность в аудиокниге."""
        return self._duration

    # вместо set_duration используется метод duration и @duration.setter
    @duration.setter
    def duration(self, new_duration: float) -> None:
        """Устанавливает продолжительность аудиокниги."""
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = new_duration


if __name__ == '__main__':
    # Тестирую классы
    evg = Book('Евгений Онегин', 'А. С. Пушкина')
    war = AudioBook(duration=4.55, name='Война_и_Мир', author='Л. Н. Толстой')

    war.duration = 4.55
    print(evg.name, evg.author)  # Евгений Онегин А. С. Пушкина
    print(evg)  # Книга Евгений Онегин. Автор А. С. Пушкина
    print(war.duration)  # 4.55


# Замечание об __str__ и __repr__: оба этих метода преобразуют объект к строке.
# Но __str__ обычно используют для представления данных в удобном для чтения пользователем виде.
# И именно его вызовет метод print, а __repr__ чаще пишут так,
# чтобы было удобно читать отладочную информацию или выполнять полученную строку как код.
# Интерпретатор вызывает __repr__.
# Если функции __str__ нет, то вызывается автоматически __repr__.
