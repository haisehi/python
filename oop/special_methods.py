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
    
emp_1 = employee("Huy","h@gmail.com","VietNam",5000)
emp_2 = employee("bb","b@gmail.com","USA",6000)

    