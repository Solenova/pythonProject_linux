# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключoм для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.
import json
from pathlib import Path


def set_user(file: Path) -> None:
    unique_id = set()   #заводим множество, т.к. имена должны быть идентичными
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)                 # преобразовали в объект python, в строку
            for _, value in data.items():
                unique_id.update(value.keys())
    else:
        data = {str(i): {} for i in range(1, 7 + 1)}

    while True:
        name = input('Name: ')
        if not name:
            break
        id = input('ID: ')
        level = input('Level [1, 7]: ')

        if id in unique_id and data[level].get(id) is None:
            continue
        data[level].update({id: name})
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    set_user(Path('users.json'))

#  # 2 method
# def fill_bd(file: Path):
#     current_set = set()
#
#     if Path.exists(file):
#         with open(file, 'r', encoding='utf-8') as fj:
#             dict_bd = json.load(fj)
#             for _, value in dict_bd.items():
#                 current_set.update(value.keys())
#     else:
#         dict_bd = {i: {} for i in range(1, 8)}
#
#         current_data = input(
#             f'РІРІРµРґРёС‚Рµ РРјСЏ, id, СѓСЂРѕРІРµРЅСЊ РґРѕСЃС‚СѓРїР° (РѕС‚ 1 РґРѕ 7) С‡РµСЂРµР· РїСЂРѕР±РµР»: \n ')
#         while current_data != "":
#             name, id_cod, level = current_data.split()
#
#             if id_cod not in current_set:
#                 current_set.add(id_cod)
#                 dict_bd[int(level)] = {id_cod: name}
#
#                 with open(file, "w", encoding='utf-8') as fj:
#                     json.dump(dict_bd, fj, indent=2, ensure_ascii=False)
#
#             current_data = input(
#                 f'РІРІРµРґРёС‚Рµ РРјСЏ, id, СѓСЂРѕРІРµРЅСЊ РґРѕСЃС‚СѓРїР° (РѕС‚ 1 РґРѕ 7) С‡РµСЂРµР· РїСЂРѕР±РµР»: \n ')
