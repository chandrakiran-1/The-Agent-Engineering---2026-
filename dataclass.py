from dataclasses import dataclass
@dataclass
class Student:
    name : str
    age : int
s = Student("chandu", 20)
print(s)