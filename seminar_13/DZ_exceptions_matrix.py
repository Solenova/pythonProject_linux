# 3.Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц
from random import randint
from error import ErrorDimenshionMatrix

class Matrix:
    """класс Matrix  """
    def __init__(self, rows, cols):
        """инициализирует объект класса Matrix с заданным количеством строк и столбцов.
        Матрица заполняется нулями по умолчанию.
        """
        self.rows = rows
        self.cols = cols
        self.data = [[randint(0, 10)] * cols for _ in range(rows)]

    def __str__(self):
        """возвращает строковое представление матрицы в удобочитаемом формате"""
        return '\n'.join([' '.join([str(item) for item in row]) for row in self.data])

    def __add__(self, other):
        """Сложение мтриц. Проверка на корректность. Создание новой матрицы сложением элементов каждой исходной"""

        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ErrorDimenshionMatrix

        result_data = []
        for i in range(len(self.data)):
            row = [self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))]
            result_data.append(row)

        return '\n'.join(' '.join(str(item) for item in row) for row in result_data)
        # return Matrix(len(self.data[0]), len(self.data[0]))

    def __eq__(self, other):
        """Сравнение матриц"""
        return self.rows == other.rows and self.cols == other.cols


if __name__ == "__main__":

    matrix = Matrix(4, 2)

    print(f'{matrix }\n')
    matrix2 = Matrix(4, 2)
    print(f'{matrix2} \n')
    print(matrix + matrix2)
    print(matrix == matrix2)