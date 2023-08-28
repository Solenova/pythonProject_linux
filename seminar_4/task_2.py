# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def func_str (my_text) -> list[int]:
    mi_list = list()
    for i in range(len(my_text)):
        my_list[i] = ord(my_text[i])
        my_list = sorted(my_list, reverse=True)
    return my_list

def func_str_2 (text: str):
    return sorted(list(set(map(ord, text))), reverse=True)

text_1='Мама мыла Милу мыла. Мила мыться не любила.'
# data = func_str(text_1)
print(func_str_2(text_1))