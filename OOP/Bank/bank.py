def menu():
    print("---PYBANK---")

def options():
    print("1. Create a Bank Account\n2. Login to an Existing Account\n3. View Bank Information\n4. Exit")

menu()
options()
choice=int(input("Enter your choice: "))

class Bank:
    def __init__(self,name,age,deposit):
        self.name=name
        self.age=age
        self.deposit=deposit

    def create(self):
        self.name=str(input("Enter your name: "))
        self.age=int(input("Enter your age: "))
        self.deposit=int(input("Enter the money you want to deposit: "))
        return self.name

match choice:
    case 1:
        Bank().create