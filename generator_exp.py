# list gives all values immediately .generator gives one value at a time . 
n = ( i for i in range(10))
print(n)
print(next(n))
print(next(n))