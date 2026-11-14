import random

number=random.randint(1,100)
tries=5

for tries in range(5,0,-1):
    print(f"You have {tries} left")
    guess=int(input("Enter your guess: "))
    if guess<number:
        print("Higher")
    elif guess>number:
        print("Lower")
    else:
        print("You have won")
        break