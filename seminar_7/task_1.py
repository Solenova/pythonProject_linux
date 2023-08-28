# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

import random
MIN_NUM = -1000
MAX_NUM = 1000
def filling_file (count: int, fname: str):
    with open(fname, 'a', encoding='utf-8') as f:
        for _ in range(0, count):
            f.write(f'{random.randint(MIN_NUM, MAX_NUM)} | {random.uniform(MIN_NUM, MAX_NUM)}\n')


if __name__ == '__main__':
    filling_file(3, 'number.txt') # заполняет файл (добавляет в конец) случайными парами чисел