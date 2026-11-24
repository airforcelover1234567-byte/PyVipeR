def menu():
    print("=====WELCOME TO SPACECRAFTS=====")
    print("Choose spacecraft type:\n1. Fighter\n2. Cargo Ship\n3. Exploration Ship")

class Spacecrafts:
    def __init__(self):
        self.name=str(input("Enter name ship: "))
        self.fuel=int(input("Enter fuel capacity of ship: "))
        self.speed=int(input("Enter max speed of ship: "))

    def ship_info(self):
        print(f"Name:{self.name}")
        print(f"Fuel:{self.fuel}")
        print(f"Speed:{self.speed}")

class Fighter_Ship(Spacecrafts):
    def __init__(self):
        super().__init__()
        self.power=int(input("Enter power of Fighter: "))
        self.ammo=int(input("Enter maximum ammo of fighter: "))
        print(f"{self.name} has been created!")

    def attack(self):
        self.ammo-=100
        print("You used 100 ammo")

    def weapon_info(self):
        print(f"Power:{self.power}")
        print(f"Ammo:{self.ammo}")

class Cargo_Ship(Spacecrafts):
    def __init__(self):
        super().__init__()
        self.cargo_capacity=int(input("Enter cargo capacity of Ship: "))
        self.current_cargo=int(input("Enter current cargo: "))
        if self.current_cargo>self.cargo_capacity:
            print("Cargo cannot be bigger than capacity")

    def cargo_load(self):
        self.unload=int(input("Enter amount for unloading: "))
        self.current_cargo-=self.unload
        return self.current_cargo

    def cargo_load(self):
        self.load=int(input("Enter amount for loading: "))
        self.current_cargo+=self.load
        return self.current_cargo

    def cargo_info(self):
        print(f"Cargo:{self.current_cargo}")

    def emergency(self):
        if self.load+self.current_cargo>self.cargo_capacity:
            print("Cargo exceeded Capacity")
            self.load+self.current_cargo==self.current_cargo+self.load-self.cargo_capacity
            return self.load

class Exploration_Ship(Spacecrafts):
    def __init__(self):
        super().__init()
        self.scan=int(input("Enter your scanning range: "))
        

    
menu()
choice=int(input("Enter the type of Spacecraft: "))

match choice:
    case 1:
        player=Fighter_Ship()
    case 2:
        player=Cargo_Ship()
    case 3:
        player