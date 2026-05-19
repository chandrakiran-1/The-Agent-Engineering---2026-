from collections import namedtuple
std = namedtuple("std",["name", "age", "mail"])
std = std("Chandu",20 , "gudlachandrakiran@gmail.com")
print(std.name)
print(std.age)
print(std.mail)

car = namedtuple("car",["name","model","brand"])
car = car("benz","320d","mercerdes")
print(car.name)
print(car.model)
print(car.brand)    