#Python Object-Oriented-Programming

class Employee:

    def __init__(self,first,last):
        self.first=first
        self.last=last

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1=Employee('Rounak','Roy')
emp_2=Employee('Sounak','Roy')

print(emp_1.first)
print(emp_2.first)

print(emp_1.fullname())
print(Employee.fullname(emp_2))