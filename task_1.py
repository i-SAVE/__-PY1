# TODO Написать 3 класса с документацией и аннотацией типов
# TODO работоспособность экземпляров класса проверить с помощью doctest

import doctest
from typing import Union


class Olympics:
    """
    Класс описывающий сноубордиста
    :param level: уровень подготвоки
    :param score: количесвто балов
    >>> pearson=Olympics("Medium",178)
    >>> pearson.cheack_level()
    'Запись успешна'
    """

    def __init__(self, level: str, score: Union[int, float]):
        self.level = level
        self.score = score
        if level.isdigit():
            raise TypeError
        if not isinstance(score, (int, float)):
            raise TypeError
        if score < 0:
            raise ValueError

    def check_level(self):
        """
        Метод проверки уровня
        :param self.level
        :return: str
        """
        if self.level == "Begginer":
            return "Не проходите отбор"
        else:
            return "Запись успешна"

    def training_program(self):
        """
        Метод, формирующий программу тренировки
        """
        pass


class Snowboard:
    """
    Класс описывающий сноуборд
    :param weight: ширина,см
    :param hight: высота,см
    >>> boar1=Snowboard(30,178)
    """

    def __init__(self, weight: Union[int, float], hight: Union[int, float]):
        self.weight = weight
        self.hight = hight
        if not isinstance(weight, (int, float)):
            raise TypeError
        if not isinstance(hight, (int, float)):
            raise TypeError
        if hight and weight <= 0:
            raise ValueError

    def level_skill(self):
        """
        Метод подбора доски по уровню катани
        """
        pass

    def check_price(self):
        """
        Метод подбора доски по уровню катания
        """
        pass


class Snowboarder:
    """
    Класс описывающий сноубордиста
    :param level: уровень подготвоки
    :param experience: опыт катания
    >>> pearson=Snowboarder("Mediun","Medium")
    """

    def __init__(self, level: str, experience: str):
        self.level = level
        self.experience = experience
        if level.isdigit():
            raise TypeError
        if experience.isdigit():
            raise TypeError

    def check_level(self):
        """
        Метод проверки уровня
        """
        pass

    def training_program(self):
        """
        Метод разработки программы тренировки
        """
        pass


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
