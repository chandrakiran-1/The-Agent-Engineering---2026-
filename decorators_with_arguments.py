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