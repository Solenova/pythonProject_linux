# Задание №3
# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.
import json
import os.path
from typing import Any, Callable


def fun_log(func: Callable) -> Callable[..., None]: # ... т.к. указываем args and kwargs
    def wrapper(*args, **kwargs):
        res_dict = {}
        name = f"{func.__name__}.json" #имя файла json задаем такое же как и имя функции
        if os.path.exists(name):        #проверяем, есть ли файл, который открываем
            with open(name, encoding="utf-8") as json_f:    #по умолчанию режим чтение
                if json_f.read():
                    json_f.seek(0)
                    res_dict = json.load(json_f)

        with open(name, "w", encoding="utf-8") as json_f:
            res_dict[str(args)] = args
            res_dict.update(**kwargs)
            res_dict[f"func:{args}"] = func(*args, **kwargs)
            json.dump(res_dict, json_f, indent=2, ensure_ascii=False)

    return wrapper


@fun_log
def get_all(*args, **kwargs) -> tuple[tuple[Any, ...], dict[str, Any]]:
    return args, kwargs


if __name__ == '__main__':
    get_all(4, 11, "s", a=420, h=60)
    get_all(43, 31, "ts", a=120, h=67)