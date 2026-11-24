import random

def menu():
    print("=====WELCOME TO SPACECRAFTS=====")
    print("Choose spacecraft type:\n1. Fighter\n2. Cargo Ship\n3. Exploration Ship")

def fighter_menu():
    print("1.Attack  2.Weapon Info")

def cargo_menu():
    print("1.Unload  2.Load  3.Cargo Info")

def explore_menu():
    print("1.Planet Scan  2.Discovery")

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

    def cargo_unload(self):
        self.unload=int(input("Enter amount for unloading: "))
        self.current_cargo-=self.unload
        return self.current_cargo

    def cargo_load(self):
        self.load=int(input("Enter amount for loading: "))
        self.current_cargo+=self.load
        if self.current_cargo>self.cargo_capacity:
            print("Cargo exceeded Capacity")
            self.current_cargo==self.current_cargo-self.cargo_capacity
            return self.current_cargo

    def cargo_info(self):
        print(f"Cargo:{self.current_cargo}")

class Exploration_Ship(Spacecrafts):
    def __init__(self):
        super().__init__()
        self.scan=100000
        self.planet_list=[
    "Nyxara",
    "Cryonis",
    "Ferrovax",
    "Coriolis",
    "Aethelgard",
    "Xelarvis",
    "Zaphus",
    "Halcyon",
    "Vespera",
    "Ignis Prime",
    "Solstice",
    "Oakhaven",
    "Borealis",
    "Thalassa",
    "Erebus",
    "Chronos",
]


    def planet_scan(self):
        self.scan_planets=random.choice(self.planet_list)
        self.planet_list.remove(self.scan_planets)
        print(f"{self.name} has scanned something")
        print(f"It is the planet {self.scan_planets}")

    def discovery(self):
        self.discoveries=[]
        self.discoveries.append(self.scan_planets)
        for i in self.discoveries:
            print(i)

menu()
choice=int(input("Enter the type of Spacecraft: "))

match choice:
    case 1:
        player=Fighter_Ship()
        fighter_menu()
        fighter_choice=int(input("Enter choice: "))

        match fighter_choice:
            case 1:
                player.attack()
            case 2:
                player.weapon_info()
            case _:
                print("Enter a proper Function")
    case 2:
        player=Cargo_Ship()
        cargo_menu()
        cargo_choice=int(input("Enter choice: "))

        match cargo_choice:
            case 1:
                print("Unloaded",player.cargo_unload())
            case 2:
                print("Loaded",player.cargo_load())
            case 3:
                player.cargo_info()
            case _:
                print("Enter a proper function")
    case 3:
        player=Exploration_Ship()
        explore_menu()
        explore_choice=int(input("Enter choice: "))

        match explore_choice:
            case 1:
                player.planet_scan()
            case 2:
                player.discovery()
            case _:
                print("Enter a proper function")
    case _:
        print("Enter a proper ship to be made")