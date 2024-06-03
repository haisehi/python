# Write a Python class Teacher inherited from abstract class Person to manage information of teachers with some supplementing attributes: TeachingClasses, TeachingHours, SalaryPerHour and some overiding methods:
# “increment_count”, “cls_information”, “get_salary()” in which salary is
# computed as follows: Salary=SalaryPerHour * TeachingHours

from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_salary(self):
        pass

    @classmethod
    def increment_count(cls):
        pass

    @staticmethod
    def cls_information():
        pass

class Teacher(Person):
    _teacher_count = 0

    def __init__(self, name, teaching_classes, teaching_hours, salary_per_hour):
        self.id = Teacher._teacher_count + 1
        Teacher._teacher_count += 1
        self.name = name
        self.teaching_classes = teaching_classes
        self.teaching_hours = teaching_hours
        self.salary_per_hour = salary_per_hour

    @classmethod
    def increment_count(cls):
        cls._teacher_count += 1

    @staticmethod
    def cls_information():
        print(f"Total number of teachers: {Teacher._teacher_count}")

    def get_salary(self):
        return self.teaching_hours * self.salary_per_hour

    def __str__(self):
        return (f"Teacher ID: {self.id}, Name: {self.name}, "
                f"Teaching Classes: {self.teaching_classes}, "
                f"Teaching Hours: {self.teaching_hours}, "
                f"Salary Per Hour: {self.salary_per_hour}, "
                f"Total Salary: {self.get_salary()}")

# Example usage
if __name__ == "__main__":
    teacher1 = Teacher("Alice", ["Math", "Science"], 30, 50)
    teacher2 = Teacher("Bob", ["History"], 25, 60)

    print(teacher1)
    print(teacher2)

    Teacher.cls_information()
