# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

import math

def simpl(n: int):
    count = 1
    number = 2
    yield number
    while count < n:
        number += 1
        for i in range(2, math.ceil(number ** 0.5) + 1):
            if number % i == 0:
                break
        else:
            count += 1
            yield number


for i in simpl(10):
    print(i)

