# Задание №1
# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.
#

from random import randint
from typing import Callable

from typing import Callable
def add_one_str(num: int, count: int) -> Callable[[], None]:
    def add_two_str():
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

    return add_two_str


if __name__ == "__main__":
    game = add_one_str(int(input('input num')), int(input('count')))
    game()
