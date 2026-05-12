def decorator(func):
    def wrapper():
        print("before the func:")
        func()
        print("after the function:")
    return wrapper
@decorator
def hello():
     print("hello world")
hello()