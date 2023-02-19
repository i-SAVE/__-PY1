class programming_language:
    """ Базовый класс - язык програмирования. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def number_of_community(self) -> int:
        pass

    def info(self):
        print(f"It is a programming language{self.name}.")

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


class Java(programming_language):
    """Дочерний класс - язык програмирования джава"""

    def __init__(self, difficulty: str, name: str, author: str):
        super().__init__(name, author)
        self._difficulty = None
        self.difficulty = difficulty  # отработает setter свойства!

    def __repr__(self):
        return f"{self.__class__.__name__}(difficulty={self.difficulty!r}, name={self.name!r}, author={self.author!r})"

    # вместо get_pages используется метод pages и @property
    @property
    def difficulty(self) -> str:
        """Возвращает сложность языка."""
        return self._difficulty

    # вместо set_pages используется метод pages и @pages.setter
    @difficulty.setter
    def difficulty(self, new_difficulty: str) -> None:
        """Устанавливает сложность языка."""
        if not isinstance(new_difficulty, str):
            raise TypeError("Сложность должна быть типа str")
        self._difficulty = new_difficulty


class Python(programming_language):
    """Дочерний класс - язык програмирования питон"""

    def __init__(self, version: float, name: str, author: str):
        super().__init__(name, author)
        self._version = version  # отработает setter свойства!

    def __repr__(self):
        return f"{self.__class__.__name__}(version={self.version!r}, name={self.name!r}, author={self.author!r})"

    # вместо get_duration используется метод duration и @property
    @property
    def version(self) -> float:
        """Возвращает версию в питоне."""
        return self._version

    # вместо set_duration используется метод duration и @duration.setter
    @version.setter
    def version(self, new_version: float) -> None:
        """Устанавливает версию питона."""
        if not isinstance(new_version, float):
            raise TypeError("Версия языка должна быть типа float")
        if new_version <= 0:
            raise ValueError("Версия питона не может быть отрицательным числом")
        self._version = new_version


if __name__ == "__main__":
    # Тестирую классы
    py = Python(version=3.10, name='python', author='Гвидо ван Россум')
    jv = Java(difficulty='средний', name='java', author='Джеймс Гослинг')
    py.version = 3.10
    jv.difficulty = 1.01
    print(py)
