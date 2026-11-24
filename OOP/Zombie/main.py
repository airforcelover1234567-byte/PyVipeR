from player import Player

def menu():
    print("===ZOMBIE GAME===")

name=str(input("Enter your name: "))
c_health=100
MAX_HEALTH=100
c_stam=100
MAX_STAM=100
hunger=10
thirst=10
inventory=["Knife","Water Bottle","Burger"]
equip_weapon=False
User=Player(name,c_health,MAX_HEALTH,c_stam,MAX_STAM,hunger,thirst,inventory,equip_weapon)