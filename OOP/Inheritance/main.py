class Pet:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

    def show(self):
        print(f"I am {self.name}. My breed is {self.breed}")

class Cat(Pet):
    def __init__(self,name,breed,color):
        super().__init__(name,breed)
        self.color=color

    def meow(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} {self.breed} {self.color}")

class Dog(Pet):
    def bark(self):
        print("Bark")

p=Pet("Bill","Golden Retriever")
p.show()
c=Cat("Tim","Labrador","Brown")
c.show()