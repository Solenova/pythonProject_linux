# Задание №4
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.

def task_4():
    my_gen = (i for i in range(0, 100, 2) if (i//10 + i%10) != 8)
    for i in my_gen:
        print(i)
   

print(task_4())