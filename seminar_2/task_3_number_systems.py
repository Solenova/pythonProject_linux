# Задание №3
# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

BIANAR_SYSTEM = 2
OCTAL_SYSTEM = 8

num: int = int(input('\n Введите целое число'))

def system_selection() ->int:
    system: int = 0

    while system!=BIANAR_SYSTEM and system!= OCTAL_SYSTEM:
        system = int(input('\nВберите систему счисления\n'
                           '2- двоичная система счисления'
                           '8 - восьмеричная система счисления'))
    return system

def tranfer_to_system(num: int, system: int) -> str:
    result: str = ''

    while num:
        mod: str = str(num%system)
        result=mod + result
        num //= system


    return result

selection: int = system_selection()
tranfer: str = tranfer_to_system(num,selection)

print(f'Результат {tranfer}')
print(f'Число в двоичной системе счисления: {bin(num)}')
print(f'Число в восьмеричной системе счисления: {oct(num)}')