# Задание №3
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

my_list = [23, 'Hello', 23.3, [58, 4, 4]]
my_dict = {}
# for i in range(len(my_list)):
#     my_dict[i+1] = my_list[i]

# 2 method
for item in my_list:
    k = my_dict.setdefault(type(item).__name__, [])
    k.append(item)

print(my_list, my_dict)