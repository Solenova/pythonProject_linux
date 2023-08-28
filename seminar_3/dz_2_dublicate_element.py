# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.
from random import choices
TWO=2
my_list = [3, 5, 2, 3, 6, 2, 4, 3, 3, 3]

my_list_2 = []
for i in my_list:
    if i not in my_list_2 and my_list.count(i) >=2:
        my_list_2.append(i)
print(my_list_2)

# 2 metod через множество
# count = int(input())
# list_nums = choices(range(1, count * 2), k=count)
#
# print(list_nums)
#
# res_list = set()
# for i in list_nums:
#     if list_nums.count(i) > 1:
#         res_list.add(i)
#
# print(res_list)
