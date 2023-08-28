# 3. Напишите однострочный генератор словаря, который принимает на вход
# три списка одинаковой длины: имена str, ставка int, премия str
# с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и
# суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии


def tarif_praiz_generator(names, tarif, prize):
    return {n: t * float(p.rstrip("%")) / 100
            for n, t, p in zip(names, tarif, prize)}



my_list_name = ["Alex", "Mery", "Dimon"]
my_list_tarif = [20_000, 30_000, 10_000]
my_list_prize = ["10%", "2.5%", "10.75%"]

print(tarif_praiz_generator(my_list_name, my_list_tarif, my_list_prize))