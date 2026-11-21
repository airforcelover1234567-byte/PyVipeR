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

def match_play(match_1,match_2,final_match):
    match_no=len(name_list)/2
    if match_no%1!=0:
        print("Please enter another participants\nas having even number of players\nwill make it easier for the tournament")
    elif match_no>2:
        print("Please enter only 4 participants as this will make the game easier")
    else:
        match_1=[name_list[0],choice_list[0]]
        print(f"First match= {name_list[0]} vs {choice_list[0]}")
        match1_win=random.choice(match_1)
        print(f"The winner of the first match is {match1_win}")

        match_2=[name_list[1],choice_list[1]]
        print(f"First match= {name_list[1]} vs {choice_list[1]}")
        match2_win=random.choice(match_2)
        print(f"The winner of the second match is {match2_win}")

        print(f"Final match= {match1_win} vs {match2_win}")
        final_match=[match1_win,match2_win]
        winner=random.choice(final_match)

        return winner


retry_choice=None
choice_option=None
name=None
id=None
name_list=[]
id_list=[]
choice_list=[]
match_1=[]
match_2=[]
final_match=[]

menu()

while retry(retry_choice)!=2:
    menu()
    match choice(choice_option):
        case 1:
            id_input(id)
            name_input(name)
        case 2:
            if name_list:
                for i in range(1,len(name_list)+1,1):
                    if i%2==0:
                        choice_match=random.choice(name_list)
                        name_list.remove(choice_match)
                        choice_list.append(choice_match)
            else:
                print("Enter the data of some Participants")
                id_input(id)
                name_input(name)
        case 3:
            print("THe winner of the event is",match_play(match_1,match_2,final_match))
        case _:
            print("Enter a proper option")

