class Dog:
    def __init__(self,name): #It is used to instantiate an object when it is created
        self.name=name
        
    def meow(self,x):
        return "meow",x+1

    def bark(self):
        print("Bark")

d=Dog("Shiro")
print(d.name)