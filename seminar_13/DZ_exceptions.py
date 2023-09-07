# # Урок 15. Обзор стандартной библиотеки Python
# # Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование
# # ошибок и полезной информации. Также реализуйте возможность запуска из командной
# # строки с передачей параметров.

#
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.
import logging
from error import ErrorRectangleDimensions


class Range:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            logger.error(f'ввод отрицательной длины {value}')
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
        p = 2 * (self.height + self.width)
        logger.info(f'perimetr {p} ')
        return

    def get_area(self):
        s = self.width * self.height
        logger.info(f'perimetr {s} ')
        return s

    def __str__(self):
        return f'прямоугольник: ({self.height}x{self.width}), S= {self.get_area()}'

    def __repr__(self):
        return f'размеры:({self.height}x{self.width}), S= {self.get_area()}'


if __name__ == "__main__":
    FORMAT = '{levelname} - {asctime}. в {created} секунд записала сообщение: {msg}'

    logging.basicConfig(format=FORMAT, filename='rectangle.log', style='{', filemode='a', encoding='utf-8',
                        level=logging.NOTSET)
    logger = logging.getLogger(__name__)
    rect = Rectangle(2, 5)
    print(rect)

