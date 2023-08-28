# Задание №3
# Создайте класс с базовым исключением и дочерние классы исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class BaseExcept(Exception):
    pass


class ErrorLevel(BaseExcept):
    pass


class ErrorAccept(BaseExcept):
    pass


try:
    raise ErrorLevel('ошибка уровня')
except ErrorLevel as exp:
    print(f'Error: {exp}')

try:
    raise ErrorAccept('ошибка доступа')
except ErrorAccept as exp:
    print(f'Error: {exp}')
