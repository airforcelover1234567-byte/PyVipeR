def menu():
    print("=====CHESS TOURNAMENT MANAGER=====")
    print("1.Register Player\n2.Create Match\n3.Record Match Result\n4.Display Players\n5.Display Matches\n6.Display Leaderboard\n7.Declare Winner\n8.Exit")

def registration():
    print("===REGISTRATION===")
    id=int(input("Enter your ID: "))
    name=str(input("Enter your name: "))

menu()
try:    
    choice=int(input("Enter your choice: "))
except ValueError:
    print("Enter a proper choice")

match(choice):
    case 1:
        registration()