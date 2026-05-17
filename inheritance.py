class Parent:
    def house(self):
        print("value is 20 cr:")
class Child(Parent):
    pass
c = Child()
c.house()

class Animal:
    def animal(self):
        print("Animal is there:")
class Dog(Animal):
    print("the dog is barking:")
    pass
d = Dog()
d.animal()

class Vehicle:
    def Start(self):
        print("the car is Started:")
class Car(Vehicle):
    def Drive(self):
        print("the car is driving by  her:")
    pass
car = Car()
car.Start()

class Parent:
    def show(self):
        print("Parent-class")
class Child(Parent):
    def showex(self):
        super().show()
        print("child - class")
c = Child()
c.showex()