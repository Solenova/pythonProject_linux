"""
тесты для задачи:
📌 Создайте класс студента.
    ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
    ○ Названия предметов должны загружаться из файла CSV при создании
      экземпляра. Другие предметы в экземпляре недопустимы.
    ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
    ○ Также экземпляр должен сообщать средний балл по тестам для каждого
      предмета и по оценкам всех предметов вместе взятых.
"""
from student import Student
import doctest
import unittest


class TestDelSymbol(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nsetUpClass method: Runs before all tests...")
        
    def setUp(self) -> None:
        self.first = Student("Ivan Ivanovich Ivanov", "subjects.csv")
        self.first("Math", 4, 80)
        self.first("Math", 5, 90)
        self.first("Math", 5, 90)
        self.first("Math", 4, 80)
        self.first("History", 4, 85)

    def test_name(self):
        self.assertEquals(Student("Ivan Ivanovich Ivanov", "subjects.csv").name, 'Ivan Ivanovich Ivanov')

    def test_subjects(self):
        self.assertEquals(Student("Ivan Ivanovich Ivanov", "subjects.csv").subjects, ['Math', 'Physics', 'Chemistry', 'Russian', 'History', 'Informatics'])

    def test_calc_average(self):
        self.assertEquals(self.first.calc_average_test_score("Math"), 85)

    def test_calc_average_grade(self):
        self.assertEquals(self.first.calc_average_grade(), 4.4)
    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass method: Runs after all tests...")

if __name__ == '__main--':
    unittest.main(verbosity=2)

