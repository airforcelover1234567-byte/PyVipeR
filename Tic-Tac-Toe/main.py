import random

def menu(a,b,c,d,e,f,g,h,i):
    print(a,b,c)
    print(d,e,f)
    print(g,h,i)

a,b,c,d,e,f,g,h,i=str(1,2,3,4,5,6,7,8,9)
menu(a,b,c,d,e,f,g,h,i)

for i in range(0,9,1):
    choice=str(input("Enter your choice: "))
    print(choice)