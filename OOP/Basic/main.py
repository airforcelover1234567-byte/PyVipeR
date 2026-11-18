#Python Object-Oriented-Programming

name="Rounak"
age=14

print(type(name)) #This is assigned to a class called 'str'
print(type(age)) #This is assigned to a class called 'int'

class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

    def bark(self):
        print("Whoof Whoof")

dog1=Dog("Bozo","Golden Retriever")
dog1.bark()
print(dog1)
