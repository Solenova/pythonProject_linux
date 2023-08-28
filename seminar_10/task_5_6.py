# Задание №5
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.
class Fauna:
    def __init__(self, name, class_fauna, habitat):
        self.name = name
        self.class_fauna = class_fauna
        self.habitat = habitat


class Animal(Fauna):
    def __init__(self, type_foot, name, class_fauna, habitat):
        self.type_foot = type_foot
        super().__init__(name, class_fauna, habitat)

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


if __name__ == "__main__":
    fish = Fish(52, 'стерлядь',  'осетровые',  '52 параллель')
    bird = Birds(2, 'соловей', 'певчие', 'У воды')
    animal = Animal('парнокопытное', 'косуля', 'олени', 'средняя азия')
    print(f'specific fich {fish.specific()}, specific bird {bird.specific()}, {animal.specific()} ')



