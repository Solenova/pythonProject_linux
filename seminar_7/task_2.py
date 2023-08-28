# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import random
from  random import randint, uniform, shuffle
STR_LETTER = 'qwrtpsdfghjklzxcvbnm'
STR_VOWEL = 'eyuioa'
MIN_LEN_PS = 4
MAX_LEN_PS = 7

def gen_psevdonim(name_file: str):
    spam = random.sample(STR_LETTER, randint(MIN_LEN_PS, MAX_LEN_PS - 1))
    eggs = random.sample(STR_VOWEL, randint(1, len(STR_VOWEL)))
    eggs.extend(spam)
    eggs = eggs[:random.randint(MIN_LEN_PS, MAX_LEN_PS)]
    random.shuffle(eggs)
    print(eggs)
    with open(name_file, 'a', encoding='utf-8') as f:
        f.write(f'{"".join(eggs).title()}\n')

if __name__ == '__main__':
    gen_psevdonim('../seminar_8/data.txt')



#     2 method
# def pseudo_names(fname: str):
#     with open(fname, 'a', encoding='utf-8') as f:
#         name = "jay", "jim", "roy", "axel", "billy", "charlie", "jax", "gina", "paul",
#         "ringo", "ally", "nicky", "cam", "ari", "trudie", "cal", "carl", "lady", "lauren",
#         "ichabod", "arthur", "ashley", "drake", "kim", "julio", "lorraine", "floyd", "janet",
#         "lydia", "charles", "pedro", "bradley"
#
#         f.write(f'{random.choice(name)} \n')