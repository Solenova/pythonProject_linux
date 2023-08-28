# Задание №2
# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях

def task_2():
    current_str: str = input(f'введите строку: \n')

    if current_str.isdigit():   #проверяем все символы цифры или нет #если все цифры, то возвращаем число int
        return int(current_str)
    elif current_str.replace('.', '', 1).isdigit():     #убираем точку, проверяем остальные цифры или нет
        return float(current_str)
    elif current_str[0] == '-' and current_str.replace('-', '', 1).isdigit():
        return float(current_str)
    elif current_str.lower() != current_str:
        return current_str.lower()
    else:
        return current_str.upper()

print(task_2())