# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

def dict_tarif(my_name: list[str], my_tarif: list[int], my_prize: list[str]) -> dict[str, float]:
    my_dict = {}
    for n, t, p in zip(my_name, my_tarif, my_prize):
       my_dict[n] = round(t*float(p[:-1])/100, 2)

    return my_dict
my_name = ['Ivanov', 'Petrova', 'Jonson', 'Yo']
my_tarif = [22_120, 24_654, 28_985, 23_354]
my_prize = ['15%', '10.25%', '17.5%', '23%']

print(dict_tarif(my_name, my_tarif, my_prize))