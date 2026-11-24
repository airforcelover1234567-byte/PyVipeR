def menu():
    print("---PYBANK---")

def options():
    print("1. Create a Bank Account\n2. Login to an Existing Account\n3. View Bank Information\n4. Exit")

menu()
options()
acc=[]

class Bank:
    def __init__(self):
        self.name
        self.age
        self.deposit

    def user_input(self):
        self.name=str(input("Enter your name: "))
        self.age=int(input("Enter your age: "))
        self.deposit=int(input("Enter your deposit: "))

choice=int(input("Enter your choice: "))

match choice:
    case 1:
        acc=Bank()
