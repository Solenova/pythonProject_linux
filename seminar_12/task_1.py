# Задание №1
# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.

# Задание №2
# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

from collections import deque
import json


class Factorial:

    def __init__(self, count):
        self.count = count
        self.archive = deque(maxlen=count)

    def __call__(self, number):
        res = 1
        for item in range(1, number + 1):
            res *= item
        self.archive.append((number, res))   # добавляет ключ и значение в словарь для хранения
        return res

    def __str__(self):
        return str(self.archive)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('factorial_archive.json', 'w', encoding='utf-8') as fj:
            temp = {item[0]: item[1] for item in self.archive}
            json.dump(temp, fj, indent=2)

if __name__ == "__main__":

    with Factorial(3) as factor: #factor и есть экземпляр    #менеджер контекста
        print(factor(5)) #факториал находим от 5
        print(factor(3))
        print(factor(2))
        factor(4)
        factor(6)
        print(factor)
