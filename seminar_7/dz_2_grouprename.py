# 2.Напишите функцию группового переименования файлов. Она должна:
# * -- принимать параметр желаемое конечное имя файлов.
#      При переименовании в конце имени добавляется порядковый номер.
# * -- принимать параметр количество цифр в порядковом номере.
# * -- принимать параметр расширение исходного файла.
#       Переименование должно работать только для этих файлов внутри каталога.
# * -- принимать параметр расширение конечного файла.
# * -- принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os

def group_rename(file_origin: str, count_num: int, extension: str, extension_new: str, list_name: list = None):

         # Получаем список всех файлов в текущем каталоге
     files = [f.split(extension)[0] for f in os.listdir('.')
              if os.path.isfile(f) and f.endswith(extension)]

     # Проверяем, что файлы присутствуют
     if not files:
         print("Файлы с заданным расширением не найдены.")
         return

     # Перебираем файлы и переименовываем их
     for i, file in enumerate(files, 1):
         # Извлекаем часть имени в соответствии с диапазоном
         if list_name:
             start, end = list_name
             base_name = file[start - 1:end]

         # Собираем новое имя файла . 0-значение по умолчанию
         new_name = base_name + file_origin + f"{i:0{count_num}}" + extension_new

         # Переименовываем файл
         os.rename(f'{file}{extension}', new_name)
         print(f"Переименован файл {file} в {new_name}")


group_rename("_new", 6, ".doc", ".txt", list_name=[3, 6])
