# Возьмите 1-3 задачи из тех,
# что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.

from error import ErrorRectangleDimensions


class Range:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ErrorRectangleDimensions(self.name)
        instance.__dict__[self.name] = value


class Rectangle:
    # __slots__ = ('_height', '_width')   #экономия памяти
    width = Range('_width')
    height = Range('_height')

    def __init__(self, width, height):
        self.height = height
        if width:
            self.width = width
        else:
            self.width = height

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def get_perimetr(self):
        return 2 * (self.height + self.width)

    def get_area(self):
        return self.width * self.height

    def __str__(self):
        return f'прямоугольник: ({self.height}x{self.width}), S= {self.get_area()}'

    def __repr__(self):
        return f'размеры:({self.height}x{self.width}), S= {self.get_area()}'


if __name__ == "__main__":
    rect = Rectangle(2, -5)

    print(rect)
