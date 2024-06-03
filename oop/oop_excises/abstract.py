# Change Person class to abstract class by creating abstract methods:
# “increment_count”, “cls_information”, “get_salary()”. Then, let’s definite these
# method in Employee class and Manager class

from abc import ABC, abstractmethod

class Person(ABC):
    # constructor
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # abstract method
    @abstractmethod
    def get_salary(self):
        pass

    # class method (not used in Person, but defined to be overridden)
    @classmethod
    def increment_count(cls):
        pass

    # static method
    @staticmethod
    def cls_information():
        pass

    # special method
    def __str__(self):
        return '-' * 40 + '\nHello' + '\nMy name is ' + self.__name + "\nI am " + str(self.__age) + " years old"

class Employee(Person):
    # Class variable
    emp_count = 0

    # constructor
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.__salary = salary
        Employee.increment_count()

    # class method
    @classmethod
    def increment_count(cls):
        cls.emp_count += 1

    # overriding - get_salary() method
    def get_salary(self):
        return self.__salary

    # overriding - static method
    @staticmethod
    def cls_information():
        print('=' * 40 + '\nClass information: \n- Class name: ' + str(Employee.__name__) + '\n- Base Classes: ' + str(Employee.__bases__) + '\n- Number of Employees: ' + str(Employee.emp_count))

    # overriding special method
    def __str__(self):
        return super().__str__() + "\nMy salary is " + str(self.__salary) + "\nMy total salary is " + str(self.get_salary()) + "\nMY ROLE IS EMPLOYEE"

class Manager(Person):
    # Class variable
    man_count = 0

    # constructor
    def __init__(self, name, age, salary, bonus):
        super().__init__(name, age)
        self.__salary = salary
        self.__bonus = bonus
        Manager.increment_count()

    # class method
    @classmethod
    def increment_count(cls):
        cls.man_count += 1

    # overriding - get_salary() method
    def get_salary(self):
        return self.__salary + self.__bonus

    # overriding - static method
    @staticmethod
    def cls_information():
        print('=' * 30 + '\nClass information: \n- Class name: ' + str(Manager.__name__) + '\n- Base Classes: ' + str(Manager.__bases__) + '\n- Number of Managers: ' + str(Manager.man_count))

    # overriding special method
    def __str__(self):
        return super().__str__() + "\nMy salary is " + str(self.__salary) + "\nBonus is " + str(self.__bonus) + "\nMy total salary is " + str(self.get_salary()) + "\nMY ROLE IS MANAGEMENT"

 # Two objects from Employee class
c = Employee("C", 21, 600)
d = Employee("D", 20, 650)
print(c)
print(d)
Employee.cls_information()
# Two objects from Manager class
e = Manager("E", 21, 600,50)
f = Manager("F", 20, 650,50)
print(e)
print(f)
Manager.cls_information()