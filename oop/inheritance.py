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
        
#internal
class Developer(employee):
    raise_amount = 1.10
    #constructor
    def __init__ (self,para_name,para_email,para_address,para_salary,para_prog_lang):
        super().__init__(para_name,para_email,para_address,para_salary)
        self.prog_lang = para_prog_lang

class Manager(employee):
    raise_amount = 1.10
    #constructor
    def __init__ (self,para_name,para_email,para_address,para_salary,employees = None):
        super().__init__(para_name,para_email,para_address,para_salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_employees(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employees(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_employees(self):
        for emp in self.employees:
            print("--->"+emp.name)

    
    
emp_1 = employee("Huy","h@gmail.com","VietNam",5000)
emp_2 = employee("bb","b@gmail.com","USA",6000)

#inheritance
dev_1 = Developer("Kaka","k@gmail.com","VietNam",5000,"python")
dev_2 = Developer("bdd","bdd@gmail.com","USA",6000,"java")

print(dev_1.email+" ,"+dev_1.prog_lang)
print(dev_2.email+" ,"+dev_2.prog_lang)

mgr_1 = Manager("Coconout","coco@gmail.com","VietNam",5000,[dev_1])
print(mgr_1.email)
mgr_1.add_employees(dev_2)
mgr_1.remove_employees(dev_1)
mgr_1.print_employees()