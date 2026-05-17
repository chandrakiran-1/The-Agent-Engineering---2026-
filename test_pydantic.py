from pydantic import BaseModel
class Student(BaseModel):
    name : str
    age : int
s = Student(name = "chandu" , age = 20)
print(s)
s =  Student(name = 10 , age = "chandu")
print(s)