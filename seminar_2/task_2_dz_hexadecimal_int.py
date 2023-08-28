# 2. Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.

BIANAR_SYSTEM = 2
OCTAL_SYSTEM = 8
HEX_SYSTEM = 16

num: int = int(input('\n Введите целое число'))

def system_selection() ->int:
    system: int = 0

    while system!=BIANAR_SYSTEM and system!= OCTAL_SYSTEM and system!= HEX_SYSTEM:
        system = int(input('\nВыберите систему счисления\n'
                           '2- двоичная система счисления'
                           '8 - восьмеричная система счисления'
                           '16 - шестнадцатиричная система счисления'))
    return system

def tranfer_to_system_bin_oct(num: int, system: int) -> str:
    result: str = ''

    while num:
        mod: str = str(num%system)
        result = mod + result
        num //= system


    return result

def tranfer_to_system_hex(num: int, system: int) -> str:
    result: str = ''
    hexadecimal_digits = "0123456789ABCDEF"
    while num :
        mod: int = int(num % system)
        hexadecimal_digit = hexadecimal_digits[mod]
        result = hexadecimal_digit + result
        num //= system

    return result

selection: int = system_selection()
if selection != 16:
    tranfer: str = tranfer_to_system_bin_oct(num,selection)
else:
    tranfer: str = tranfer_to_system_hex(num,selection)

print(f'Результат {tranfer}')
print(f'Число в двоичной системе счисления: {bin(num)}')
print(f'Число в восьмеричной системе счисления: {oct(num)}')
print(f'Число в шестнадцатиричной системе счисления: {hex(num)}')


