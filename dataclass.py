from dataclasses import dataclass
@dataclass
class Student:
    name : str
    age : int
s = Student("Chandu" , 20)
print(s)
print(s.name)
print(s.age)