def question_1():
    print("The First Question")
    print("1. What is the value of pi upto 2 decimal places ?")
    print("The options are \n")
    print("1) 3.14  2)6.02  3)4.96  4)5.12")
    
def greet(name):
    print("Welcome to the quiz")
    print(f"Hello {name}")
    print("\n")

name=str(input("Enter your name: "))
greet(name)
print(question_1())
try:
    ans1=int(input("Enter your answer: "))
    if ans1==1:
        print("Good answer")
    else:
        print("Wrong answer")
except ValueError:
    print("Enter  a proper value")