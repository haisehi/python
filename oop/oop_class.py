#class
class employee:
    #field
    id =1
    raise_amount = 1.04
    #constructor
    def __init__ (self,para_name,para_email,para_address,para_salary):
        self.name = para_name
        self.email = para_email
        self.address = para_address
        self.salary = para_salary

        self.stt = employee.id
        employee.id +=1
    #method
    def output(self):
        return '{}. I''''''''m {} on {} ,my address is {}, salary {} usd'.format(self.stt,self.name,self.email,self.address,str(self.salary))
    #method
    def apply_raise(self):
        self.salary = int(self.salary * employee.raise_amount)
    #class methods
    @classmethod
    def set_raise_amount(cls, amount): #trong phương thức này làm việc với class thay vì instances variable
        cls.raise_amount = amount
    #alternative constructor
    @classmethod
    def from_string(cls, str_emplyee):
        name,email,address,salary = str_emplyee.split('-')
        return cls(name,email,address,salary)
    #static method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
    
emp_1 = employee("Huy","h@gmail.com","VietNam",5000)
emp_2 = employee("bb","b@gmail.com","USA",6000)

print("salary employee 1:"+ str(emp_1.salary)+" usd")
employee.set_raise_amount(1.05)
emp_1.apply_raise()
print(emp_1.output())
print(emp_1.raise_amount)

print(emp_2.output())
print(emp_2.__dict__)

#alternative constructor
new_employee_1 = employee.from_string("John-john@gmail.com-UK-70000")
print(new_employee_1)
print(new_employee_1.name)
print(new_employee_1.email)
print(new_employee_1.address)
print(new_employee_1.salary)

#static method
import datetime
my_date = datetime.date(2024,3,5)
print(employee.is_workday(my_date))
