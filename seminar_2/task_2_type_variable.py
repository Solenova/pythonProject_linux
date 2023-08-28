# Задание №2
# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

import sys

data=[45, 'текст', 123.321, 'a', 45, 0]
for i, element in enumerate (data, 1):
    number_output = 'Это целое чсло' if isinstance(element, int) else ''
    str_output = 'Это стрoка' if isinstance(element, str) else ''
    print (f'пoрядковый номер {i},'
           f'значение {element}, '
           f'адрес в памяти {id(element)},'
           f'размер в памяти {sys.getsizeof(element)};'
           f'хэш объекта {hash(element)}'
           f'{number_output},'
           f'{str_output}')

    print(hash(data[i]))

