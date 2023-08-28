# Задание №3
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

class GeneratorFactor:

    def __init__(self, *args):

        match len(args):
            case 1:
                self.start = 1
                self.stop = args[0]
                self.step = 1
            case 2:

                self.start, self.stop = args
                self.step = 1
            case 3:
                self.start, self.stop, self.step = args

    def __iter__(self):
        return self

    def __next__(self):

        while self.start < self.stop:
            res = 1
            for item in range(1, self.start + 1):
                res *= item
            self.start += self.step
            return res
        raise StopIteration


if __name__ == "__main__":
    factor = GeneratorFactor(5)
    for item in factor:
        print(item)