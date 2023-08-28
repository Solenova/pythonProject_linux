# 1.Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.


class Fauna:
    def __init__(self, name, class_fauna, habitat):
        self.name = name
        self.class_fauna = class_fauna
        self.habitat = habitat


class Animal(Fauna):
    def __init__(self, type_foot, *args, **kwargs):
        self.type_foot = type_foot
        super().__init__(*args, **kwargs)

    def specific(self):
        return f'Тип конечностей {self.type_foot}'


class Fish(Fauna):
    def __init__(self, water_level: int, name: str, class_fauna: str, habitat: str):
        super().__init__(name, class_fauna, habitat)
        self.water_level = water_level

    def specific(self):
        return f'Глубина обитания {self.water_level}'


class Birds(Fauna):
    def __init__(self, flight_duration, name, class_fauna, habitat):
        super().__init__(name, class_fauna, habitat)
        self.flight_duration = flight_duration

    def specific(self):
        return f'Длительность полета {self.flight_duration}'


class FaunaFactory:
    def __init__(self):
        self.fauna_classes = {
            'Fish': Fish,
            'Animal': Animal,
            'Birds': Birds,
       }

    def create_fauna(self, fauna_type, *args):
        if fauna_type not in self.fauna_classes:
            raise ValueError("Invalid animal type")

        fauna_class = self.fauna_classes[fauna_type]
        return fauna_class(*args)


if __name__ == "__main__":
    factory = FaunaFactory()

    fish = factory.create_fauna('Fish', 52, 'стерлядь',  'осетровые',  '52 параллель')
    bird = factory.create_fauna('Birds', 2, 'соловей', 'певчие', 'У воды')
    animal = factory.create_fauna('Animal', 'парнокопытное', 'косуля', 'олени', 'средняя азия')
    print(fish.specific())
    print(bird.specific())
    print(animal.specific())



#
#
# if __name__ == "__main__":
#     fish = Fish(52, 'стерлядь',  'осетровые',  '52 параллель')
#     bird = Birds(2, 'соловей', 'певчие', 'У воды')
#     animal = Animal('парнокопытное', 'косуля', 'олени', 'средняя азия')
#     print(f'specific fich {fish.specific()}, specific bird {bird.specific()}, {animal.specific()} ')
