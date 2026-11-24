class Account:
    def __init__(self,holder,balance,account_no):
        self.holder=holder
        self.balance=balance
        self.account_no=account_no

    def deposit(self):
        deposit=int(input("Enter the amount of money you want to deposit: "))
        self.account_no=int(input("Enter the account_no of the receiver: "))
        if self.account_no==acc2.account_no:
            acc1.balance-=deposit
            acc2.balance+=deposit
            print("You have successfully deposited ",deposit)
        else:
            print("Return a proper account no of an account")
        
acc1=Account("Rounak",5000,312)
acc2=Account("Sounak",2000,127)
choice=int(input("Enter your choice: "))
print("1.Deposit  2.Withdraw  3.Balance")

match choice:
    case 1:
        acc1.deposit()
