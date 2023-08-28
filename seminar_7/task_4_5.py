# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

import random
from  random import randint, choices
from  string import ascii_lowercase, digits
STR_LETTER = 'qwrtpsdfghjklzxcvbnm'
STR_VOWEL = 'eyuioa'
MIN_LEN_PS = 4
MAX_LEN_PS = 7
#
# def gen_psevdonim():
#     spam = random.sample(STR_LETTER, randint(MIN_LEN_PS, MAX_LEN_PS - 1))
#     eggs = random.sample(STR_VOWEL, randint(1, len(STR_VOWEL)))
#     eggs.extend(spam)
#     eggs = eggs[:random.randint(MIN_LEN_PS, MAX_LEN_PS)]
#     random.shuffle(eggs)
#     print(eggs)
#     name = "".join(eggs)
#     return name
# print(gen_psevdonim())
#
#
# def add_file(extension: str, min_len: int = 6, max_len: int = 30,\
#              min_byte: int = 256, max_byte: int = 4096, count_file: int = 42):
#     file_name = gen_psevdonim() + '.' + extension
#     with open(file_name, 'w', encoding='utf-8') as f:
#         f.truncate(randint(min_byte, max_byte))
#     return file_name


# -------------2 method
def add_file_1(extension: str, min_len: int = 6, max_len: int = 30,\
             min_byte: int = 256, max_byte: int = 4096, count_file: int = 42):
    for _ in range(0, count_file):
        name_file_1 = "".join(random.choices(STR_LETTER, k=random.randint(min_len, max_len))) + '.' + extension
        with open(name_file_1, 'wb') as f:
            f.write(bytes(randint(0, 255) for _ in range(randint(min_byte, max_byte))))

#-------------2 method
def make_file(extension: str, min_name: int = 6, max_name: int = 30,
              min_size: int = 256, max_size: int = 4096, count: int = 42):
    for _ in range(count):
        name = "".join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{extension}', 'wb') as f:
            f.write(data)

if __name__ == '__main__':
    make_file('bin', count=3)
#____________________________________________________
    # Доработаем предыдущую задачу.
    # ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
    # ✔ Расширения и количество файлов функция принимает в качестве параметров.
    # ✔ Количество переданных расширений может быть любым.
    # ✔ Количество файлов для каждого расширения различно.
    # ✔ Внутри используйте вызов функции из прошлой задачи.

def file_generate(**kwargs) -> None:
    for extension, count, in kwargs.items():
        make_file(extension=extension, count=count)

if __name__ == '__main__':
    file_generate(bin=2, jpg=1)

