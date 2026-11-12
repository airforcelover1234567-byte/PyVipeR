target=int(input("Enter a number to check wether it is prime or not: "))

for i in range(2,target,1):
    if(target%i==0):
        print("The number is not a prime number")
        break
else:
        print("It is a prime number")