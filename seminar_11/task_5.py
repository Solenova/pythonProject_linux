# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.


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


c1 = Rectangle(8, 2)
c2 = Rectangle(10, 5)
s = c2 + c1
r = c1 - c2

print(f'perimeter {c1.perimeter()}, square = {c1.square()}')
print(f'perimeter {c2.perimeter()}, square = {c2.square()}')
print(f'summ {s.length}  {s.width}')
print(f'sub {r}')
