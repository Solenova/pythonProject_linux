# Задание №8
# Погружение в Python | Коллекции
# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей

friends_things = {
    'друг 1': ('Рюкзак', 'Палатка', 'Фонарик', 'Котелок'),
    'друг 2': ('Палатка', 'Фонарик', 'Рюкзак', 'Гитара'),
    'друг 3': ('Рюкзак', 'Палатка', 'Аптечка', 'Компас'),
}
# какие вещи взяли все три друга
un_items = set.intersection(set(friends_things['друг 1']), set(friends_things['друг 2']), set(friends_things['друг 3']))
print(un_items)

# список всех вещей
all_items = set.union(set(friends_things['друг 1']), set(friends_things['друг 2']), set(friends_things['друг 3']))
print(all_items)
#уникальные элементы, получились которые не у всех

unique_items = all_items.difference(un_items)
#
# print(unique_items)
# #какие вещи есть у всех кроме одного
# # count = 0
# # list_res = ()
# # for item in friends_items.values():
# #     for i in range(len(friends_items)):
# #         if item in :
# #             count+=1
# #     if count == 1:
# #         list_res.append(item)
# # print(list_res)
#
#
# list_res = []
# data_items = friends_things.items()
# print(data_items)
# for item in data_items:
#     count = 0
#     for i in item[2]:
#         if i in item:
#                count += 1
#         if count == 1:
#             list_res.append(i)
# print(list_res)

