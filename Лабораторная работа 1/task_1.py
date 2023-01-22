# TODO Написать 3 класса с документацией и аннотацией типов
# TODO работоспособность экземпляров класса проверить с помощью doctest

import doctest

class Snowboard():
    """
    Класс описывающий сноуборд
    """

    def __init__(self, weight, hight):
        self.weight = weight
        self.hight = hight

    def level_skill(self):
        """
        Метод подбора доски по уровню катани
        """
        pass

    def check_price(self):
        """
        Метод подбора доски по уровню катания
        :param
        :return:
        """
        pass


class Snowboarder():
    def __init__(self, sex, level, experience):
        self.sex = sex
        self.level = level
        self.experience = experience

    def cheack_level(self):
        pass

    def training_programm(self):
        pass


class Olympics():
    def __init__(self, level, skill, score):
        self.level = level
        self.skill = skill
        self.score = score

    def cheack_level(self):
        pass

    def training_programm(self):
        pass


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
