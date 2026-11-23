class Dog:
    def __init__(self): #It is used to instantiate an object when it is created
        print("I am a good boy")
        
    def meow(self,x):
        return "meow",x+1

    def bark(self):
        print("Bark")

d=Dog()
d.bark()
print(d.meow(5))
print(type(d))