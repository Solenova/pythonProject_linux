# Задание №2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.
from math import pi


class Rectangle:
    def __init__(self, length, width):
        if length is None:
            self.length = width
            self.width = width
        elif width is None:
            self.length = length
            self.width = length
        else:
            self.length = length
            self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def square(self):
        return self.width * self.length


c1 = Rectangle(8, 2)
c2 = Rectangle(10, 5)

print(f'perimeter {c1.perimeter()}, square = {c1.square()}')
print(f'perimeter {c2.perimeter()}, square = {c2.square()}')