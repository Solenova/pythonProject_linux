"""
📌 Создайте класс студента.
    ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
    ○ Названия предметов должны загружаться из файла CSV при создании
      экземпляра. Другие предметы в экземпляре недопустимы.
    ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
    ○ Также экземпляр должен сообщать средний балл по тестам для каждого
      предмета и по оценкам всех предметов вместе взятых.
"""

import csv
import os


class NameValidator:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        if not all(i.isalpha() for i in value.split()):
            raise ValueError("Name should contain only letters.")
        if not all(i.istitle() for i in value.split()):
            raise ValueError("Name should start with an uppercase letter.")
        instance._name = value


class Student:
    name = NameValidator()

    def __init__(self, name, subjects_file):
        self.name = name
        if os.path.exists(subjects_file):
            self.subjects = self.load_sub(subjects_file)
            self.scores = {subject: {"grades": [], "test_results": []} for subject in self.subjects}
        else:
            self.subjects = []
            self.scores = {}

    def load_sub(self, subjects_file):
        with open(subjects_file, 'r') as file:
            reader = csv.reader(file)
            subjects = next(reader)
        return subjects

    def __call__(self, subject, grade, test_result):
        if subject not in self.subjects:
            raise ValueError(f"{subject} is not a valid subject.")
        if grade < 2 or grade > 5:
            raise ValueError("Grade should be between 2 and 5.")
        if test_result < 0 or test_result > 100:
            raise ValueError("Test result should be between 0 and 100.")
        self.scores[subject]["grades"].append(grade)
        self.scores[subject]["test_results"].append(test_result)

    def calc_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"{subject} is not a valid subject.")
        test_results = self.scores[subject]["test_results"]
        if not test_results:
            return 0
        return sum(test_results) / len(test_results)

    def calc_average_grade(self):
        total_grades = []
        total_subjects = 0
        for subject in self.subjects:
            total_grades.extend(self.scores[subject]["grades"])
            total_subjects += len(self.scores[subject]["grades"])
        if not total_grades:
            return 0
        return sum(total_grades) / total_subjects


student = Student("Ivan Ivanovich Ivanov", "subjects.csv")

student("Math", 4, 80)
student("Math", 5, 90)
student("Informatics", 5, 90)
student("Physics", 3, 70)
student("History", 4, 85)

print("Name:", student.name)
print("Subjects:", student.subjects)
print("Math average test score:", student.calc_average_test_score("Math"))
print("Overall average grade:", student.calc_average_grade())
print(student.scores)




#
#
#
#
# class Range:
#     def __init__(self, min_value: int = None, max_value: int = None):
#         self.min_value = min_value
#         self.max_value = max_value
#
#     def __set_name__(self, owner, name):
#         self.param_name = '_' + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.param_name)
#
#     def __set__(self, instance, value):
#         self.validate(value)
#         setattr(instance, self.param_name, value)
#
#     def __delete__(self, instance):
#         raise AttributeError(f'Свойство "{self.param_name}" нельзяудалять')
#
#     def validate(self, value):
#         if not isinstance(value, int):
#             raise TypeError(f'Значение {value} должно быть целымcчислом')
#         if self.min_value is not None and value < self.min_value:
#             raise ValueError(f'Значение {value} должно быть больше 18 или равно {self.min_value}')
#         if self.max_value is not None and value >= self.max_value:
#             raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')
#
#
# class Student:
#     age = Range(3, 103)
#     grade = Range(1, 11 + 1)
#     office = Range(3, 42 + 1)
#
#     def __init__(self, last_name, first_name, first_name, subject):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.first_name = first_name
#         self.subject = subject
#
#     def __repr__(self):
#         return f'Student(name={self.name}, age={self.age}, grade={self.grade}, office={self.office})'
#
#
# if __name__ == '__main__':
#     std_one = Student('Архимед', 12, 4, 29)
#     std_other = Student('Аристотель', 2406, 5, 17) # ValueError: Значение 2406 должно быть меньше 103
#     print(f'{std_one = }')
#     std_one.age = 15
#     print(f'{std_one = }')
#     std_one.grade = 11.0 # TypeError: Значение 11.0 должно быть целым числом
#     std_one.office = 73 # ValueError: Значение 73 должно быть меньше 42
#
#     del std_one.age # AttributeError: Свойство "_age" нельзя удалять
#     print(f'{std_one.__dict__ = }')
