class NegativeError(Exception):
    pass
n = -1
if n < 0:
    raise NegativeError("The number cant be zero")
print("the num is : " , n)