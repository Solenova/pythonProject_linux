# 4. Создайте словарь со списком вещей для похода в качестве ключа
# и их массой в качестве значения. Определите какие вещи влезут в рюкзак
# передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

MAX_WEIGHT = 25

dict_inventory = {
    "Палатка": 7,
    "Спальный мешок": 3,
    "Котелок": 1.5,
    "Продукты": 7,
    "Топор": 2,
    "Нож": 0.1,
    "Компас": 0.08,
    "Фонарь": 0.5,
    "Спрей от насекомых": 0.2,
    "Аптечка": 0.6,
    "Пауербанк": 0.5,
    "Гитара": 1.5,
    "Непромокаемые спички": 0.08,
    "Запасная одежда": 3,
    "Кружка": 0.3,
    "Туалетные принадлежности": 0.2,
    "necn": 5
}

while True:
    summ_value = sum(dict_inventory.values())
    if summ_value > MAX_WEIGHT:
        dict_inventory.popitem()
    else:
        break
if summ_value >= 0:
    print(f'Вы можете взять')
    for key in dict_inventory.keys():
        print(f'{key}', end='/')
else:
    print('Вам не стоит идти в поход. Предельный вес не позволяет взять с собой вещи')