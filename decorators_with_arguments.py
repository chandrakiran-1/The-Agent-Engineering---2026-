def decorators(func):
    def wrapper(*args, **kwargs):
        print("Before function:")
        func(*args,**kwargs)
        print("After function:")
    return wrapper
@decorators
def wish(name):
    print(f"hello {name}")
wish("chandu")

@decorators
def info(age , rollno):
    print("age :",age , "rollno :",rollno)
info(age=21, rollno=11)