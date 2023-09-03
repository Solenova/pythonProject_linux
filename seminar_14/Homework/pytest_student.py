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
from seminar_14.Homework.student import Student
from student import Student
import pytest


@pytest.fixture
def data() -> Student:
    st = Student("Ivan Ivanovich Ivanov", "subjects.csv")
    return st


@pytest.fixture
def set_data(data):
    data("Math", 4, 80)
    data("Math", 5, 90)
    data("Math", 5, 90)
    data("Math", 4, 80)
    data("History", 4, 85)


def test_name():
    assert Student("Ivan Ivanovich Ivanov", "subjects.csv").name == 'Ivan Ivanovich Ivanov'


def test_subjects():
    assert Student("Ivan Ivanovich Ivanov", "subjects.csv").subjects == \
           ['Math', 'Physics', 'Chemistry', 'Russian', 'History', 'Informatics']


def test_calc_average(data, set_data):
    assert data.calc_average_test_score("Math") == 85


def test_calc_average_grade(data, set_data):
    assert data.calc_average_grade() == 4.4


if __name__ == '__main--':
    pytest.main(['-v'])