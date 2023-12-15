import logging
import csv

logging.basicConfig(filename='student.log', level=logging.DEBUG)


class CustomError(Exception):
    pass


class Student:

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', newline='') as file:
            reader = csv.reader(file)
            subjects_list = next(reader)
            for subject in subjects_list:
                self.subjects[subject] = {'grades': [], 'test_scores': []}   

    def __setattr__(self, name, value):
        if name == 'name':
            if not value.istitle() and not value.isalpha():
                print("ФИО должно состоять только из букв и начинаться с заглавной буквы")
                return
        super().__setattr__(name, value)

    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        else:
            print(f"Предмет {name} не найден")


    def __str__(self):
        active_subject = []
        for i in self.subjects:
            if len(self.subjects[i]['grades']) != 0:
                active_subject.append(i)
        return f'Студент: {self.name}\nПредметы: {", ".join(active_subject)}'

    def add_grade(self, subject, grade):
        if grade in range(2, 6):
            self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        if test_score in range(101):
            self.subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        try:
            if self.subjects[subject]['test_scores']:
                return sum(self.subjects[subject]['test_scores']) / len(self.subjects[subject]['test_scores'])
            else:
                return 0
        except KeyError:
            raise ValueError(f'Предмет {subject} не найден')

    def get_average_grade(self):
        total_grades = []
        for subject in self.subjects:
            total_grades.extend(self.subjects[subject]['grades'])
        if total_grades:
            return sum(total_grades) / len(total_grades)
        else:
            return 0

    def run(self):
        try:
            # Логируем информацию о студенте
            logging.debug(f"Student {self.name} is running")
        except CustomError as e:
            logging.error(f"An error occurred: {e}")



student = Student("Ivan Ivanov", "subjects.csv")
student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)


student.run()