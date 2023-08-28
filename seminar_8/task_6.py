# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 5 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import csv
import pickle
from pathlib import Path


def conv_to_csv(file_name: Path) -> None:
    with (open(file_name, 'rb') as f_pickle,
          open(f'{file_name.stem}.csv', "w", newline='', encoding='utf-8') as f_csv):
        new_dict = pickle.load(f_pickle)

        csv_write = csv.DictWriter(
            f_csv,
            fieldnames=list(new_dict.keys()),   #ключи это названия столбцов
            dialect='excel',
            delimiter=',',
            quoting=csv.QUOTE_NONNUMERIC)

        csv_write.writeheader()
        csv_write.writerows([new_dict])

#-----------------2 method
# def conv_to_csv(file_name: Path) -> None:
#     with (open(file_name, 'rb') as f_pickle,
#           open(f'{file_name.stem}.csv', "w", newline='', encoding='utf-8') as f_csv):
#         new_dict = pickle.load(f_pickle)
#
#         csv_write = csv.writer(
#             f_csv,
#             dialect='excel',
#             delimiter=',',
#             )
#         csv_write.writerow(new_dict.keys()) #ключи это названия столбцов
#
#         n = [str(i).split() for i in new_dict.values()]
#         csv_write.writerows([n])

if __name__ == "__main__":
    conv_to_csv(Path("new_user.pickle"))