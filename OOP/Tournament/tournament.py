import random

def menu():
    print("=====CHESS TOURNAMENT MANAGER=====")
    print("1.Register Player\n2.Create Match\n3.Record Match Result\n4.Display Players\n5.Display Matches\n6.Display Leaderboard\n7.Declare Winner\n8.Exit")

def choice(choice_option):
    try:
        choice_option=int(input("Enter your choice: "))
    except ValueError:
        print("Enter a valid choice Option")
    return choice_option

def name_input(name):
    name=str(input("Enter your name: "))
    name_list.append(name)

def id_input(id):
    try:
        id=int(input("Enter your id: "))
    except:
        print("Enter a valid ID")
    id_list.append(id) 

def retry(retry_choice):
    print("Do you want to retry ?")
    print("1.YES  2.NO")
    try:
        retry_choice=int(input("Enter your choice if you want to retry: "))
    except ValueError:
        print("Enter a proper function")
    return retry_choice

retry_choice=None
choice_option=None
name=None
id=None
name_list=[]
id_list=[]

menu()

while retry(retry_choice)!=2:
    menu()
    match choice(choice_option):
        case 1:
            id_input(id)
            name_input(name)
        case 2:
            if name_list:
                choice_list=random.choice(name_list)
                name_list.remove(choice_list)
            else:
                print("Enter the data of some Participants")
                id_input(id)
                name_input(name)
        case 3:
            print(name_list)
        case _:
            print("Enter a proper option")

