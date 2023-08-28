# Задание №6
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения


class Rectangle:
    """Класс Rectangle принимает два значения. Большее значение присваивает длине, меньшее ширине
    """
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
        """Периметр прямоугольника"""
        return 2 * (self.length + self.width)

    def __add__(self, other):
        sum_rectangle = self.perimeter() + other.perimeter()
        x = sum_rectangle / 4
        y = sum_rectangle - x
        return Rectangle(x, y)

    def __sub__(self, other):
        sub_rectangle = abs(self.perimeter() - other.perimeter())
        x = sub_rectangle / 4
        y = sub_rectangle - x
        return Rectangle(x, y)

    def square(self):
        """Площадь прямоугольника"""
        return self.width * self.length

    def __eq__(self, other):
        return self.square() == other.square()

    def __ne__(self, other):
        return self.square() != other.square()

    def __gt__(self, other):
        return self.square() > other.square()

    def __str__(self):
        return f'длина прямоугольника  {self.length}, ширина прямоугольника  {self.width}'

    def __repr__(self):
        return f' {self.perimeter}, string {self.square}'

c1 = Rectangle(10, 2)
c = c1
c2 = Rectangle(2, 8)
c_ = c2
s = c2 + c1
r = c1 - c2

print(f'perimeter {c1.perimeter()}, square = {c1.square()}')
print(f'perimeter {c2.perimeter()}, square = {c2.square()}')
print(f'perimeter {c}, square = {c}')
print(f'perimeter {c_}, square = {c_}')
print(f'summ {s.length}  {s.width}')
print(f'sub {r}')
print(f' {c1 == c2 =} ')
print(f' {c1 != c2 =} ')
print(f' {c1 > c2 =} ')
