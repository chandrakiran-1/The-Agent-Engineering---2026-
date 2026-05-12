def decorator(func):
    def wrapper():
        print("before function:")
        func()
        print("after function:")
    return wrapper
@decorator
def hello():
    print("hello function:")
hello()