# 3. В большой текстовой строке подсчитать количество
# встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью
# из википедии или из документации к языку.
import re

f = open('mytext.txt', 'r', encoding='utf-8')
my_text = f.read()

f.close()

def stringToList(string):
     my_str = re.sub(r'[^a-zA-Zа-яА-Я ]+', '', string.lower())
     list_res = list(my_str.split())
     return list_res

def creat_dict(my_list):
    my_dict = {}
    for item in my_list:
        my_dict[item] = my_list.count(item)
    return my_dict

print(stringToList(my_text))
# my_list = stringToList(my_text)
my_dict = creat_dict(stringToList(my_text))
dict_res = {}
for i in range(10):
    dict_res[i] = max(my_dict, key=my_dict.get)
    my_dict.pop(max(my_dict, key=my_dict.get))
# форма записи ниже представляет список кортежей ключ, значение в порядке убывания зачений
# dict_res = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
print(f'В тексте чаще всего встречаются:  {dict_res}')

