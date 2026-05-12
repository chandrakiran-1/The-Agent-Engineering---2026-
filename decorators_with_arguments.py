def decorators(func):
    def wrapper(*args , **kwargs):
        print("before function:")
        func(*args , **kwargs)
        print("After function:")
    return wrapper

@decorators
def greet(name):
    print(f"Hello, {name}")
greet("chandu")

@decorators
def user(age , rollno):
    print( "age : ",age ,"rollno : ",rollno)
user(age=20 , rollno=11)