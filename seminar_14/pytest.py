# Задание №4
# Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import pytest
from task_1 import delsymbol


def test_str():
    assert delsymbol('hello world') == 'hello world'

def test_title():
    assert delsymbol('Hello World') == 'hello world'

def test_symbol():
    assert delsymbol('hello! world') == 'hello world'

def test_alpha():
    assert delsymbol('hello люди') == 'hello '

def test_all():
    assert delsymbol('Hello, люди!') == 'hello '

if __name__ == '__main__':
    pytest.main(['-v'])