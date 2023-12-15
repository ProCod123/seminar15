import logging

logging.basicConfig(filename='student.log', level=logging.DEBUG)


class CustomError(Exception):
    pass


class Student:
    def __init__(self, name, age):
        self.name = name
        if age < 0 or age > 150:
            raise CustomError("Invalid age")
        self.age = age

    def run(self):
        try:
            # Логируем информацию о студенте
            logging.debug(f"Student {self.name} is running")
        except CustomError as e:
            logging.error(f"An error occurred: {e}")


student = Student("Dima", 12)
student.run()