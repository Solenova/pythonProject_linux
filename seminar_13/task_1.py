# Задание №1
# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

def Float_num():
    temp = None
    while True:
        try:
            temp = float(input(f'введите целое число '))
        except ValueError as e:
            print(f'input number int | float')
        else:
            return temp


if __name__ == "__main__":
    print(Float_num())