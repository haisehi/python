#class
class employee:
    #constructor
    def __init__ (self,para_name,para_lastname):
        self.name = para_name
        self.lastname = para_lastname
    
    @property
    def email(self):
        return '{}{}@email.com'.format(self.name,self.lastname)
    #method
    @property
    def fullname(self):
        return '{} {}'.format(self.name,self.lastname)
    #getter and setter
    @fullname.setter
    def fullname(self,fullname):
        name, lastname = fullname.split(' ')
        self.name = name
        self.lastname = lastname

    @fullname.deleter
    def fullname(self):
        print("delete fullname")
        self.name = None
        self.lastname = None

emp_1 = employee("Huy","Quang")
emp_2 = employee("bb","d")

emp_1.fullname = "Ryze championships"
print(emp_1.fullname)
print(emp_1.email)
print(emp_2.fullname)
print(emp_2.email)

del emp_1.fullname