# Задание №3
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.
import datetime


class Personality:
    def __init__(self, last_name, first_name, surname, age):
        self.last_name = last_name
        self.first_name = first_name
        self.surname = surname
        self.__age = age

    def get_age(self):
        return self.__age

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return f'{self.first_name} {self.last_name} {self.surname}'


if __name__ == "__main__":
    c2 = Personality('Ivanov', 'Ivan', 'Ivanovich', 30)
    print(c2.full_name())
    c2.birthday()
    print(c2.get_age())