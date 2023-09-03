# Задание №1
# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

# Задание №2
# Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)
import doctest
import re

def delsymbol(text: str):
    """
    deleter all ...
    >>> delsymbol('hello')
    'hello'
    >>> delsymbol('Hello')
    'hello'
    >>> delsymbol('hello, kitty')
    'hello kitty'
    >>> delsymbol('hello маша')
    'hello '
    >>> delsymbol('Hello, кат!')
    'hello '

    """
    regex = re.compile('[^a-zA-Z ]')
    return regex.sub('', text).lower()


if __name__ == '__main__':
    print(delsymbol('hgfdFD !() *&^%$gfdgf рппрсопрс'))
    doctest.testmod(verbose=True)
