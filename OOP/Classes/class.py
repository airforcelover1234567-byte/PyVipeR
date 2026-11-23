class Dog:
    def __init__(self,name,breed): #It is used to instantiate an object when it is created
        self.name=name
        self.breed=breed
        print(name,breed)
        
    def meow(self,x):
        return "meow",x+1

    def bark(self):
        print("Bark")

d=Dog("Shiro","Golden Retriever")
