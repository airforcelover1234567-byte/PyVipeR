def menu():
    print("=====CHESS TOURNAMENT MANAGER=====")
    print("1.Register Player\n2.Create Match\n3.Record Match Result\n4.Display Players\n5.Display Matches\n6.Display Leaderboard\n7.Declare Winner\n8.Exit")

def registration():
    print("===REGISTRATION===")
    id=int(input("Enter your ID: "))
    name=str(input("Enter your name: "))
    print("Player registered Sucessfully")
    registrations.append(name)
    ids.append(id)
    return id,name

def choice():
    try:    
        choice=int(input("Enter your choice: "))
    except ValueError:
        print("Enter a proper choice")
        return choice

def retry():
    retry=int(input("Do you want to try again ?\n1.Yes   2.No "))
    return retry

class Registration:
    def __init__(self,id,name):
        self.id=id
        self.name=name

menu()
ids=[]
registrations=[]

match choice():
    case 1:
        registration()
        player1=Registration(registration())

    case 2:
        print(registrations)

while retry()==1:
    menu()
    choice()
    match(choice):
        case 1:
            registration()
            player1=Registration(registration())

        case 2:
            print(registrations)