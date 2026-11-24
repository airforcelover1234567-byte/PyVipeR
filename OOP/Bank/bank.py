class Bank:
    def __init__(self):
        self.accounts=[]
        self.next_acc_no=1


class Account:
    def __init__(self,name,balance,acc_no):
        self.name=name
        self.balance=balance
        self.acc_no=acc_no

    def deposit(self):
        deposit=int(input("Enter the money you want to deposit: "))