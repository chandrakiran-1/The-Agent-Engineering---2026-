n = { x : x*x for x in range(10)}
print(n)

even_square = { x : x*x for x in range(10) if x%2==0}
print(even_square)

odd_square = { x : x*x for x in range(10) if x%2 !=0}
print(odd_square)