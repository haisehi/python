# Write a Python program to create a Person class including private instance
# attributes: “name” and “age”; a class attribute “count”; a class method “increment_count” 
# (count of how many instances of the class are created), a
# method “greeting()”; a static method “cls_information()” (return information of class) 
# and a method “str()” (return information of an instance)

class Person:
    # class attribute
    count = 0

    # constructor
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Person.increment_count()

    # class method
    @classmethod
    def increment_count(cls):
        cls.count += 1

    # instance method
    def greeting(self):
        print("------Hello------")

    # static method
    @staticmethod
    def cls_information():
        print(f'Class information:\n'
                f'- Class name: {Person.__name__}\n'
                f'- Base Classes: {Person.__bases__}\n'
                f'- Number of Persons: {Person.count}\n'
                + '=' * 40)

    # special method
    def __str__(self):
        return f'My name is {self.__name}\nI am {self.__age} years old'

# Example usage
a = Person("A",19)
b = Person("B",20)
a.greeting()
print(a)
b.greeting()
print(b)
Person.cls_information()

# 1.3 Create Employee class inheriting to Person class with some supplements: an
# instance variable – “salary”; an class varibale – “emp_count”. Finally, let’s
# overide “cls_information” method, “increment_count” and “str()” method

class Employee(Person):
    emp_count =0
    #constructor
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.__salary = salary
        Employee.increment_count()
    #class method
    @classmethod
    def increment_count(cls):
        cls.emp_count +=1
    #overriding - static method
    @staticmethod
    def cls_information():
        print(f'Class information:\n'
              f'- Class name: {Employee.__name__}\n'
              f'- Base Classes: {Employee.__bases__}\n'
              f'- Number of Employee: {Employee.emp_count}\n'
              f'- Number of Person: {Person.count}\n'
              + '=' * 40)

    def __str__(self):
        return super().__str__() + "\nMy salary is " + str(self.__salary) + "\nMY ROLE IS EMPLOYEE"

c = Employee("C", 21, 600)
d = Employee("D", 20, 650)
c.greeting()
print(c)
d.greeting()
print(d)
Employee.cls_information()

# Create Manager class inheriting to Person class with some supplements:
# an instance variable – “salary”; an instance variable – “bonus”; an class
# varibale – “man_count”. Finally, let’s overide “cls_information” method;
# “increment_count” method and “str()” method.

class Manager(Person):
    #class variable
    man_count = 0
    #constructor
    def __init__(self,bonus,salary,name,age):
        super().__init__(name,age)
        self.__salary = salary
        self.__bonus = bonus
        Manager.increment_count()

    #class method
    @classmethod
    def increment_count(cls):
        cls.man_count +=1
    #overriding - static method
    @staticmethod
    def cls_information():
        print(f'Class information:\n'
              f'- Class name: {Manager.__name__}\n'
              f'- Base Classes: {Manager.__bases__}\n'
              f'- Number of Employee: {Manager.man_count}\n'
              f'- Number of Person: {Person.count}\n'
              + '=' * 40)

    def __str__(self):
        return super().__str__() + "\nMy salary is " + str(self.__salary) + "\nMY ROLE IS Manager"

e = Manager("E", 21, 600,50)
f = Manager("F", 20, 650,50)
e.greeting()
print(e)
f.greeting()
print(f)
Manager.cls_information()



