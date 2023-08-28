# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.

import csv
import pickle
from pathlib import Path


# ---------------------------------- 1 вариант

def print_pickl_str(file_name: Path) -> None:
    with open(file_name, "r", newline='', encoding='utf-8') as f_csv:
        print(pickle.dumps(f_csv.read()))
        # print(len(str(pickle.dumps(f_csv.read())).split(",")))
#считываент строку (строку можно без проблем преобразовать с помощью damps в pickle)
if __name__ == "__main__":
    print_pickl_str(Path("new_user.csv"))


# ---------------------------------- 2 вариант

def csv2pickles(file: Path) -> None:
    pickle_list = []
    with open(file, 'r', newline='', encoding='utf-8') as f:
        csv_file = csv.reader(f, dialect='excel-tab')
        for i, line in enumerate(csv_file):
            if i == 0:
                pickle_keys = line
            else:
                pickle_dict = {k: v for k, v in zip(pickle_keys, line)}
                pickle_list.append(pickle_dict)

    print(pickle.dumps(pickle_list))


if __name__ == '__main__':
    csv2pickles(Path('new_user.csv'))