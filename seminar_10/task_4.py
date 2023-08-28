# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь
from random import randint

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


class Employee(Personality):
    def __init__(self, id_employee, *args):
        super().__init__(self, *args)
        if (99999 < id_employee) and (id_employee < 1000000):
            self.id_employee = id_employee
        else:
            self.id_employee = randint(100000, 999999)

    # def access_level(self):
    #     sum = 0
    #     number = int(self.id_employee)
    #     while number > 0:
    #         digit = number % 10
    #         sum += digit
    #         number //= 10
    #     res_level = sum % 7
    #     return res_level
    # 2method
    def access_level(self):
        return sum([int(item) for item in str(self.id_employee)]) % 7


if __name__ == "__main__":
    pers = Employee(52, 'ivan', 'family', 'surname')
    print(f'{pers.id_employee=}')
    print(f'уровень доступа {pers.access_level()} ')
