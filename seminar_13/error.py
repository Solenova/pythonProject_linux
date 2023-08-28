class UserException(Exception):
    pass


class ErrorRectangleDimensions(UserException):
    """ Ошибка при введении отрицательных длин сторон прямоугольника"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Длины сторон прямоугольника должны быть положительными величинами'

class ErrorDimenshionMatrix(UserException):
    """ Ошибка размерности матриц"""

    def __str__(self):
        return f'Соблюдайте размерность матриц'