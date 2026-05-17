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