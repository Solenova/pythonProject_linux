# Задание №2
# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

def get_value(diction: dict, key, value_default=None):
    try:
        spam = diction[key]
    except KeyError as exp:
        spam = value_default

    return spam


if __name__ == "__main__":
    eggs_dict = {'one': 1, 'two': 2, 'char': 'k'}

    print(get_value(eggs_dict, 'two'))
    print(get_value(eggs_dict, 'two', 'err'))
    print(get_value(eggs_dict, 'two222', 'err'))
    print(get_value(eggs_dict, 'two222'))