print("1.Message 2.Message 3.Message 4.Message")
choice=int(input("Enter your choice: "))

match choice:
    case 1:
        print("Tui ekta kutta")
    case 2:
        print("Haramzada")
    case 3:
        print("Laure")
    case 4:
        print("Chacha")
    case _:
        print("Saale select something")