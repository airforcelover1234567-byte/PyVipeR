def menu():
    print("1.Bank  2.Account")

class Bank:
    def __init__(self):
        self.accounts=[]
        self.next_acc_no=1

    def create(self):
        self.name=name
        self.acc_no=acc_no
        name=int(input("Enter your name: "))
        acc_no=int(input("Enter your Acc. No : "))

class Account:
    def __init__(self,name,balance,acc_no):
        self.name=name
        self.balance=balance
        self.acc_no=acc_no

    def deposit(self):
        deposit=int(input("Enter the money you want to deposit: "))

choice=int(input("Enter your choice: "))
match choice:
    case 1:
        acc1=Bank.create()