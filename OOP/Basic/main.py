#Python Object-Oriented-Programming

name="Rounak"
age=14

print(type(name)) #This is assigned to a class called 'str'
print(type(age)) #This is assigned to a class called 'int'

class Employee:

    def __init__(self,first,last):
        self.first=first
        self.last=last

emp_1=Employee('Rounak','Roy')
emp_2=Employee('Sounak','Roy')

print(emp_1.first)
print(emp_2.first)