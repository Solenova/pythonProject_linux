# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def func_str_2(text: str) -> dict[str, int]:
        my_list = text.split()
        my_dict = {}
        begin = min(int(my_list[0]), int(my_list[1]))
        my_end = max(int(my_list[0]), int(my_list[1]))
        for item in range(begin, my_end):
            my_dict[chr(item)] = item

        return my_dict


text_1='25 36'
# data = func_str(text_1)
print(func_str_2(text_1))