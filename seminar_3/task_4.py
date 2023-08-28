# Задание №4
# Погружение в Python | Коллекции
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.
TWO=2
my_list = [3, 5, 2, 3, 6, 2, 4, 3]


# for i in my_list:
#     if i not in my_list:
#         my_list.pop(i)
# print(my_list)

#2 method удаляет элемент, встречающийся дважды
# for element in set(my_list):
#     if my_list.count(element) == TWO:
#         for _ in range(TWO):
#             my_list.remove(element)
# print(my_list)