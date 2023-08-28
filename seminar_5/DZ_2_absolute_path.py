# 2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def absolute_path(link: str):

    path, suffix = link.rsplit('/', 1)
    name_file, ext_file = suffix.split(".", 1)
    return path, name_file, f".{ext_file}"

link = 'jetbrains://pycharm/navigate/reference?project=pythonProject&path=seminar_5/task_1.py'
path, filename, file_extension = absolute_path(link)
print("Путь:", path)
print("Имя файла:", filename)
print("Расширение файла:", file_extension)
