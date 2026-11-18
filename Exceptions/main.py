try:
    age=int(input("Enter your age: "))
    print(age)
    income=20000
    risk=income/age
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print("Invalid Value")