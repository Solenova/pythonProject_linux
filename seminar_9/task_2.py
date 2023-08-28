# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюу гадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.


from random import randint
from typing import Callable

from typing import Callable


def main(func: Callable) -> Callable[[int, int], None]:
    def wrapper(*args):
        num, count = args   #передаются параметры из функции fun_secret, чтобы вытащить в переменные используем эту запись
        if num not in range(1, 101) and count not in range(1, 11):  # проверяем если число не входит в диапазон
            return func(randint(1, 100), randint(1, 10))
        else:
            return func(num, count)

    return wrapper

@main
def fun_secret(num: int, count: int):
    current_num = randint(1, num)
    for item in range(1, count+1):
        spam = int(input(f'введите число от 1 до {num}; попытка № {item}\n'))
        if spam == current_num:
            print('yes')
            break
        elif spam > current_num:
            print('введите меньше')
        else:
            print('введите больше')

if __name__ == "__main__":
    fun_secret(50, 15)