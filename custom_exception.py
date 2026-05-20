class ZeroError(Exception):
    pass
n = 0
if n == 0:
    raise ZeroError("the number cant be zero:")
print("the num is :" , n)