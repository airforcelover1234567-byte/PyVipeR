# functions that return a function while changing it
def greet(func):
    def mod_func():
        print("Good Morning")
        func()
        print("Thanks for using this function")
    return mod_func

@greet
def hello():
    print("Hello World")

def add(a,b):
    print(a+b)