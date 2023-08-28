# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def length_circle(self):
        return 2 * pi * self.radius

    def square_circle(self):
        return pi * (self.radius ** 2)


c1 = Circle(8)
c2 = Circle(10)

print(f'length {c1.length_circle()}, square = {c1.square_circle()}')
print(f'length {c1.length_circle()}, square = {c1.square_circle()}')