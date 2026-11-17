def fibonnaci(num):
    for i in range(1,num,1):
        j=1
        j=j+j
    return j

num=int(input("Enter the number you want the fibonacci series to go to:"))
print(fibonnaci(num))