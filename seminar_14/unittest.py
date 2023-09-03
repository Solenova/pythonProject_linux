# Задание №3
# Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)
import unittest

from task_1 import delsymbol


class TestDelSymbol(unittest.TestCase):

    def test_str(self):
        self.assertEquals(delsymbol('hello world'), 'hello world')

    def test_title(self):
        self.assertEquals(delsymbol('Hello World'), 'hello world')

    def test_symbol(self):
        self.assertEquals(delsymbol('hello! world'), 'hello world')

    def test_alpha(self):
        self.assertEquals(delsymbol('hello люди'), 'hello ')

    def test_all(self):
        self.assertEquals(delsymbol('Hello, люди!'), 'hello ')


if __name__ == '__main--':
    unittest.main(verbosity=2)


