# Задание №5
# ✔ Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.

a = float(input('\nвведите число a: '))
b = float(input('\nвведите число b: '))
c = float(input('\nвведите число c: '))

d = b**2 - 4 * a * c
result = ''

if d > 0:
    x1 = (-b + d**0.5)/(2 * a)
    x2 = (-b - d**0.5)/(2 * a)
    result = f'\n два корня: {(x1, x2)}'

elif d == 0:
    x = -b/(2 * a)
    result = f'\n один корень: {(x)}'

else:
    d = complex(d, 0)
    x1 = (-b + d**0.5)/(2 * a)
    x2 = (-b - d**0.5)/(2 * a)
    result = f'\nдва комплексных корня: {(x1, x2)}'

print(result)