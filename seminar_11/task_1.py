# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
import datetime

class StrPro(str):
    def __new__(cls, name, time_create):
        instance = super().__new__(cls, name)
        instance.name = name
        instance.time_create = datetime.datetime.today()
        return instance


if __name__ == "__main__":
    temp = StrPro('Stroka origin', 'Ivanov')
    print(f'{temp.name},  {temp.time_create}')