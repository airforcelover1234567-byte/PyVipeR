Details={
    "name":"Rounak Roy",
    "birth":"2/12/2011",
    "marks":98,
    "is_disciplined":True
}
print("1.Name  2.Birth  3.Marks  4.Behaviour")
choice=int(input("Enter your choice"))

match(choice):
    case 1:
        print(Details["name"])
    case 2:
        print(Details["birth"])
    case 3:
        print(Details["marks"])
    case 4:
        print(Details["is_disciplined"])
    case _:
        print("Enter a proper functi0on")