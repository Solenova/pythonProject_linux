# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

def summ_num_index(my_name: list[int], ind_1: [int], ind_2: [int]) -> int:
    start_i: int
    end_i: int
    if ind_1 <= ind_2:
        start_i = ind_1
        end_i = ind_2
    else:
        start_i = ind_2
        end_i = ind_1
    if start_i < 0:
        start_i = 0
    if end_i > len(my_name)-1:
        end_i = len(my_name)-1
    list_res = my_name[start_i:end_i+1]

    return sum(list_res)
my_tarif = [22, 120, 24, 654, 28, 85, 23, 54]

print(summ_num_index(my_tarif, 2, 4))

# 2 metod
# def func(data: list[int | float], first: int | float, last: int | float) -> int | float:
#     i = min(first, last) if min(first, last) >= 0 else 0
#     j = max(first, last) if max(first, last) < len(data) else len(data)
#     result = sum(data[i:j])
#
#     return result
#
#
# s = [73, 42, 7, 3, 5, 2, 11, 100, 500, 1, -750]
#
# print(func(s, 200, 5))
