from abc import ABC, abstractmethod

class Person(ABC):
    # constructor
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    # abstract method
    @abstractmethod
    def get_salary(self):
        pass

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

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

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

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    @property
    def bonus(self):
        return self.__bonus

    @bonus.setter
    def bonus(self, value):
        self.__bonus = value

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

# Example usage
c = Employee("C", 21, 600)
print(c)

# Change information using setters
c.name = 'Nguyen Van C'
c.age = 20
c.salary = 650

print('-' * 40 + '\nMY UPDATE INFORMATION\n' + '-' * 40)
print(c)

# Test information for Manager
e = Manager("E", 21, 600, 50)
print(e)

# Change information using setters
e.name = "Tran Thi E"
e.age = 20
e.salary = 650
e.bonus = 60

print('-' * 40 + '\nMY UPDATE INFORMATION\n' + '-' * 40)
print(e)
