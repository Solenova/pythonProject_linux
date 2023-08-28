# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра
# Задание №4
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

class Archive:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.list_archive = []
            cls._instance.list_archive.append([args])

        cls._instance.list_archive.append([args])
        return cls._instance

    def __init__(self, text: str, num: int):
        self.text = text
        self.num = num

    def __str__(self):
        return f'текст строки {self.text}, число строки {self.num}, список значений экземпляров класса "{self.list_archive}"'

    def __repr__(self):
        return f'text {self.text}, string {self.num}, List {self.list_archive}'

if __name__ == "__main__":
    temp = Archive('Stroka origin', 65)
    print(f'{temp}')

    temp2 = Archive('ночной дозор', 1555)
    print(f'{temp2 =},  {temp2.text =}')

    temp3 = Archive('cnhf;b', 84)
    print(f'{temp3.num},  {temp3.text}, {temp3.list_archive}')