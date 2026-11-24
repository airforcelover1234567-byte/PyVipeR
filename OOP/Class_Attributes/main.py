class Person:
    no_of_ppl=0 #This is an attribute of a class and is fixed
    #It does not change like self.name does
    def __init__(self,name):
        self.name=name
p=Person("Jill")
print(Person.no_of_ppl)