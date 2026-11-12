age=int(input("Enter your age: "))

if age>120:
    print("You are probably dead")
elif age>=18:
    print("You are allowed to vote")
    print("You are a adult")
elif 18>age>=13:
    print("You are a teenager")
else:
    print("You are a child")