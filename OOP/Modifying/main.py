class Car:
    def __init__(self,engine,name,speed):
        self.engine=engine
        self.name=name
        self.speed=speed

    def accelerate(self):
        self.speed+=5
        return self.speed

    def new_speed(self,speed):
        self.speed=speed
        return speed

car1=Car("v8","Chiron",10)
car2=Car("w16","Lamborghini",20)
print(car1.accelerate())
print(car2.speed)
print(car2.new_speed(9))

